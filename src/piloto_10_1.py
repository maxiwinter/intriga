import numpy as np, zlib, bz2, lzma, os, gzip, math

rng = np.random.default_rng(42)
results = {}

def Lbits(b): return len(b)*8
def generic_C(data):
    return min(Lbits(zlib.compress(data,9)), Lbits(bz2.compress(data,9)), Lbits(lzma.compress(data)))
def code_bits(src): return Lbits(gzip.compress(src.encode()))

# ---------- A. LORENZ ----------
SIG,RHO,BET = 10.0,28.0,8/3
DT=0.01
def lorenz_step(s):
    def f(v):
        x,y,z=v; return np.array([SIG*(y-x), x*(RHO-z)-y, x*y-BET*z])
    k1=f(s); k2=f(s+DT/2*k1); k3=f(s+DT/2*k2); k4=f(s+DT*k3)
    return s+DT/6*(k1+2*k2+2*k3+k4)
RANGES=np.array([[-25,25],[-30,30],[0,55]],float)
def quant(traj):
    lo=RANGES[:,0]; hi=RANGES[:,1]
    q=np.clip(np.floor((traj-lo)/(hi-lo)*256),0,255).astype(np.uint8)
    return q
s=np.array([1.0,1.0,1.0])
for _ in range(1000): s=lorenz_step(s)
IC=s.copy()
N=20000
traj=np.empty((N,3))
for i in range(N):
    s=lorenz_step(s); traj[i]=s
ref_q=quant(traj)
lorenz_bytes=ref_q.tobytes()

LORENZ_SRC="""def f(v):x,y,z=v;return[10*(y-x),x*(28-z)-y,x*y-8/3*z]
integrador RK4 dt=0.01, cuantizador 8 bits rangos [-25,25][-30,30][0,55]"""
lorenz_code=code_bits(LORENZ_SRC)
param_bits=3*64

def trunc_ic(ic,p):
    lo=RANGES[:,0]; hi=RANGES[:,1]
    cells=2**p
    idx=np.clip(np.floor((ic-lo)/(hi-lo)*cells),0,cells-1)
    return lo+(idx+0.5)*(hi-lo)/cells

def match_len(p,nmax):
    s=trunc_ic(IC,p); 
    for i in range(nmax):
        s=lorenz_step(s)
        if not np.array_equal(quant(s[None,:])[0],ref_q[i]): return i
    return nmax

ps=list(range(12,54,4))
matches={p:match_len(p,N) for p in ps}

def lorenz_C(n):
    best=24*n  # literal fallback
    for p in ps:
        m=min(matches[p],n)
        c=lorenz_code+param_bits+3*p+24*(n-m)
        best=min(best,c)
    return best

lorenz_rows=[]
for n in [1000,2500,5000,10000,20000]:
    L0=24*n
    Cg=generic_C(ref_q[:n].tobytes())
    Cm=lorenz_C(n)
    lorenz_rows.append((n,L0,Cg/L0,Cm/L0))
results['lorenz_scaling']=lorenz_rows
# slope: steps per extra IC bit (only where not saturated)
valid=[(3*p, matches[p]) for p in ps if matches[p]<N and matches[p]>0]
if len(valid)>=2:
    xs=np.array([v[0]/3 for v in valid]); ys=np.array([v[1] for v in valid])
    slope=np.polyfit(xs,ys,1)[0]
else: slope=float('nan')
results['lorenz_slope_steps_per_bit']=slope
results['lorenz_matches']={p:matches[p] for p in ps}

# ---------- B/C. CELLULAR AUTOMATA ----------
W,T=256,400
def run_ca(rule,init,T):
    rows=np.empty((T,W),np.uint8); r=init.copy()
    tbl=np.array([(rule>>i)&1 for i in range(8)],np.uint8)
    for t in range(T):
        rows[t]=r
        idx=(np.roll(r,1)<<2)|(r<<1)|np.roll(r,-1)
        r=tbl[idx]
    return rows
init=rng.integers(0,2,W).astype(np.uint8)
ca110=run_ca(110,init,T); ca30=run_ca(30,init,T)
b110=np.packbits(ca110).tobytes(); b30=np.packbits(ca30).tobytes()
CA_SRC="autómata elemental: regla r, fila inicial w bits, T pasos, vecindad 3, frontera periódica"
ca_code=code_bits(CA_SRC)
ca_gen=ca_code+8+W+32

# ---------- D. PRNG ----------
prng_bytes=np.random.default_rng(7).integers(0,256,32768,dtype=np.uint8).tobytes()
prng_gen=code_bits("PCG64 numpy seed=7, 32768 bytes")+64

# ---------- E. NOISE ----------
noise=os.urandom(32768)

# ---------- SURROGATES ----------
bits110=np.unpackbits(np.frombuffer(b110,np.uint8)); perm=rng.permutation(bits110.size)
b110_sur=np.packbits(bits110[perm]).tobytes()
lz=np.frombuffer(lorenz_bytes,np.uint8).copy(); rng.shuffle(lz); lorenz_sur=lz.tobytes()

# ---------- OUT-OF-SAMPLE: inferir regla ----------
def infer_rule(rows):
    votes=np.zeros((8,2),int)
    for t in range(len(rows)-1):
        r=rows[t]; idx=(np.roll(r,1)<<2)|(r<<1)|np.roll(r,-1)
        for k in range(8):
            m=idx==k
            votes[k,0]+=int((rows[t+1][m]==0).sum()); votes[k,1]+=int((rows[t+1][m]==1).sum())
    rule=sum((1<<k) for k in range(8) if votes[k,1]>votes[k,0])
    return rule
def oos(rows):
    tr=rows[:40]; rule=infer_rule(tr)
    r=rows[39].copy(); mism=0; tot=0
    tbl=np.array([(rule>>i)&1 for i in range(8)],np.uint8)
    for t in range(40,len(rows)):
        idx=(np.roll(r,1)<<2)|(r<<1)|np.roll(r,-1); pred=tbl[idx]
        mism+=int((pred!=rows[t]).sum()); tot+=W; r=rows[t]
    ptest=mism/tot
    H=0 if ptest in (0,1) else -(ptest*math.log2(ptest)+(1-ptest)*math.log2(1-ptest))
    Ltest=tot*H + (0 if mism==0 else 0)
    g=(ca_code+8+Ltest)/tot
    return rule,ptest,g
noise_rows=np.unpackbits(np.frombuffer(noise[:W*T//8],np.uint8)).reshape(T,W)
results['oos']={'R110':oos(ca110),'R30':oos(ca30),'ruido':oos(noise_rows)}

# ---------- TABLA PRINCIPAL ----------
def row(name,data,gen_bits=None):
    L0=Lbits(data); Cg=generic_C(data)
    rg=Cg/L0; rm=min(rg,(gen_bits/L0)) if gen_bits else rg
    return (name,L0,round(rg,4),round(rm,4) if gen_bits else None)
table=[row("Lorenz (20k pasos)",lorenz_bytes,lorenz_C(N)),
       row("Regla 110",b110,ca_gen),
       row("Regla 30",b30,ca_gen),
       row("PRNG (PCG64)",prng_bytes,prng_gen),
       row("Ruido (urandom)",noise),
       row("Surrogate R110 (bits mezclados)",b110_sur),
       row("Surrogate Lorenz (bytes mezclados)",lorenz_sur)]
results['table']=table

for t in table: print(t)
print("pendiente Lorenz (pasos/bit CI):",round(slope,1))
print("matches:",results['lorenz_matches'])
print("escalamiento Lorenz (n,L0,rho_gen,rho_model):",lorenz_rows)
print("OOS:",results['oos'])

import numpy as np, math, time
from mpmath import mp, mpf, floor as mfloor

# ---------- TEST 1: piso float64 — referencia en precision extendida (160 bits) ----------
mp.prec = 160
SIG,RHO,BET = mpf(10), mpf(28), mpf(8)/mpf(3)
DT = mpf(1)/mpf(100)
def step(s):
    def f(v):
        x,y,z=v
        return (SIG*(y-x), x*(RHO-z)-y, x*y-BET*z)
    k1=f(s); k2=f(tuple(s[i]+DT/2*k1[i] for i in range(3)))
    k3=f(tuple(s[i]+DT/2*k2[i] for i in range(3)))
    k4=f(tuple(s[i]+DT*k3[i] for i in range(3)))
    return tuple(s[i]+DT/6*(k1[i]+2*k2[i]+2*k3[i]+k4[i]) for i in range(3))

LO=(mpf(-25),mpf(-30),mpf(0)); HI=(mpf(25),mpf(30),mpf(55))
def q8(s):
    out=[]
    for i in range(3):
        v=int(mfloor((s[i]-LO[i])/(HI[i]-LO[i])*256))
        out.append(min(255,max(0,v)))
    return tuple(out)

t0=time.time()
s=(mpf(1),mpf(1),mpf(1))
for _ in range(500): s=step(s)
IC=s
N=5500
ref=[]
for _ in range(N):
    s=step(s); ref.append(q8(s))
print("ref extendida lista", round(time.time()-t0,1),"s")

def trunc(ic,p):
    out=[]
    for i in range(3):
        cells=mpf(2)**p
        idx=mfloor((ic[i]-LO[i])/(HI[i]-LO[i])*cells)
        out.append(LO[i]+(idx+mpf(1)/2)*(HI[i]-LO[i])/cells)
    return tuple(out)

for p in [40,52,64,76]:
    s=trunc(IC,p); m=N
    for i in range(N):
        s=step(s)
        if q8(s)!=ref[i]: m=i; break
    print(f"prec.extendida p={p}: match={m}  ({'sin saturar' if m<N else 'tope N'})")
print()

# ---------- TEST 2: barrido de epsilon (eta) en float64, Lorenz + ruido continuo ----------
SIGf,RHOf,BETf,DTf=10.0,28.0,8/3,0.01
def stepf(s):
    def f(v):
        x,y,z=v; return np.array([SIGf*(y-x), x*(RHOf-z)-y, x*y-BETf*z])
    k1=f(s);k2=f(s+DTf/2*k1);k3=f(s+DTf/2*k2);k4=f(s+DTf*k3)
    return s+DTf/6*(k1+2*k2+2*k3+k4)
R=np.array([[-25,25],[-30,30],[0,55]],float)
def qb(traj,b):
    lo,hi=R[:,0],R[:,1]
    return np.clip(np.floor((traj-lo)/(hi-lo)*(2**b)),0,2**b-1).astype(np.int32)
s=np.array([1.0,1.0,1.0])
for _ in range(1000): s=stepf(s)
ICf=s.copy(); Nf=5000
traj=np.empty((Nf,3))
for i in range(Nf):
    s=stepf(s); traj[i]=s

def truncf(ic,p):
    lo,hi=R[:,0],R[:,1]; cells=2.0**p
    idx=np.clip(np.floor((ic-lo)/(hi-lo)*cells),0,cells-1)
    return lo+(idx+0.5)*(hi-lo)/cells

code_bits=1252  # gzip del fuente declarado (piloto)
CK=3*52
rows=[]
for b in [4,6,8,10,12]:
    refq=qb(traj,b)
    s=truncf(ICf,52); m=Nf
    for i in range(Nf):
        s=stepf(s)
        if not np.array_equal(qb(s[None,:],b)[0],refq[i]): m=i; break
    L0=3*b*Nf
    C=code_bits+192+CK*math.ceil(Nf/max(m,1))
    rows.append((b,m,L0,C,C/L0))
    print(f"Lorenz b={b}: horizonte={m}  L0={L0}  C={C}  rho={C/L0:.4f}")
print()
print("eta_eps (dif. finitas entre resoluciones consecutivas, Lorenz):")
for i in range(1,len(rows)):
    b0,m0,L00,C0,_=rows[i-1]; b1,m1,L01,C1,_=rows[i]
    eta=(C1-C0)/(L01-L00)
    print(f"  b {b0}->{b1}: dC={C1-C0}  dL0={L01-L00}  eta={eta:.4f}")
print()
# ruido continuo: uniforme quantizado — M0 gana siempre => eta=1 por construccion; verificacion empirica a b=8,16
import zlib,bz2,lzma
rng=np.random.default_rng(11)
u=rng.random((Nf,3))
for b in [8,16]:
    q=np.clip(np.floor(u*(2**b)),0,2**b-1).astype(np.uint16 if b>8 else np.uint8)
    data=q.tobytes()
    L0=len(data)*8
    Cg=min(len(zlib.compress(data,9)),len(bz2.compress(data,9)),len(lzma.compress(data)))*8
    print(f"ruido continuo b={b}: r_generic={Cg/L0:.4f} -> rho_MDL=1 (gana M0); eta=1")

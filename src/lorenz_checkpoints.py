# lorenz_checkpoints.py — Enmienda 6 (trazabilidad), verificación de herencia 2026-08-26
#
# Genera, con script versionado, dos números que el informe del piloto citaba sin
# código que los produjera:
#   (1) codificador generativo de Lorenz con checkpoints (re-sincronización cada
#       horizonte de Lyapunov) hasta n = 20.000: imprime C, ρ y nº de checkpoints;
#   (2) longitudes de coincidencia en precisión extendida (160 bits) y ajuste de
#       pendiente (pasos por bit de condición inicial) global y por tramos.
# Reproduce exactamente las constantes de piloto_10_1.py (generación de la
# trayectoria float64, cuantizador, fuente declarada) y de
# verificacion_piso_y_eta.py (referencia extendida, costo por checkpoint).
# Sin semillas: todo es determinista (aritmética float64 y mpmath a 160 bits).

import numpy as np, gzip, math, time
from mpmath import mp, mpf, floor as mfloor

# ---------- (1) CODIFICADOR CON CHECKPOINTS, float64, hasta n=20000 ----------
SIG, RHO, BET = 10.0, 28.0, 8/3
DT = 0.01
def lorenz_step(s):
    def f(v):
        x, y, z = v; return np.array([SIG*(y-x), x*(RHO-z)-y, x*y-BET*z])
    k1 = f(s); k2 = f(s+DT/2*k1); k3 = f(s+DT/2*k2); k4 = f(s+DT*k3)
    return s+DT/6*(k1+2*k2+2*k3+k4)
RANGES = np.array([[-25, 25], [-30, 30], [0, 55]], float)
def quant(traj):
    lo = RANGES[:, 0]; hi = RANGES[:, 1]
    return np.clip(np.floor((traj-lo)/(hi-lo)*256), 0, 255).astype(np.uint8)

s = np.array([1.0, 1.0, 1.0])
for _ in range(1000): s = lorenz_step(s)
IC = s.copy()
N = 20000
traj = np.empty((N, 3))
for i in range(N):
    s = lorenz_step(s); traj[i] = s
ref_q = quant(traj)

LORENZ_SRC = """def f(v):x,y,z=v;return[10*(y-x),x*(28-z)-y,x*y-8/3*z]
integrador RK4 dt=0.01, cuantizador 8 bits rangos [-25,25][-30,30][0,55]"""
code_bits = len(gzip.compress(LORENZ_SRC.encode()))*8   # mismo cómputo que piloto_10_1.py
param_bits = 3*64
P_CK = 52                 # bits por coordenada de cada checkpoint (precisión float64 efectiva)
CK = 3*P_CK               # costo de un checkpoint

def trunc_ic(ic, p):
    lo = RANGES[:, 0]; hi = RANGES[:, 1]; cells = 2**p
    idx = np.clip(np.floor((ic-lo)/(hi-lo)*cells), 0, cells-1)
    return lo+(idx+0.5)*(hi-lo)/cells
def match_len(p, nmax):
    s = trunc_ic(IC, p)
    for i in range(nmax):
        s = lorenz_step(s)
        if not np.array_equal(quant(s[None, :])[0], ref_q[i]): return i
    return nmax

h = match_len(P_CK, N)    # horizonte de re-sincronización (referencia float64)
print(f"codigo fuente comprimido: {code_bits} bits; parametros: {param_bits} bits; "
      f"checkpoint: {CK} bits (p={P_CK}/coord)")
print(f"horizonte float64 (p={P_CK}, 8 bits/coord): {h} pasos")
print()
print("codificador con checkpoints (n, L0, k=ceil(n/h), C, rho):")
for n in [1000, 2500, 5000, 10000, 20000]:
    L0 = 24*n
    k = math.ceil(n/h)
    C = code_bits + param_bits + CK*k
    print(f"  n={n:6d}  L0={L0:6d}  k={k}  C={C}  rho={C/L0:.4f}")
print(f"nota de trazabilidad: verificacion_piso_y_eta.py cablea code_bits=1252; el gzip del "
      f"fuente declarado da {code_bits}. Con {code_bits} y k=ceil(n/h) se reproduce el 0.0053 "
      f"del informe; con 1252 daria {(1252+param_bits+CK*8)/480000:.4f}.")
print()

# ---------- (1b) BARRIDO DE RESOLUCIÓN CON code_bits TRAZADO (n=5000, como la Adenda) ----------
# Mismo procedimiento que verificacion_piso_y_eta.py (TEST 2), pero con el code_bits
# calculado arriba en lugar de la constante cableada 1252. eta_eps no depende de esa constante.
Nf = 5000
def qb(t, b):
    lo, hi = RANGES[:, 0], RANGES[:, 1]
    return np.clip(np.floor((t-lo)/(hi-lo)*(2**b)), 0, 2**b-1).astype(np.int32)
rows = []
print(f"barrido de resolucion, n={Nf}, code_bits={code_bits} (b, horizonte, L0, k, C, rho):")
for b in [4, 6, 8, 10, 12]:
    refq = qb(traj[:Nf], b)
    sb = trunc_ic(IC, P_CK); m = Nf
    for i in range(Nf):
        sb = lorenz_step(sb)
        if not np.array_equal(qb(sb[None, :], b)[0], refq[i]): m = i; break
    L0 = 3*b*Nf; k = math.ceil(Nf/max(m, 1)); C = code_bits + param_bits + CK*k
    rows.append((b, L0, C))
    print(f"  b={b:2d}  horizonte={m}  L0={L0}  k={k}  C={C}  rho={C/L0:.4f}")
print("eta_eps (dif. finitas entre resoluciones consecutivas):")
for i in range(1, len(rows)):
    b0, L00, C0 = rows[i-1]; b1, L01, C1 = rows[i]
    print(f"  b {b0}->{b1}: dC={C1-C0}  dL0={L01-L00}  eta={(C1-C0)/(L01-L00):.4f}")
print()

# ---------- (2) PRECISIÓN EXTENDIDA (160 bits) Y PENDIENTES ----------
mp.prec = 160
SIGm, RHOm, BETm = mpf(10), mpf(28), mpf(8)/mpf(3)
DTm = mpf(1)/mpf(100)
def step(s):
    def f(v):
        x, y, z = v
        return (SIGm*(y-x), x*(RHOm-z)-y, x*y-BETm*z)
    k1 = f(s); k2 = f(tuple(s[i]+DTm/2*k1[i] for i in range(3)))
    k3 = f(tuple(s[i]+DTm/2*k2[i] for i in range(3)))
    k4 = f(tuple(s[i]+DTm*k3[i] for i in range(3)))
    return tuple(s[i]+DTm/6*(k1[i]+2*k2[i]+2*k3[i]+k4[i]) for i in range(3))
LO = (mpf(-25), mpf(-30), mpf(0)); HI = (mpf(25), mpf(30), mpf(55))
def q8(s):
    out = []
    for i in range(3):
        v = int(mfloor((s[i]-LO[i])/(HI[i]-LO[i])*256))
        out.append(min(255, max(0, v)))
    return tuple(out)
def trunc(ic, p):
    out = []
    for i in range(3):
        cells = mpf(2)**p
        idx = mfloor((ic[i]-LO[i])/(HI[i]-LO[i])*cells)
        out.append(LO[i]+(idx+mpf(1)/2)*(HI[i]-LO[i])/cells)
    return tuple(out)

t0 = time.time()
sm = (mpf(1), mpf(1), mpf(1))
for _ in range(500): sm = step(sm)
ICm = sm
Nm = 5500
ref = []
for _ in range(Nm):
    sm = step(sm); ref.append(q8(sm))
print(f"referencia extendida (160 bits) lista: {time.time()-t0:.1f} s  [tiempo, no medición]")

ps = [40, 52, 64, 76]
matches = {}
for p in ps:
    sm = trunc(ICm, p); m = Nm
    for i in range(Nm):
        sm = step(sm)
        if q8(sm) != ref[i]: m = i; break
    matches[p] = m
    print(f"  prec.extendida p={p}: match={m}  ({'sin saturar' if m < Nm else 'tope N'})")
print()

xs = np.array(ps, float); ys = np.array([matches[p] for p in ps], float)
slope_fit = np.polyfit(xs, ys, 1)[0]
slope_ends = (ys[-1]-ys[0])/(xs[-1]-xs[0])
segs = [(ps[i], ps[i+1], (matches[ps[i+1]]-matches[ps[i]])/(ps[i+1]-ps[i])) for i in range(len(ps)-1)]
LAMBDA = 0.906
pred = math.log(2)/LAMBDA/DT
print("pendiente (pasos por bit de condicion inicial, 1 bit = +1 bit/coord):")
print(f"  ajuste lineal global p={ps[0]}..{ps[-1]}: {slope_fit:.1f}")
print(f"  extremos (p={ps[0]}..{ps[-1]}):            {slope_ends:.1f}")
for a, b, sl in segs:
    print(f"  tramo p={a}->{b}: {sl:.1f}")
seg_vals = [sl for _, _, sl in segs]
print(f"  promedio de tramos: {np.mean(seg_vals):.1f}   rango: {min(seg_vals):.1f}-{max(seg_vals):.1f}")
print(f"  prediccion pre-registrada ln2/(lambda*dt), lambda={LAMBDA}: {pred:.1f}")
print(f"  discrepancia ajuste global vs prediccion: {100*(slope_fit-pred)/pred:+.1f} %  (SIN CAUSA ASIGNADA; se reporta, no se corrige)")

# contabilidad_completa_v2.py — v2: identidad exacta de g_total - g_pred (auditoria final)
#
# Identico a contabilidad_completa.py salvo por la seccion OOS, que ahora imprime A, B, H,
# g_pred, g_total, delta_g = g_total - g_pred y la identidad algebraica
#     delta_g = (A - B*g_pred) / (B + H)        [equivalentemente (A*H - B*G) / (H*(B+H))]
# con verificacion numerica por assert, SIN redondeo interno previo.
# El script v1 y su salida archivada NO se modifican (convencion un-archivo-por-version).
#
# --- cabecera original ---
# contabilidad_completa.py — cierre contable de L_U(M0) (Tarea 4)
#
# Recomputa la contabilidad del piloto §10.1 bajo la definición formal de
# protocol/definicion-L-M0.md, SIN modificar ningún script ni salida previos:
#
#   L_U(T) = L_id(T|M) + L_U(spec(T)|U_ref) + L_U(theta_T)   para TODO T, incluido M0
#   Familia de primer nivel del piloto: {M0 literal, zlib, bz2, lzma, generativo}
#   k = 5  ->  L_id = ceil(log2 5) = 3 bits, iguales para los cinco miembros
#   spec = 0 para los miembros 1-4 (primitivas declaradas de U_ref); el generativo paga
#
#   L0_full = L_U(M0) + L_U(D_eps|M0) = 3 + L0
#   rho_full = C / L0_full,  C = min sobre la familia de [L_U(T) + L_U(D|T)]
#
# Compara contra la convención histórica (rho_bare: sin identificadores, denominador L0)
# e imprime delta = rho_full - rho_bare por fila.
#
# PREDICCIÓN PRE-DECLARADA (a confirmar o refutar por esta salida):
#   |delta| cae bajo el redondeo de las tablas (~3 bits sobre denominadores >= 6e4).
#   Si alguna fila se mueve visiblemente, se reporta como hallazgo; NO se ajusta.
#
# Semillas y orden de llamadas al PRNG idénticos a piloto_10_1.py, para reproducir
# los surrogates. El control os.urandom es irreproducible por diseño (Enmienda 6b):
# se reporta por invariantes.

import numpy as np, zlib, bz2, lzma, gzip, os, math

# ---------- familia de primer nivel y regla de identificador ----------
FAMILIA = ["M0 literal", "zlib", "bz2", "lzma", "generativo"]
K = len(FAMILIA)
L_ID = math.ceil(math.log2(K))          # 3 bits
PRIMITIVAS = {"M0 literal", "zlib", "bz2", "lzma"}   # spec = 0, declaradas en U_ref

def Lbits(b): return len(b)*8
def code_bits(src): return Lbits(gzip.compress(src.encode()))

def L_modelo(nombre, spec_bits=0, theta_bits=0):
    """L_U(T) = L_id + spec + theta. M0 incluido, sin excepción."""
    assert nombre in FAMILIA, nombre
    if nombre in PRIMITIVAS:
        assert spec_bits == 0, "una primitiva declarada no paga spec"
    return L_ID + spec_bits + theta_bits

L_M0 = L_modelo("M0 literal")            # = 3 bits: el modelo nulo paga su identificador

# ---------- A. LORENZ (idéntico a piloto_10_1.py) ----------
rng = np.random.default_rng(42)          # MISMO orden de consumo que el piloto
SIG, RHO, BET, DT = 10.0, 28.0, 8/3, 0.01
def lorenz_step(s):
    def f(v):
        x, y, z = v; return np.array([SIG*(y-x), x*(RHO-z)-y, x*y-BET*z])
    k1 = f(s); k2 = f(s+DT/2*k1); k3 = f(s+DT/2*k2); k4 = f(s+DT*k3)
    return s+DT/6*(k1+2*k2+2*k3+k4)
RANGES = np.array([[-25, 25], [-30, 30], [0, 55]], float)
def quant(t):
    lo, hi = RANGES[:, 0], RANGES[:, 1]
    return np.clip(np.floor((t-lo)/(hi-lo)*256), 0, 255).astype(np.uint8)
s = np.array([1.0, 1.0, 1.0])
for _ in range(1000): s = lorenz_step(s)
IC = s.copy(); N = 20000
traj = np.empty((N, 3))
for i in range(N):
    s = lorenz_step(s); traj[i] = s
ref_q = quant(traj); lorenz_bytes = ref_q.tobytes()

LORENZ_SRC = """def f(v):x,y,z=v;return[10*(y-x),x*(28-z)-y,x*y-8/3*z]
integrador RK4 dt=0.01, cuantizador 8 bits rangos [-25,25][-30,30][0,55]"""
LOR_SPEC = code_bits(LORENZ_SRC)         # 1096 bits
LOR_THETA = 3*64                         # 192 bits
P_CK = 52; CK = 3*P_CK                   # 156 bits por checkpoint

def trunc_ic(ic, p):
    lo, hi = RANGES[:, 0], RANGES[:, 1]; cells = 2**p
    idx = np.clip(np.floor((ic-lo)/(hi-lo)*cells), 0, cells-1)
    return lo+(idx+0.5)*(hi-lo)/cells
def match_len(p, nmax):
    st = trunc_ic(IC, p)
    for i in range(nmax):
        st = lorenz_step(st)
        if not np.array_equal(quant(st[None, :])[0], ref_q[i]): return i
    return nmax
H_LOR = match_len(P_CK, N)               # h(p=52, eps=8 bits) medido
K_CK = math.ceil(N/H_LOR)
NIVEL_A = LOR_SPEC + LOR_THETA           # regla: spec + theta
NIVEL_B = CK*K_CK                        # trayectoria: checkpoints
LOR_GEN_SIN_ID = NIVEL_A + NIVEL_B

# ---------- B/C. AUTÓMATAS (mismo consumo de rng que el piloto) ----------
W, T = 256, 400
def run_ca(rule, init, T):
    rows = np.empty((T, W), np.uint8); r = init.copy()
    tbl = np.array([(rule >> i) & 1 for i in range(8)], np.uint8)
    for t in range(T):
        rows[t] = r
        idx = (np.roll(r, 1) << 2) | (r << 1) | np.roll(r, -1)
        r = tbl[idx]
    return rows
init = rng.integers(0, 2, W).astype(np.uint8)          # 2ª llamada a rng(42)
ca110 = run_ca(110, init, T); ca30 = run_ca(30, init, T)
b110 = np.packbits(ca110).tobytes(); b30 = np.packbits(ca30).tobytes()
CA_SRC = "autómata elemental: regla r, fila inicial w bits, T pasos, vecindad 3, frontera periódica"
CA_SPEC = code_bits(CA_SRC)                              # 800 bits
CA_GEN_SIN_ID = CA_SPEC + 8 + W + 32                     # regla + fila inicial + T

# ---------- D. PRNG ----------
prng_bytes = np.random.default_rng(7).integers(0, 256, 32768, dtype=np.uint8).tobytes()
PRNG_GEN_SIN_ID = code_bits("PCG64 numpy seed=7, 32768 bytes") + 64

# ---------- E. RUIDO (irreproducible por diseño) ----------
noise = os.urandom(32768)

# ---------- SURROGATES (3ª y 4ª llamadas a rng(42), mismo orden) ----------
bits110 = np.unpackbits(np.frombuffer(b110, np.uint8)); perm = rng.permutation(bits110.size)
b110_sur = np.packbits(bits110[perm]).tobytes()
lz = np.frombuffer(lorenz_bytes, np.uint8).copy(); rng.shuffle(lz); lorenz_sur = lz.tobytes()

# ---------- contabilidad por fila ----------
def genericos(data):
    """Devuelve (mejor_nombre, bits) entre los tres compresores primitivos."""
    c = {"zlib": Lbits(zlib.compress(data, 9)),
         "bz2":  Lbits(bz2.compress(data, 9)),
         "lzma": Lbits(lzma.compress(data))}
    n = min(c, key=c.get); return n, c[n]

def fila(nombre, data, gen_sin_id=None):
    L0 = Lbits(data)
    L0_full = L_M0 + L0                       # baseline completo
    gname, Cg = genericos(data)
    # --- convención histórica (bare): sin identificadores, denominador L0
    cand_bare = [L0, Cg] + ([gen_sin_id] if gen_sin_id else [])
    rho_bare = min(cand_bare)/L0
    # --- convención completa: cada modelo paga su identificador
    cand_full = [L_M0 + L0,                                   # M0
                 L_modelo(gname) + Cg]                        # mejor genérico
    if gen_sin_id:
        cand_full.append(L_modelo("generativo", gen_sin_id, 0))   # generativo
    C = min(cand_full)
    ganador = ["M0", gname, "generativo"][cand_full.index(C)]
    rho_full = C/L0_full
    return dict(nombre=nombre, L0=L0, r_generic=Cg/L0, rho_bare=rho_bare,
                C=C, L0_full=L0_full, rho_full=rho_full,
                delta=rho_full-rho_bare, ganador=ganador)

filas = [fila("Lorenz (20k, checkpoints)", lorenz_bytes, LOR_GEN_SIN_ID),
         fila("Regla 110", b110, CA_GEN_SIN_ID),
         fila("Regla 30", b30, CA_GEN_SIN_ID),
         fila("PRNG (PCG64)", prng_bytes, PRNG_GEN_SIN_ID),
         fila("Ruido (urandom)", noise),
         fila("Surrogate R110", b110_sur),
         fila("Surrogate Lorenz", lorenz_sur)]

print("="*104)
print("CONTABILIDAD COMPLETA — definicion protocol/definicion-L-M0.md")
print("="*104)
print(f"Familia de primer nivel: {FAMILIA}")
print(f"k = {K}  ->  L_id = ceil(log2 {K}) = {L_ID} bits para TODO miembro, M0 incluido")
print(f"spec = 0 para primitivas declaradas de U_ref: {sorted(PRIMITIVAS)}")
print(f"L_U(M0) = L_id + spec + theta = {L_ID} + 0 + 0 = {L_M0} bits   (M0 NO es gratis)")
print()
print("--- Tabla principal: rho_bare (historico) vs rho_full (baseline completo) ---")
print(f"{'dominio':<28} {'L0':>8} {'L0_full':>8} {'r_generic':>10} {'rho_bare':>10} {'rho_full':>10} {'delta':>11} {'gana':>12}")
print("-"*104)
for f in filas:
    print(f"{f['nombre']:<28} {f['L0']:>8} {f['L0_full']:>8} {f['r_generic']:>10.4f} "
          f"{f['rho_bare']:>10.4f} {f['rho_full']:>10.4f} {f['delta']:>+11.2e} {f['ganador']:>12}")
print()
print("--- Verificacion rho_full <= 1 ---")
todas_ok = True
for f in filas:
    ok = f['rho_full'] <= 1.0
    todas_ok &= ok
    print(f"  {f['nombre']:<28} rho_full = {f['rho_full']:.6f}  {'OK' if ok else '*** VIOLACION ***'}")
print(f"  => rho_full <= 1 en TODAS las filas: {todas_ok}")
print()
print("--- Prediccion pre-declarada: |delta| bajo el redondeo de 4 decimales (5e-5) ---")
peor = max(filas, key=lambda f: abs(f['delta']))
for f in filas:
    v = "confirmada" if abs(f['delta']) < 5e-5 else "REFUTADA (hallazgo)"
    print(f"  {f['nombre']:<28} |delta| = {abs(f['delta']):.3e}  -> {v}")
print(f"  => peor caso: {peor['nombre']}, |delta| = {abs(peor['delta']):.3e}")
print(f"  => rho a 4 decimales cambia en alguna fila: "
      f"{any(round(f['rho_bare'],4) != round(f['rho_full'],4) for f in filas)}")
print()

# ---------- descomposición Nivel A / Nivel B de Lorenz (deuda 4 de C ter) ----------
print("--- Descomposicion Nivel A / Nivel B de la descripcion de Lorenz (impresa, no derivada) ---")
print(f"  h(p={P_CK}, eps=8 bits) medido            = {H_LOR} pasos")
print(f"  k = ceil(n/h) = ceil({N}/{H_LOR})       = {K_CK} checkpoints")
print(f"  identificador L_id                     = {L_ID} bits")
print(f"  NIVEL A (regla: spec {LOR_SPEC} + theta {LOR_THETA}) = {NIVEL_A} bits   [fijo, no crece con n]")
print(f"  NIVEL B (trayectoria: {CK} x {K_CK})        = {NIVEL_B} bits   [crece con el horizonte]")
print(f"  TOTAL C = L_id + Nivel A + Nivel B      = {L_ID + NIVEL_A + NIVEL_B} bits")
print(f"  Nivel A como fraccion del total         = {NIVEL_A/(L_ID+NIVEL_A+NIVEL_B):.4f}")
print("  escalamiento por n (n, k, NivelA, NivelB, C, rho_full):")
for n in [1000, 2500, 5000, 10000, 20000]:
    kk = math.ceil(n/H_LOR); nb = CK*kk; C = L_ID + NIVEL_A + nb
    print(f"    n={n:6d}  k={kk}  A={NIVEL_A}  B={nb:5d}  C={C:5d}  rho_full={C/(L_M0+24*n):.4f}")
print()

# ---------- métricas fuera de muestra con baseline simétrico ----------
def infer_rule(rows):
    votes = np.zeros((8, 2), int)
    for t in range(len(rows)-1):
        r = rows[t]; idx = (np.roll(r, 1) << 2) | (r << 1) | np.roll(r, -1)
        for k in range(8):
            m = idx == k
            votes[k, 0] += int((rows[t+1][m] == 0).sum()); votes[k, 1] += int((rows[t+1][m] == 1).sum())
    return sum((1 << k) for k in range(8) if votes[k, 1] > votes[k, 0])

L_T_OOS = L_modelo("generativo", CA_SPEC, 8)   # id + fuente del automata + regla

def oos(rows):
    rule = infer_rule(rows[:40])
    r = rows[39].copy(); mism = 0; tot = 0
    tbl = np.array([(rule >> i) & 1 for i in range(8)], np.uint8)
    for t in range(40, len(rows)):
        idx = (np.roll(r, 1) << 2) | (r << 1) | np.roll(r, -1); pred = tbl[idx]
        mism += int((pred != rows[t]).sum()); tot += W; r = rows[t]
    ptest = mism/tot
    H = 0 if ptest in (0, 1) else -(ptest*math.log2(ptest)+(1-ptest)*math.log2(1-ptest))
    L_test = tot*H; L0_test = tot
    g_pred = L_test/L0_test
    g_bare = (CA_SPEC + 8 + L_test)/L0_test                 # historico, asimetrico
    g_full = (L_T_OOS + L_test)/(L_M0 + L0_test)            # simetrico
    return ptest, L_test, g_pred, g_bare, g_full

rng2026 = np.random.default_rng(2026)
noise_seed = rng2026.integers(0, 256, W*T//8, dtype=np.uint8).tobytes()
casos_oos = [("Regla 110", ca110), ("Regla 30", ca30),
             ("Ruido PRNG (semilla 2026)",
              np.unpackbits(np.frombuffer(noise_seed, np.uint8)).reshape(T, W))]

print("--- Generalizacion fuera de muestra: g_pred, g_total^bare (historico), g_total (simetrico) ---")
print(f"  L_U(T_train) = L_id {L_ID} + spec {CA_SPEC} + regla 8 = {L_T_OOS} bits")
print(f"  L_U(M0) = {L_M0} bits ;  L_U(D_test|M0) = {360*W} bits ;  denominador simetrico = {L_M0+360*W}")
print(f"{'dataset':<28} {'p_error':>9} {'L_test':>10} {'g_pred':>9} {'g_total^bare':>14} {'g_total':>10} {'g_tot-g_pred':>13}")
print("-"*104)
resultados_oos = []
for nombre, rows in casos_oos:
    ptest, L_test, gp, gb, gf = oos(rows)
    resultados_oos.append((nombre, ptest, L_test, gp, gb, gf))
    print(f"{nombre:<28} {ptest:>9.4f} {L_test:>10.1f} {gp:>9.4f} {gb:>14.4f} {gf:>10.4f} {gf-gp:>+13.4f}")
print()

# ---------- identidad exacta de g_total - g_pred (correccion de la auditoria final) ----------
# A = L_U(T_train) ; B = L_U(M0) ; G = L_U(D_test|T_train) ; H = L_U(D_test|M0)
#     g_pred  = G/H
#     g_total = (A+G)/(B+H)
#     g_total - g_pred = (A - B*g_pred)/(B+H) = (A*H - B*G)/(H*(B+H))
# NO es A/(B+H) salvo en el caso especial g_pred = 0.
A_OOS = L_T_OOS; B_OOS = L_M0; H_OOS = 360*W
print("--- Identidad exacta de g_total - g_pred (sin redondeo interno) ---")
print(f"  A = L_U(T_train) = {A_OOS} bits ; B = L_U(M0) = {B_OOS} bits ; H = L_U(D_test|M0) = {H_OOS} bits")
print("  g_total - g_pred = (A - B*g_pred)/(B + H) = (A*H - B*G)/(H*(B + H))")
print(f"  ATENCION: A/(B+H) = {A_OOS/(B_OOS+H_OOS):.7f} solo vale cuando g_pred = 0.")
print()
print(f"{'dataset':<28} {'G':>10} {'g_pred':>12} {'delta_g':>12} {'formula1':>12} {'formula2':>12} {'|dif|':>10}")
print("-"*104)
TOL = 1e-12
todas_id_ok = True
for nombre, ptest, G, gp, gb, gf in resultados_oos:
    delta_g = gf - gp
    f1 = (A_OOS - B_OOS*gp)/(B_OOS + H_OOS)                 # (A - B*g_pred)/(B+H)
    f2 = (A_OOS*H_OOS - B_OOS*G)/(H_OOS*(B_OOS + H_OOS))    # (A*H - B*G)/(H*(B+H))
    ok = abs(delta_g - f1) < TOL and abs(delta_g - f2) < TOL
    todas_id_ok &= ok
    assert ok, f"identidad violada en {nombre}: {delta_g} vs {f1} vs {f2}"
    print(f"{nombre:<28} {G:>10.1f} {gp:>12.9f} {delta_g:>12.9f} {f1:>12.9f} {f2:>12.9f} {abs(delta_g-f1):>10.2e}")
print(f"  => identidad verificada por assert (tol {TOL:g}) en todos los casos: {todas_id_ok}")
print()
print("  Lectura fila por fila:")
for nombre, ptest, G, gp, gb, gf in resultados_oos:
    if gp == 0.0:
        print(f"    {nombre:<28} g_pred = 0 EXACTO -> delta = A/(B+H) = {A_OOS}/{B_OOS+H_OOS} = {A_OOS/(B_OOS+H_OOS):.7f}")
    else:
        num = A_OOS - B_OOS*gp
        print(f"    {nombre:<28} g_pred = {gp:.9f} -> delta = (A - B*g_pred)/(B+H) = {num:.6f}/{B_OOS+H_OOS} = {(gf-gp):.7f}")
        print(f"    {'':<28}   (con g_pred = 1 exacto daria (A-B)/(B+H) = {(A_OOS-B_OOS)}/{B_OOS+H_OOS} = {(A_OOS-B_OOS)/(B_OOS+H_OOS):.7f})")
print()
print("  A cuatro decimales, TODAS redondean a 0.0088; la tabla publicada NO cambia.")
print(f"    R110/R30: {A_OOS/(B_OOS+H_OOS):.7f} -> {round(A_OOS/(B_OOS+H_OOS),4)}")
print(f"    ruido   : {(A_OOS-B_OOS)/(B_OOS+H_OOS):.7f} -> {round((A_OOS-B_OOS)/(B_OOS+H_OOS),4)}")
print()

# ---------- trazabilidad del antiguo cargo log2(3) ----------
print("--- Trazabilidad: el antiguo cargo log2(3) de seleccion de compresor ---")
print(f"  total historico Lorenz (sin identificador) = {LOR_SPEC} + {LOR_THETA} + {NIVEL_B} = {LOR_SPEC+LOR_THETA+NIVEL_B} bits")
print(f"  total full  Lorenz (con identificador)     = {L_ID} + {LOR_SPEC} + {LOR_THETA} + {NIVEL_B} = {L_ID+LOR_SPEC+LOR_THETA+NIVEL_B} bits")
print(f"  diferencia = {L_ID} bits (el identificador uniforme de primer nivel, k={K})")
print(f"  log2(3) = {math.log2(3):.4f} bits: cargo DECLARADO en informes anteriores pero NO incluido")
print(f"  en el total historico trazado ({LOR_SPEC+LOR_THETA+NIVEL_B} no contiene ningun sumando de seleccion).")
print()
print("Nota: g_total^bare NO es g_total. La primera divide por L(D_test|M0); la segunda por")
print("      L_U(M0)+L(D_test|M0). Los valores historicos del piloto son g_total^bare.")
print("Nota: el control os.urandom es irreproducible por diseno (Enmienda 6b); en la tabla")
print("      principal se reporta por invariantes (r_generic ~ 1, gana M0, rho_full = 1).")

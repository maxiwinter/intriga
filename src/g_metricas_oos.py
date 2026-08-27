# g_metricas_oos.py — separación formal de las métricas fuera de muestra (preprint v0.4)
#
# MOTIVO. piloto_10_1.py calcula una sola cantidad:
#     g = [L(T_train) + L(D_test|T_train)] / L(D_test|M0)
# es decir, cobra el modelo en el numerador pero NO cobra M0 en el denominador.
# Esa cantidad se denomina aquí g_total_bare y es la que produjo los valores
# históricos 0.0088 / 1.009 / 1.0088. Se conserva para trazabilidad.
#
# Este script imprime por separado, sin modificar ningún script ni salida previos:
#   g_pred       = L(D_test|T_train) / L(D_test|M0)                      [predictivo puro]
#   g_total_bare = [L(T_train) + L(D_test|T_train)] / L(D_test|M0)       [histórico, asimétrico]
#   g_total_full = [L(T_train) + L(D_test|T_train)] / [L(M0) + L(D_test|M0)]   [simétrico]
#
# g_total_full NO SE CALCULA: exige L_U(M0), el costo de descripción del modelo nulo,
# que el protocolo todavía no define. No se inventa un valor. Queda como deuda declarada.
#
# Reproduce exactamente el procedimiento oos() y las semillas de piloto_10_1.py
# (rng=42 para la fila inicial de los autómatas) y de ruido_oos_semilla.py (PCG64 2026).

import numpy as np, gzip, math

W, T = 256, 400
CA_SRC = "autómata elemental: regla r, fila inicial w bits, T pasos, vecindad 3, frontera periódica"
ca_code = len(gzip.compress(CA_SRC.encode()))*8
L_T = ca_code + 8          # fuente comprimida del autómata + identificador de regla (8 bits)

def run_ca(rule, init, T):
    rows = np.empty((T, W), np.uint8); r = init.copy()
    tbl = np.array([(rule >> i) & 1 for i in range(8)], np.uint8)
    for t in range(T):
        rows[t] = r
        idx = (np.roll(r, 1) << 2) | (r << 1) | np.roll(r, -1)
        r = tbl[idx]
    return rows

def infer_rule(rows):
    votes = np.zeros((8, 2), int)
    for t in range(len(rows)-1):
        r = rows[t]; idx = (np.roll(r, 1) << 2) | (r << 1) | np.roll(r, -1)
        for k in range(8):
            m = idx == k
            votes[k, 0] += int((rows[t+1][m] == 0).sum()); votes[k, 1] += int((rows[t+1][m] == 1).sum())
    return sum((1 << k) for k in range(8) if votes[k, 1] > votes[k, 0])

def metricas(rows):
    """Devuelve (regla, p_error, L_test, L0_test, g_pred, g_total_bare)."""
    rule = infer_rule(rows[:40])
    r = rows[39].copy(); mism = 0; tot = 0
    tbl = np.array([(rule >> i) & 1 for i in range(8)], np.uint8)
    for t in range(40, len(rows)):
        idx = (np.roll(r, 1) << 2) | (r << 1) | np.roll(r, -1); pred = tbl[idx]
        mism += int((pred != rows[t]).sum()); tot += W; r = rows[t]
    ptest = mism/tot
    H = 0 if ptest in (0, 1) else -(ptest*math.log2(ptest)+(1-ptest)*math.log2(1-ptest))
    L_test = tot*H                      # residuo bajo el modelo entrenado
    L0_test = tot                       # L(D_test | M0): 1 bit por celda, código literal
    return rule, ptest, L_test, L0_test, L_test/L0_test, (L_T + L_test)/L0_test

# ---------- datasets ----------
init = np.random.default_rng(42).integers(0, 2, W).astype(np.uint8)   # misma semilla que el piloto
casos = [("Regla 110", run_ca(110, init, T)),
         ("Regla 30",  run_ca(30,  init, T))]
rng = np.random.default_rng(2026)                                     # control negativo reproducible
noise = rng.integers(0, 256, W*T//8, dtype=np.uint8).tobytes()
casos.append(("Ruido PRNG (PCG64 semilla=2026)",
              np.unpackbits(np.frombuffer(noise, np.uint8)).reshape(T, W)))

print(f"L(T_train) = {L_T} bits (fuente comprimida {ca_code} + regla 8)")
print(f"L(D_test|M0) = {360*W} bits (360 filas x {W} celdas, codigo literal)")
print("L_U(M0) = NO DEFINIDO en el protocolo -> g_total_full NO se calcula (deuda declarada)")
print()
print(f"{'dataset':<32} {'p_error':>8} {'L_test':>10} {'g_pred':>10} {'g_total_bare':>14} {'g_total_full':>13}")
print("-"*92)
for nombre, rows in casos:
    rule, ptest, L_test, L0_test, g_pred, g_bare = metricas(rows)
    print(f"{nombre:<32} {ptest:>8.4f} {L_test:>10.1f} {g_pred:>10.4f} {g_bare:>14.4f} {'PENDIENTE':>13}")
print()
print("Nota 1: g_total_bare es la cantidad que imprime piloto_10_1.py (columna 3 de su OOS).")
print("        Reproduce los valores historicos 0.0088 (R110/R30) y 1.0088 (ruido con semilla).")
print("Nota 2: el control historico con os.urandom no tiene semilla; sus invariantes reportables")
print("        son p_error ~ 0.5 y g_total_bare > 1 (Enmienda 6b). No se compara cifra a cifra.")
print("Nota 3: g_pred y g_total_bare tienen denominadores distintos de g_total_full; no se")
print("        asume ninguna desigualdad entre ellos.")

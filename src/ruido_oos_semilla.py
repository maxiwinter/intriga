# ruido_oos_semilla.py — Enmienda 6(b): control de ruido dual para el test fuera de muestra
#
# piloto_10_1.py evalúa la generalización fuera de muestra sobre ruido de os.urandom,
# que es declaradamente irreproducible (sin semilla). Este script agrega la variante
# reproducible: ruido PRNG (PCG64, semilla declarada) tratado como autómata celular,
# con el MISMO procedimiento oos() de piloto_10_1.py (regla inferida de 40 filas,
# congelada, testeada en 360). Los invariantes reportables son p_error ≈ 0.5 y g > 1;
# la identidad de la "regla" espuria depende de la corrida y no se cita.
#
# Semilla declarada: 2026 (distinta de 42 y 7, usadas por el piloto para otros fines).

import numpy as np, gzip, math

W, T = 256, 400
CA_SRC = "autómata elemental: regla r, fila inicial w bits, T pasos, vecindad 3, frontera periódica"
ca_code = len(gzip.compress(CA_SRC.encode()))*8

def infer_rule(rows):
    votes = np.zeros((8, 2), int)
    for t in range(len(rows)-1):
        r = rows[t]; idx = (np.roll(r, 1) << 2) | (r << 1) | np.roll(r, -1)
        for k in range(8):
            m = idx == k
            votes[k, 0] += int((rows[t+1][m] == 0).sum()); votes[k, 1] += int((rows[t+1][m] == 1).sum())
    return sum((1 << k) for k in range(8) if votes[k, 1] > votes[k, 0])

def oos(rows):
    tr = rows[:40]; rule = infer_rule(tr)
    r = rows[39].copy(); mism = 0; tot = 0
    tbl = np.array([(rule >> i) & 1 for i in range(8)], np.uint8)
    for t in range(40, len(rows)):
        idx = (np.roll(r, 1) << 2) | (r << 1) | np.roll(r, -1); pred = tbl[idx]
        mism += int((pred != rows[t]).sum()); tot += W; r = rows[t]
    ptest = mism/tot
    H = 0 if ptest in (0, 1) else -(ptest*math.log2(ptest)+(1-ptest)*math.log2(1-ptest))
    g = (ca_code+8+tot*H)/tot
    return rule, ptest, g

SEED = 2026
rng = np.random.default_rng(SEED)
noise = rng.integers(0, 256, W*T//8, dtype=np.uint8).tobytes()
noise_rows = np.unpackbits(np.frombuffer(noise, np.uint8)).reshape(T, W)
rule, ptest, g = oos(noise_rows)
print(f"ruido PRNG (PCG64 semilla={SEED}) como automata, OOS 40 train / 360 test:")
print(f"  p_error_test = {ptest:.4f}   g = {g:.4f}   invariantes: p_error~0.5 -> {abs(ptest-0.5) < 0.02}, g>1 -> {g > 1}")
print(f"  (identificador de la regla espuria: dependiente de corrida; no se reporta como resultado)")

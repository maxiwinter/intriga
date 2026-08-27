# Protocolo experimental — Enmienda 6: trazabilidad y control de ruido dual

**Naturaleza de este documento.** Enmienda registrada el 2026-08-26, **antes del congelamiento** del protocolo y **antes de cualquier dataset empírico**. No nace de resultados: nace de la *verificación de herencia* del repositorio ensamblado (`docs/preprint/reproduccion-2026-08-26.md`), que reprodujo todas las salidas del piloto con semilla y detectó que tres números citados en el informe no eran generados por ningún script versionado. Es, por tanto, una corrección de proceso, no un ajuste a datos, y se documenta para que esa distinción quede auditable.

**Relación con el changelog v1.0 → v1.1.** El changelog define v1.1 = v1.0 + Enmiendas 1–5 y no se reescribe. Esta enmienda es su adenda. Nomenclatura para el congelamiento (acto del investigador): si el protocolo se congela después de esta enmienda, el documento consolidado es **v1.1 = v1.0 + Enmiendas 1–6**; si el investigador prefiere congelar 1–5 tal como estaban, esta enmienda abre v1.2. En ambos casos el hash del PDF consolidado debe declarar qué enmiendas incluye.

---

## 6(a) — Regla de trazabilidad (afecta §10, §13 y todo informe de resultados)

**Hallazgos de la verificación de herencia.**
1. El informe final del piloto citaba ρ_oracle = 0.0053 para Lorenz (20 000 pasos, codificador con checkpoints) sin que ningún script de `/src` produjera ese número: `piloto_10_1.py` imprime la fila con el codificador ingenuo (0.5307) y `verificacion_piso_y_eta.py` solo corre el codificador con checkpoints a n = 5000.
2. La pendiente "~64 pasos/bit en precisión extendida" se derivaba a mano de las longitudes de coincidencia archivadas; el script no la imprimía.
3. Al construir el script que cierra el punto 1 (`src/lorenz_checkpoints.py`) se descubrió un cuarto hueco: `verificacion_piso_y_eta.py` cablea `code_bits = 1252` como "gzip del fuente declarado (piloto)", pero el gzip del fuente declarado en `piloto_10_1.py` mide **1096 bits** (verificable también desde la salida archivada del codificador ingenuo: C(n=1000) = 1360 = 1096 + 192 + 72). Con 1096 y k = ⌈n/h⌉ checkpoints el 0.0053 del informe **se reproduce exactamente**; la constante 1252 desplaza en +156 bits los C del barrido de resolución de la Adenda (ρ ligeramente sobreestimados) y no afecta η_ε, que es una diferencia. Las erratas correspondientes están en el informe.

**Enmienda.** Todo número publicado en un informe del programa —tabla, texto o adenda— debe ser generado por un script versionado en `/src`, con su salida archivada en `/results`, de modo que `python src/<script>.py` reproduzca el número a la precisión reportada. Corolarios:
- Ninguna constante derivada (longitud de código fuente comprimido, costo de un checkpoint, horizonte de re-sincronización) se cablea a mano en un segundo script: se recalcula o se lee de la salida archivada del script que la produjo, con la referencia explícita.
- Un número derivado por cálculo manual a partir de salidas archivadas (una pendiente, un promedio) no es citable hasta que un script lo imprima.
- Si un número del informe no puede regenerarse, el informe lo declara en una sección de erratas, con el valor viejo visible (tachado o citado), el valor nuevo y el script que lo produce. Nada se reescribe silenciosamente.
- Los tiempos de cómputo impresos por los scripts no son mediciones y no se comparan.

## 6(b) — Control de ruido dual (afecta §10.1, control negativo, y §14 sobre el control negativo)

**Hallazgo.** El control negativo del piloto usa `os.urandom`, sin semilla. Su fila en la tabla principal es estable a cuatro decimales (r_generic ≈ 1.0005) por la alta entropía de la fuente, pero su fila en el test fuera de muestra no lo es: el identificador de la "regla" espuria inferida y el error de test varían entre corridas (informe: 166; salida archivada: 9; reproducción: 199; error 50.07 % vs 50.23 %), aunque los invariantes que el control debe exhibir se mantienen (p_error ≈ 0.5, g > 1).

**Enmienda.** El control negativo se desdobla:
1. **`os.urandom` se mantiene** como control negativo *declaradamente irreproducible*: su papel es que la fuente no dependa de ningún generador determinista que la familia de modelos pudiera, en principio, capturar. Sus **invariantes reportables** son p_error ≈ 0.5 y g > 1 (y, en la tabla principal, r_generic ≈ 1 y ρ_MDL = 1). **La identidad de la regla espuria es dependiente de corrida y no se cita** como resultado.
2. **Se agrega ruido PRNG con semilla declarada** (PCG64, semilla 2026; `src/ruido_oos_semilla.py`) para la fila reproducible del test fuera de muestra, con el mismo procedimiento `oos()` del piloto. Esta fila sí es citable a la precisión impresa.

La distinción se traslada a §14 del protocolo: todo control cuya fuente sea no determinista declara de antemano qué invariantes reporta y qué identificadores no.

---

## Estado de los tres huecos tras esta enmienda

| Hueco | Cierre |
|---|---|
| ρ_oracle Lorenz 20k sin script | `src/lorenz_checkpoints.py` → `results/lorenz-checkpoints-salida.txt`: 0.0053 confirmado (k = 8, code_bits = 1096) |
| "regla espuria 166" | Formulación invariante en el informe; fila reproducible con semilla en `results/ruido-oos-semilla-salida.txt` |
| Pendiente "~64" derivada a mano | Mismo script: ajuste lineal global, extremos, tramos, promedio y rango. La discrepancia con la predicción de 76.5 pasos/bit **sigue sin causa asignada** y se reporta, no se corrige |

Las Enmiendas 2 y 4 citan ρ = 0.0053 para Lorenz generativo: ese valor queda **confirmado** por script y no requiere corrección.

---

*Cambio no incluido en esta enmienda (pendiente de decisión del investigador): si `piloto_10_1.py` debe integrar el codificador con checkpoints en su tabla principal (hoy imprime el ingenuo, con el valor con checkpoints en el informe) o si la tabla publicada cita explícitamente los dos scripts. Ambas opciones cumplen 6(a).*

**Protocolo tras esta enmienda: v1.0 + Enmiendas 1–6, listo para congelar.** Fecha, hash y commit son actos del investigador.

---

*Historia: v1 (2026-08-26) — redactada por el asistente de IA bajo supervisión de Maximiliano Winter, a partir de la verificación de herencia del mismo día.*

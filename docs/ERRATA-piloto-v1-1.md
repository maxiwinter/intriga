# Errata del informe del piloto §10.1 — Protocolo v1.1

**Fecha:** 2026-08-26. **Documento afectado:** `docs/piloto-seccion-10-1-informe-final.md`, que **no se modifica** con esta errata. El informe histórico conserva su texto y su propia sección "Erratas de trazabilidad"; este archivo registra la corrección que aquella sección todavía no incluye, para que ninguna cifra quede corregida en silencio.

**Origen:** regla de trazabilidad de la Enmienda 6(a) — todo número publicado debe provenir de un script versionado.

---

## Errata 5 — Costo de Nivel A de la regla de Lorenz

> **«≈ 1.400 bits»  →  1288 bits**

**Dónde aparece el valor viejo.** En el informe final del piloto, sección "Las dos lecciones que van más allá de la validación": *«la **regla** de Lorenz cuesta ~1.400 bits fijos (nivel A)»*.

**Valor correcto y su composición**, trazado a `results/lorenz-checkpoints-salida.txt` (generado por `src/lorenz_checkpoints.py`):

| Componente | Bits |
|---|---|
| Código fuente comprimido (gzip del fuente declarado en `piloto_10_1.py`) | 1096 |
| Parámetros (3 × 64) | 192 |
| **Total Nivel A** | **1288** |

**Origen del error.** `src/verificacion_piso_y_eta.py` cablea la constante `code_bits = 1252` con el comentario "gzip del fuente declarado (piloto)". Esa constante es obsoleta: el gzip del fuente efectivamente declarado en `piloto_10_1.py` mide **1096 bits**, verificable también en la salida archivada del codificador ingenuo, donde C(n = 1000) = 1360 = 1096 + 192 + 72. Con 1252 el total de Nivel A daba 1252 + 192 = 1444 ≈ «1.400». La constante fue identificada y corregida bajo la Enmienda 6; el script histórico **no se modificó**, y conserva su salida archivada como registro de la corrida original.

**Alcance del cambio.** Afecta únicamente la cifra del costo de Nivel A citada en prosa. **No afecta** ρ_oracle = 0.0053 (Lorenz, 20 000 pasos), que `src/lorenz_checkpoints.py` reproduce exactamente con el valor trazado de 1096 bits y k = ⌈20000/2655⌉ = 8 checkpoints; C = 1096 + 192 + 156 × 8 = 2536 bits sobre L₀ = 480 000. Tampoco afecta η_ε, que es una diferencia entre resoluciones y en la cual la constante se cancela.

**Deuda asociada (Enmienda 6a, §17 del protocolo consolidado).** Los subtotales por nivel —1288 bits de Nivel A y 156·⌈n/h(p,ε)⌉ bits de Nivel B— son hoy **sumas de cantidades que el script imprime**, no cantidades que el script imprima. Antes de que una tabla final los publique, `src/lorenz_checkpoints.py` debe emitir directamente el subtotal de Nivel A, el de Nivel B y el total. Hasta entonces se citan con esta advertencia y no se derivan a mano en ninguna tabla nueva.

---

## Errata 7 — Cargo de selección log₂3: declarado pero no incorporado a los totales históricos

**Detectada:** auditoría final, 2026-08-26. **Naturaleza:** trazabilidad contable. **Ninguna cifra experimental cambia.**

**Convención declarada anteriormente.** El informe del piloto y la metodología asociada declaran un cargo de selección de **log₂3 ≈ 1.585 bits** por elegir el mejor de los tres compresores genéricos dentro de su metaclase, y afirman que ese cargo está "incluido en ρ_MDL".

**Evidencia trazada.** El total histórico de la fila de Lorenz (20 000 pasos, codificador con checkpoints), reproducido por `src/lorenz_checkpoints.py`, es

> 1096 (fuente comprimida) + 192 (parámetros) + 156 × 8 = 1248 (checkpoints) = **2536 bits**

Esa suma **no contiene ningún sumando de selección**. Los 1.585 bits declarados **no estaban incluidos** en el total numérico.

**Nueva convención.** Identificador uniforme prefix-free de primer nivel sobre la familia enumerada {M₀ literal, zlib, bz2, lzma, generativo}: k = 5 → **⌈log₂ 5⌉ = 3 bits**, iguales para los cinco miembros, M₀ incluido (`protocol/definicion-L-M0.md`).

**Total recomputado.**

> 3 (identificador) + 1096 + 192 + 1248 = **2539 bits**

**Alcance.**
1. Las cifras de contabilidad completa (ρ_full, g_total) **ya incorporan** los 3 bits: la recomputación de `src/contabilidad_completa.py` y su verificación en `src/contabilidad_completa_v2.py` los suman explícitamente en el numerador de todo modelo y en el baseline L₀_full.
2. Los **valores históricos se conservan sin reinterpretación**: 2536 bits sigue siendo el total histórico trazado, y ρ_bare sigue publicándose bajo su propio nombre junto a ρ_full, con δ explícito.
3. **Ninguna cifra publicada cambia a cuatro decimales**: el mayor desplazamiento entre ρ_bare y ρ_full es 2.9 × 10⁻⁵.
4. El identificador de 3 bits **no debe presentarse como reetiquetado de 1.585 bits ya pagados**, porque numéricamente no lo estaban. Reemplaza una convención *declarada*, no una *cobrada*.

**Formulación fijada para citar:** *«Earlier reports stated a log₂3 selection charge for the generic-compressor meta-class, but the traced numerical totals did not include that charge. The unified 3-bit first-level identifier now replaces that stated convention and is explicitly included in all recomputed full-accounting results.»*

## Errata 8 — Expresión algebraica de g_total − g_pred

**Detectada:** auditoría final, 2026-08-26. **Naturaleza:** algebraica e interpretativa. **Ninguna cifra publicada cambia.**

Con A = L_U(T_train), B = L_U(M₀), G = L_U(D_test,ε | T_train) y H = L_U(D_test,ε | M₀):

> **g_total − g_pred = (A − B·g_pred)/(B + H) = (A·H − B·G)/[H·(B + H)]**

El preprint v0.5 usaba **A/(B + H)** y afirmaba que la diferencia valía *«811/92 163 en los tres controles»*. Esa expresión **solo es válida cuando g_pred = 0**, y la afirmación es **falsa para el control de ruido**:

| Control | g_pred | diferencia correcta | valor | redondea a |
|---|---|---|---|---|
| Regla 110 | 0 exacto | A/(B+H) = 811/92 163 | 0.0087996 | 0.0088 |
| Regla 30 | 0 exacto | A/(B+H) = 811/92 163 | 0.0087996 | 0.0088 |
| Ruido PCG64 (semilla 2026) | ≈ 1 | (A − B·g_pred)/(B+H) ≈ 808/92 163 | 0.0087671 | 0.0088 |

**Las tres redondean a 0.0088, de modo que la tabla publicada a cuatro decimales no cambia.** El error era de explicación, no de medición. Verificado por `src/contabilidad_completa_v2.py`, que imprime ambos lados de la identidad sin redondeo interno y los compara por `assert` (tolerancia 10⁻¹²). Corregido en `preprint-v0-6.md` §4.5 y §6.2, y en §13.5 y §15 del protocolo consolidado.

---

## Erratas ya documentadas en el informe (referencia, sin duplicar cifras)

Las cuatro erratas siguientes están registradas en la sección "Erratas de trazabilidad (verificación de herencia)" del propio informe y **no se repiten aquí**:

1. **Errata 1** — ρ_oracle de Lorenz con checkpoints: valor confirmado por script, no corregido.
2. **Errata 2** — «regla espuria 166» y su porcentaje de error: sustituidos por la formulación invariante del control negativo (Enmienda 6b).
3. **Errata 3** — pendiente en precisión extendida: ahora impresa por script como promedio de tramos, rango y ajuste global. La discrepancia con la predicción **sigue sin causa asignada** y se reporta sin corregir.
4. **Errata 4** — ρ_MDL del barrido de resolución de la Adenda, recalculados con la constante trazada; η_ε sin cambio.

## Erratas posteriores registradas fuera del informe

5. **Esta errata** — costo de Nivel A: ≈ 1400 → 1288 bits.
6. **Nomenclatura de las métricas fuera de muestra.** Los valores 0.0088, 1.009 y 1.0088 que el informe llama `g` son, en la nomenclatura fijada por el protocolo consolidado (§13.5), **g_total^bare** = [L(T) + L(D_test|T)] / L(D_test|M₀), una razón asimétrica. **No son** la g_total simétrica ni g_pred. Esto no cambia ningún número del informe ni ninguna conclusión: la generalización sigue discriminando exactamente igual. Se registra para que ninguna cita posterior los reinterprete. Las g_pred correspondientes (0.0000 para Reglas 110 y 30; 1.0000 para el ruido con semilla) las imprime `src/g_metricas_oos.py` en `results/g-metricas-oos-salida.txt`. La g_total simétrica **no estaba calculada** al redactarse esta entrada; **lo está desde el 2026-08-26** (ver Actualizaciones, abajo).

7. **Cargo log₂3 declarado pero no incorporado** a los totales históricos (detalle arriba).
8. **Expresión algebraica de g_total − g_pred** (detalle arriba).

## Actualizaciones de estado (no son erratas nuevas)

Dos advertencias de las entradas 5 y 6 quedaron superadas y se dejan visibles en lugar de reescribirse:

- La **deuda asociada a la Errata 5** —que los subtotales de Nivel A y Nivel B fueran sumas hechas a mano— **quedó cerrada el 2026-08-26**: `src/contabilidad_completa.py` los imprime directamente (identificador 3, Nivel A 1288, Nivel B 156·⌈n/h⌉, total).
- La advertencia de la **entrada 6** de que la g_total simétrica no estaba calculada **quedó superada el 2026-08-26**, al definirse L_U(M₀) (`protocol/definicion-L-M0.md`): g_total = 0.0088 / 0.0088 / 1.0088. Los valores históricos siguen publicándose como g_total^bare, sin reinterpretación.

---

*Historia: v1 (2026-08-26) — Erratas 5 y 6. — v2 (2026-08-26, auditoría final) — Erratas 7 (cargo log₂3 declarado pero no incorporado a los totales históricos) y 8 (expresión algebraica de g_total − g_pred). Redactada por el asistente de IA bajo supervisión de Maximiliano Winter. **El informe del piloto no fue modificado en ninguna de las dos rondas.***

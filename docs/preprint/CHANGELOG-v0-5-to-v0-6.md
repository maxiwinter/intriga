# Changelog del preprint — v0.5 → v0.6

**Fecha:** 2026-08-26. **Archivo nuevo:** `preprint-v0-6.md`. **Conservados sin modificar:** `preprint-v0-5.md`, `preprint-v0-4.md`, `preprint-v0-3.md`, `preprint-v0-1.md` (v0.2) y todos sus changelogs e informes de validación.

**Naturaleza de esta revisión.** Auditoría final, **estrictamente acotada a dos correcciones**. Ninguna otra reescritura estructural. **Ninguna cifra experimental cambió**: ambos defectos eran de álgebra e historia contable, no de medición, y las tablas a cuatro decimales quedan exactamente como estaban publicadas. Ningún dataset empírico fue abierto. La discrepancia de pendiente de Lorenz no fue investigada.

---

## Tabla de cambios

| # | Sección / archivo | Problema | Corrección | ¿Fórmula? | ¿Código? | ¿Valores? | ¿Acción humana? |
|---|---|---|---|---|---|---|---|
| **F1** | preprint §4.5; consolidado §13.5 | **Identidad algebraica incorrecta.** La diferencia se escribía como `A/(B+H)`, que **solo vale cuando g_pred = 0**. Con denominadores distintos esa expresión sobreestima la diferencia en `B·g_pred/(B+H)`. | Identidad exacta, con abreviaturas declaradas `A = L_U(T_train)`, `B = L_U(M₀)`, `G = L_U(D_test,ε\|T_train)`, `H = L_U(D_test,ε\|M₀)`: **`g_total − g_pred = (A − B·g_pred)/(B + H) = (A·H − B·G)/[H·(B + H)]`**. Tres reglas de lectura explícitas: (i) no hay desigualdad general entre las dos razones; (ii) el **signo** es el de `A − B·g_pred`, sin dirección universal; (iii) la reducción a `A/(B+H)` vale **solo** en el caso especial `g_pred = 0`. | **SÍ** | No | **No** | No |
| **F2** | preprint §5.5; consolidado §13.5 y §15 | La convergencia se enunciaba sin condiciones suficientes explícitas. | **`g_total − g_pred → 0`** enunciado bajo condiciones nombradas: **A y B fijos y g_pred acotado**, de modo que al crecer el bloque de test `H → ∞` y los costos fijos se amortizan. Se mantiene retirado "from above" y **no se afirma ninguna dirección de convergencia**. | **SÍ** | No | **No** | No |
| **F3** | preprint §6.2; consolidado §15; `ERRATA` 8 | **Afirmación falsa:** «the difference is exactly 811/92 163 in all three controls». Es correcta para las Reglas 110 y 30, donde `g_pred = 0` exacto, y **falsa para el ruido**, donde `g_pred ≈ 1`. | Retirada y sustituida por una tabla con el valor correcto de cada control: **R110 y R30 → `A/(B+H)` = 811/92 163 = 0.0087996**; **ruido → `(A − B·g_pred)/(B+H)` ≈ 808/92 163 = 0.0087671**. Se explicita que la reducción vale para los autómatas **porque su residuo predictivo es exactamente cero**, no como regla general. | No | No | **No: las tres redondean a 0.0088** y la tabla publicada a cuatro decimales no se toca. | No |
| **F4** | `src/contabilidad_completa_v2.py` y `results/contabilidad-completa-v2-salida.txt` (nuevos) | La identidad no estaba verificada por script. | Script **nuevo** (el v1 y su salida **no se modifican**, convención un-archivo-por-versión). Imprime `A`, `B`, `H`, `G`, `g_pred`, `g_total`, `delta_g` y **ambos lados de la identidad** (`formula1` y `formula2`), **sin redondeo interno**, y los compara por **`assert`** con tolerancia 10⁻¹². Resultado: R110 y R30 → 0.008799627; ruido → 0.008767076 con `g_pred = 0.999999978`; diferencia máxima entre lados 1.2 × 10⁻¹⁶. Imprime además la lectura fila por fila y la comprobación de que las tres redondean a 0.0088. | No | **SÍ** (script nuevo) | **No.** Verificado: la tabla principal, la verificación ρ_full ≤ 1, la predicción de δ y los niveles A/B son **idénticos** entre v1 y v2 (`diff` de las 60 primeras líneas: sin diferencias). | No |
| **F5** | `protocol/definicion-L-M0.md`; preprint §4.3; `ERRATA` 7 | **Historia contable incorrecta.** Se decía que el identificador de 3 bits "subsume y reemplaza" el cargo de log₂3 ≈ 1.585 bits, lo que implica que ese cargo ya estaba pagado. **La trazabilidad muestra que no lo estaba:** el total histórico de Lorenz es 1096 + 192 + 1248 = **2536 bits**, sin ningún sumando de selección, frente a 3 + 1096 + 192 + 1248 = **2539 bits** ahora. | Reformulado con la fórmula fijada: *«Earlier reports stated a log₂3 selection charge for the generic-compressor meta-class, but the traced numerical totals did not include that charge. The unified 3-bit first-level identifier now replaces that stated convention and is explicitly included in all recomputed full-accounting results.»* Se dice expresamente que **no** es un reetiquetado de bits ya pagados. El script v2 imprime los dos totales y la diferencia de 3 bits. | No | No | **No** (2536 y 2539 son totales ya trazados; ninguno cambia) | No |
| **F6** | `docs/ERRATA-piloto-v1-1.md` | Faltaba registro formal de ambos hallazgos. | **Errata 7** — cargo log₂3 declarado pero no incorporado a los totales históricos: convención declarada, evidencia trazada (2536), nueva convención (k = 5 → 3 bits), total recomputado (2539), alcance en cuatro puntos y formulación fijada para citar. **Errata 8** — expresión algebraica de g_total − g_pred, con la tabla de los tres controles y la nota de que ninguna cifra publicada cambia. Añadidas al índice de erratas. | No | No | **No** | **SÍ** — decidir si las erratas se incorporan al informe del piloto o siguen como adjunto. |
| **F7** | preprint §4.3; `definicion-L-M0.md` §3; (sustituye la frase de `VALIDATION-REPORT-v0-5.md`) | La frase «L_U(M₀) = 3 bits **no es una suposición**: es ⌈log₂ 5⌉ sobre una familia enumerada» podía leerse como si 3 bits fuera un valor canónico u ontológico. | Reformulado: la aritmética ⌈log₂ 5⌉ = 3 es exacta y **no se ajustó a los resultados**, pero **elegir una familia de cinco miembros** y **elegir un código uniforme prefix-free** son **convenciones de la pila U_ref, declaradas de antemano**. Bajo otra familia o un código no uniforme, L_U(M₀) toma otro valor y la contabilidad debe rehacerse. **No se presenta como cantidad canónica.** Añadido también al §7 del consolidado. Nota: `VALIDATION-REPORT-v0-5.md` conserva la frase original **por ser versión anterior intacta**; queda superada por este informe y por el de v0.6. | No | No | **No** | No |
| **F8** | preprint §7.5 bis; historia de versiones | Las dos correcciones debían quedar visibles como limitaciones corregidas, no borradas. | Párrafo nuevo **«Two defects of the previous draft, corrected here»** en §7.5 bis, describiendo ambos defectos y aclarando que el error fue algebraico e interpretativo, no numérico. Historia de versiones ampliada. **§7 conserva sus 9 subsecciones; ninguna limitación ni errata fue eliminada.** | No | No | **No** | No |

---

## Secciones y líneas modificadas del protocolo consolidado

El consolidado **todavía no está congelado**, por lo que se actualizó; los puntos exactos son:

1. **§7 (Modelo nulo)** — añadida la advertencia de que L_U(M₀) = 3 bits es consecuencia de convenciones pre-declaradas y no un valor canónico; añadida la referencia a `contabilidad_completa_v2.py`.
2. **§13.5 (Generalización fuera de muestra)** — sustituido el párrafo «No se asume ninguna desigualdad» por el bloque **Identidad exacta de la diferencia** (abreviaturas A/B/G/H, las dos formas de la identidad, las tres reglas de lectura) más **Convergencia, con sus condiciones explícitas**.
3. **§15 (Criterio primario de éxito)** — corregido el párrafo de convergencia: condiciones nombradas y retirada de la afirmación de que la diferencia vale lo mismo en los tres controles, con los dos valores correctos.
4. **Historia al pie** — nueva entrada de tercera incorporación pre-congelamiento.

**El bloque STATUS no se tocó: sigue `Prepared for freezing — NOT YET FROZEN OR PREREGISTERED`.** Sin hash, sin tag de Git, sin depósito OSF.

## Lo que esta ronda NO hizo

- **No investigó la discrepancia de pendiente de Lorenz** (64.2 / 67.6 contra 76.5): excluido por la consigna; sigue sin causa asignada en §7.1.
- **No abrió ningún dataset empírico** ni tocó espectros.
- **No modificó ninguna versión anterior** del preprint ni sus changelogs e informes.
- **No modificó** `src/contabilidad_completa.py` ni `results/contabilidad-completa-salida.txt` ni ninguna otra salida previa.
- **No congeló nada** ni calculó hash, tag u OSF.
- **No fortaleció ninguna claim de originalidad** ni desmarcó ninguna referencia `[VERIFY]`.

## Acciones humanas tras v0.6

1. **Revisión final y decisión de congelamiento** del protocolo consolidado (PDF + SHA-256 + tag + OSF).
2. Instanciar familia de primer nivel, árbol de códigos y primitivas de cada dominio empírico.
3. Dos pilas U_ref verdaderas; amortización de bibliotecas; precisión identificable en familias no regulares.
4. Verificar las 33 referencias `[VERIFY]`.
5. Revisión humana experta (MDL/AIT + dominio físico).
6. Decidir si las erratas se incorporan al informe del piloto.
7. Afiliación, ORCID, licencia.
8. Investigar o reportar la discrepancia de pendiente de Lorenz.
9. Primera medición empírica (§11.1, Tracks A y B). **No iniciada.**

---

*Historia: v1 (2026-08-26) — redactado por el asistente de IA bajo supervisión de Maximiliano Winter.*

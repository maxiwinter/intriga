# Informe de validación — `preprint-v0-6.md` (auditoría final)

**Fecha:** 2026-08-26. **Objetos validados:** `docs/preprint/preprint-v0-6.md` (14.428 palabras), `protocol/protocolo-v1-1-consolidado.md`, `protocol/definicion-L-M0.md`, `docs/ERRATA-piloto-v1-1.md`, `src/contabilidad_completa_v2.py` y su salida.

**Alcance:** dos correcciones y nada más. **Ninguna cifra experimental cambió.**

---

## Checklist solicitada

### ✅ g_total − g_pred usa la identidad exacta
§4.5 del preprint y §13.5 del consolidado declaran las abreviaturas `A = L_U(T_train)`, `B = L_U(M₀)`, `G = L_U(D_test,ε|T_train)`, `H = L_U(D_test,ε|M₀)` y fijan

> **g_total − g_pred = (A − B·g_pred)/(B + H) = (A·H − B·G)/[H·(B + H)]**

con las tres reglas de lectura: no hay desigualdad general; el signo es el de `A − B·g_pred`; la reducción a `A/(B+H)` vale solo con `g_pred = 0`. Verificada por `assert` en `src/contabilidad_completa_v2.py` (tolerancia 10⁻¹², sin redondeo interno): ambas formas coinciden con la diferencia directa, con desviación máxima **1.2 × 10⁻¹⁶**.

### ✅ Para g_pred = 0 se reduce a A/(B+H)
Reglas 110 y 30 tienen residuo predictivo **exactamente cero** (`G = 0.0`, `g_pred = 0.000000000`), de modo que la diferencia es `A/(B+H) = 811/92 163 = **0.008799627**`. El script lo imprime como caso especial y el preprint lo dice explícitamente: la reducción vale *porque* el residuo es cero, **no** como regla general.

### ✅ Para el ruido se usa (A − B·g_pred)/(B+H), no A/(B+H)
Control PCG64 semilla 2026: `g_pred = 0.999999978`, numerador `A − B·g_pred = 808.000000`, diferencia **0.008767076**. El script imprime además que con `g_pred = 1` exacto daría `(A − B)/(B + H) = 808/92 163 = 0.0087671`. La tabla de §6.2 del preprint distingue las tres filas.

### ✅ La tabla a cuatro decimales no cambia
`0.008799627 → 0.0088` y `0.008767076 → 0.0088`. El script imprime la comprobación. Las columnas de §6.2 (`g_pred` 0.0000 / 0.0000 / 1.0000; `g_total^bare` 0.0088 / 0.0088 / 1.0088; `g_total` 0.0088 / 0.0088 / 1.0088) quedan **idénticas**.

### ✅ Ningún resultado experimental cambió
`diff` de las 60 primeras líneas de `results/contabilidad-completa-salida.txt` contra `results/contabilidad-completa-v2-salida.txt`: **sin diferencias**. Se conservan sin alteración: ρ_full = 0.005290 / 0.010732 / 0.010732 / 0.001812 / 1.000000 / 0.994453 / 0.926134; g_pred = 0 / 0 / ≈1; g_total a cuatro decimales = 0.0088 / 0.0088 / 1.0088; Nivel A = 1288; Nivel B = 1248; total 2539; total histórico 2536. **Ningún script ni salida previos fueron modificados.**

### ✅ No queda "exactly 811/92163 in all three controls"
Retirada. Las dos ocurrencias de la frase «in all three controls» en `preprint-v0-6.md` están en §7.5 bis y en la historia de versiones, ambas **citando la afirmación retirada para documentarla**. Ninguna la sostiene.

### ✅ No queda "necessarily g_total > g_pred"
**0 ocurrencias** de "necessarily" en todo el repositorio, versiones anteriores incluidas.

### ✅ No queda "from above"
Las dos ocurrencias en `preprint-v0-6.md` son **negaciones explícitas**: «We do **not** claim the limit is approached from above, or from any particular side» (§4.5) y el registro del cambio en la historia. El consolidado dice lo mismo en §13.5 y §15. **0 ocurrencias afirmativas.**

### ✅ La convergencia se formula con condiciones explícitas
Preprint §4.5 y §5.5, consolidado §13.5 y §15: `g_total − g_pred → 0` **si A y B permanecen fijos y g_pred permanece acotado**, de modo que al crecer el bloque de test `H → ∞` y los costos fijos se amortizan. Sin dirección de convergencia afirmada.

### ✅ log₂3 queda registrado como cargo declarado pero no pagado en los totales históricos
**Errata 7** en `docs/ERRATA-piloto-v1-1.md`, con la evidencia trazada: total histórico de Lorenz = 1096 + 192 + 1248 = **2536 bits**, sin ningún sumando de selección. `protocol/definicion-L-M0.md` reemplazó su nota anterior por la formulación fijada, y dice expresamente que el identificador **no** es un reetiquetado de 1.585 bits ya pagados. El script v2 imprime ambos totales y la diferencia de 3 bits.
**Corrección adicional detectada durante esta ronda:** §6.1 del preprint todavía afirmaba, describiendo el setup, que la selección «pays log₂ 3 ≈ 1.6 bits, included in ρ_MDL» — exactamente la afirmación que la Errata 7 refuta. Reescrita: el piloto **declaró** ese cargo, los totales trazados **no lo incluían**, y bajo la contabilidad presente el identificador de 3 bits **sí** entra en toda cifra recomputada.

### ✅ El identificador nuevo de 3 bits sí está incorporado en la recomputación full
Total full de Lorenz = 3 + 1096 + 192 + 1248 = **2539 bits**, impreso por el script. Los 3 bits entran en el numerador de todo modelo y en el baseline `L₀_full = 3 + L₀` de las siete filas.

### ✅ L_U(M₀) = 3 se presenta como consecuencia de una convención pre-declarada, no como valor canónico
Preprint §4.3: «not fitted to the results, and **not a canonical property of null models**»; ⌈log₂ 5⌉ = 3 es aritmética exacta, pero *qué* cinco miembros forman la familia y *que* el código sea uniforme y prefix-free son **convenciones de la pila declaradas de antemano**; bajo otra familia o código no uniforme el valor sería otro y la contabilidad debe rehacerse. Réplicas en `definicion-L-M0.md` §3 y en §7 del consolidado.
*Nota:* `VALIDATION-REPORT-v0-5.md` conserva la frase «no es una suposición» **por ser versión anterior intacta**; queda superada por este informe.

### ✅ Errata 7 creada
Con los seis elementos pedidos: convención declarada (log₂3 ≈ 1.585 bits), evidencia trazada (2536 = 1096 + 192 + 1248), constatación de que no estaba incluida, nueva convención (k = 5 → 3 bits), total recomputado (2539) y alcance en cuatro puntos. Se agregó además **Errata 8** para el defecto algebraico, y dos «Actualizaciones de estado» que dejan visibles —sin reescribirlas— dos advertencias de las Erratas 5 y 6 que quedaron superadas.

### ✅ Ningún dataset empírico fue abierto
Ninguno. El único script ejecutado (`contabilidad_completa_v2.py`) genera todo con las semillas del piloto más `os.urandom` para el control negativo histórico. §8 sigue siendo diseño: sin mediciones.

### ✅ Ninguna referencia [VERIFY] fue desmarcada
**33 en v0.5, 33 en v0.6.**

### ✅ Ninguna claim de originalidad fue fortalecida
Mapa de §3.6 sin cambios: 7 "not original", 1 "close antecedent", 2 "possible novelty" (η_ε "unconfirmed"), 1 "most defensible contribution". La reivindicación central conserva su formulación con "to the best of our knowledge". Ambas correcciones de esta ronda **debilitan** afirmaciones previas.

### ✅ Versiones anteriores intactas
Verificado por `sha256sum`: `preprint-v0-5.md`, `preprint-v0-4.md`, `preprint-v0-3.md`, `preprint-v0-1.md`, `CHANGELOG-v0-2-to-v0-3`, `CHANGELOG-v0-3-to-v0-4`, `CHANGELOG-v0-4-to-v0-5`, `VALIDATION-REPORT-v0-3/4/5`, los dos `.docx`, `changelog-v1-0-a-v1-1.md`, `enmienda-6.md`, todos los scripts previos y todas las salidas previas — **sin cambios**. Modificados solo los permitidos y documentados: el consolidado (§7, §13.5, §15, historia), `definicion-L-M0.md`, `ERRATA-piloto-v1-1.md` y `PENDIENTES.md`.

---

## Búsquedas globales

| Término | Estado en archivos vigentes |
|---|---|
| `811/92163`, `811/92 163` | Solo donde corresponde: la fila de las Reglas 110/30, donde `g_pred = 0`. Nunca atribuido a los tres controles. |
| `exactly 811` | 0 en el preprint; solo en el changelog, citando la frase retirada. |
| `g_total - g_pred` / `g_tot-g_pred` | Script v2 y su salida (encabezados de columna). |
| `necessarily` | **0 en todo el repositorio.** |
| `from above` | Solo negaciones explícitas y registro del cambio. |
| `log₂3` / `log₂ 3` | Errata 7, `definicion-L-M0.md`, §4.3 y §6.1 del preprint — siempre como convención **declarada y no incorporada**. El informe histórico del piloto conserva la suya, intacto y cubierto por la Errata 7. |
| `1.6 bits` | En el preprint solo dentro de la corrección de §6.1. El informe histórico conserva la suya. |
| `not an assumption` | **0.** |
| `canonical` / `canónic` | Solo en negaciones («not a canonical property», «no es una cantidad canónica ni ontológica») y en usos ajenos previos (`la-intriga-v5.md`, §9 del consolidado sobre representación canónica de U). |
| `2536` / `2539` | Siempre como totales trazados: 2536 histórico sin identificador, 2539 full con identificador. |

---

## Veredicto

**17 ✅ · 0 ⚠️ · 0 ❌.**

Las dos correcciones quedaron cerradas y trazadas. **Ningún resultado numérico cambió**: ambos defectos eran de álgebra y de historia contable, y las tablas publicadas a cuatro decimales se sostienen tal como estaban. Se detectó y corrigió, dentro del alcance de la segunda corrección, una afirmación residual en §6.1 del preprint que sostenía el cargo log₂3 como incluido.

**Sigue abierto y sin tocar:** dos pilas U_ref verdaderas, amortización de bibliotecas, precisión identificable en familias no regulares, instanciación por dominio, 33 referencias `[VERIFY]`, revisión humana experta, afiliación/ORCID/licencia, **la discrepancia de pendiente de Lorenz** (no investigada por instrucción expresa), el congelamiento y la primera medición empírica.

El protocolo consolidado **no fue congelado**: sin hash definitivo, sin tag de Git, sin depósito OSF.

---

*Historia: v1 (2026-08-26) — redactado por el asistente de IA bajo supervisión de Maximiliano Winter.*

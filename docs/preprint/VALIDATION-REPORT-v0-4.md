# Informe de validación — `preprint-v0-4.md` y `protocol/protocolo-v1-1-consolidado.md`

**Fecha:** 2026-08-26. **Objetos validados:** `docs/preprint/preprint-v0-4.md` (12.905 palabras) y `protocol/protocolo-v1-1-consolidado.md`. **Contraste:** `results/*.txt`, `src/*.py`, documentos fuente de `/protocol`, informe del piloto y sus erratas.

**Estados:** ✅ cumplido y verificado — ⚠️ cumplido **con reserva declarada dentro del propio documento** — ❌ incumplido. No se usa ✅ para nada que dependa de una acción humana pendiente.

---

## Checklist solicitada

### ✅ Track A/B sólo significa benchmark conocido / blind discovery
En v0.4, "Track A" y "Track B" aparecen **exclusivamente** en §8 (diseño empírico) y en una advertencia de §6.3 cuyo propósito es negar la asociación con Lorenz. §8.2 los define como *known-physics benchmark* (la familia **sí** puede contener Rydberg y modelos físicos conocidos; condición crítica de proveniencia; reporta ρ_MDL, η_ε, g_pred, g_total, escalamiento con n, robustez U_ref y surrogates) y *blind discovery* (sin Rydberg, defecto cuántico, estructura de niveles ni tablas equivalentes como primitivas; regresión simbólica y familias genéricas admitidas; toda estructura descubierta paga su longitud). Enunciado en mayúsculas de **EXISTENCE OF COMPRESSIBLE STRUCTURE ≠ ABILITY OF A MODEL FAMILY TO DISCOVER IT**, anclado en Regla 30 / PCG64 (r_generic ≈ 1.0009 y 1.0005 con generadores de pocos cientos de bits) y con la lectura obligatoria: **un ρ_MDL alto en Track B no demuestra incompresibilidad**. Replicado en el protocolo consolidado §11.1.

### ✅ Lorenz usa Level A/B, nunca Track A/B
La tabla de §6.3 se titula **"Level A / Level B decomposition of the Lorenz description"**, con encabezados "Level A — the rule" y "Level B — this trajectory", y lleva una advertencia explícita de que la descomposición pertenece a §4.6 y **no tiene relación** con los tracks de §8. Ninguna aparición de "Track" dentro de la tabla ni de su prosa. La limitación §7.8 de v0.3 ("lectura tomada, no verificada") queda **retirada por resuelta**, según la instrucción; §7 pasa de 10 a 9 subsecciones y **ninguna otra limitación fue eliminada**.

### ✅ g_pred está correctamente definido
§4.5: `g_pred(T) = L_U(D_test,ε | T_train) / L_U(D_test,ε | M₀)`, con la pregunta explícita *"once the trained model is known, how well does it encode unseen data?"* y las cuatro lecturas (≪ 1, = 0, ≈ 1, **> 1 = predice peor que el baseline**). Idéntico en el protocolo consolidado §13.5.

### ⚠️ g_total tiene baseline completo
**Definido simétricamente:** `g_total(T) = [L_U(T_train) + L_U(D_test,ε|T_train)] / [L_U(M₀) + L_U(D_test,ε|M₀)]`, con la pregunta *"does the model earn its own description cost on the test block?"* y la lectura **g_total > 1 = modelo + test cuesta más que modelo nulo + test**. **Reserva, declarada en §4.5, §6.2 y §7.5 bis:** g_total simétrica **no se calcula en ninguna parte del proyecto**, porque exige `L_U(M₀)`, que el protocolo aún no define. La columna correspondiente de la tabla de §6.2 dice literalmente *"requires L_U(M₀) — **not computed**"*. **No se inventó ningún valor.**

### ✅ No queda "necessarily g_total > g_pred"
**0 ocurrencias** de "necessarily" y "Necessarily" en v0.4. §4.5 dice expresamente: *"The two ratios have different denominators, so g_total > g_pred does not follow and is not asserted anywhere in this paper."* El protocolo consolidado §13.5 repite la advertencia. Se conserva lo que sí es cierto: un modelo puede tener g_pred ≪ 1 y g_total > 1 con bloques de test chicos.

### ✅ Valores históricos de g no fueron reinterpretados silenciosamente
Se **inspeccionaron los scripts** antes de tocar nada: `piloto_10_1.py` calcula `g=(ca_code+8+Ltest)/tot`, es decir modelo en el numerador y residuo desnudo en el denominador. Esa cantidad se nombra **g_total^bare** (8 ocurrencias en v0.4) y bajo ese nombre se reportan 0.0088, 1.009 y 1.0088. La tabla de §6.2 tiene columnas separadas para g_pred, g_total^bare y g_total, y un párrafo que dice que los valores históricos **"are not reinterpreted"**. `docs/ERRATA-piloto-v1-1.md` registra la nomenclatura como Errata 6.
**Métrica nueva efectivamente calculada:** `src/g_metricas_oos.py` → `results/g-metricas-oos-salida.txt` imprime g_pred = **0.0000** (Reglas 110 y 30) y **1.0000** (ruido PCG64 semilla 2026), junto a g_total^bare = 0.0088 / 0.0088 / 1.0088, reproduciendo los históricos con las semillas del piloto. **Ningún script ni salida previos fueron modificados.**

### ⚠️ ρ usa baseline completo
**Definido** en §4.3 y en el protocolo §13.2: `ρ = C / L₀_full` con `L₀_full = L_U(M₀) + L_U(D_n,ε|M₀)`. **Reserva, declarada en §4.3, §7.5 bis y en el Anexo A del protocolo:** las cifras de §6 **siguen normalizadas por el residuo desnudo** y el draft lo dice expresamente ("The numbers in §6 do not yet use L₀^full, and this draft does not claim they do"). No se recalculó nada a mano.

### ✅ ρ ≤ 1 está formalmente garantizado
Como M₀ ∈ M, `C ≤ L_U(M₀) + L_U(D_ε|M₀) = L₀_full`, luego ρ ≤ 1 es consecuencia exacta, no aproximación. Corregido además el caso de igualdad: **"ρ = 1 when the null description is optimal, possibly tied with another model"** de igual costo total, en lugar de "exactly when M₀ wins". Idéntico en el protocolo §13.2.

### ✅ h(p, ε) está en el protocolo consolidado
§5.4 del protocolo consolidado lo define como horizonte **medido** y fija cinco reglas: (1) se mide, no se deriva — **no es p·ln2/λ** ni un "Lyapunov horizon" teórico, que solo sirve de referencia o predicción; (2) ambos argumentos se registran siempre, con la serie medida 3194/2655/2655/2655/2458; (3) se declara el piso aritmético o instrumental, y un h plano frente a cambios de resolución es firma de piso; (4) **N_checkpoints = ⌈n/h(p,ε)⌉** y cada checkpoint paga su costo; (5) **si h se optimiza en vez de fijarse, se paga el costo de seleccionarlo** dentro de la familia. §4.7 del preprint remite a esa sección.

### ✅ 2655 nunca se llama Lyapunov horizon
Las apariciones de 2655 en v0.4 y en el protocolo son como `h(52, 8 bits)` medido o como piso float64. Las tres ocurrencias de la expresión "Lyapunov horizon" en v0.4 son de signo contrario: §4.7 lo distingue de h, §7.5 bis registra que llamarlo así **era el defecto corregido**, y la historia de versiones documenta el reemplazo. El protocolo consolidado no lo usa como etiqueta en ningún lugar.

### ✅ El título no afirma preregistro consumado
Título de v0.4: **"A Metrological Framework for Measuring the Scale- and Resolution-Dependent Descriptive Compressibility of Empirical Regularities"** — **0 ocurrencias** de "Preregistered" en el título. Nota inicial: el protocolo **no** está congelado y **no** existe preregistro público; el cuerpo usa *preregistration-ready*, *designed for preregistration*, *to be preregistered*, nunca *publicly preregistered*, *frozen* ni *completed*; disponibilidad dice **"No preregistration record exists yet to cite"**. Sin hash, sin identificador de registro, sin fecha de depósito.

### ✅ El protocolo dice NOT YET FROZEN
`protocol/protocolo-v1-1-consolidado.md` abre con un bloque `STATUS` que dice **"Prepared for freezing — NOT YET FROZEN OR PREREGISTERED"** y aclara: sin hash definitivo, sin tag de Git, sin depósito OSF, nada citable como pre-registro público. Declara además que los documentos fuente **no fueron modificados y prevalecen** ante cualquier discrepancia de redacción hasta el congelamiento.

### ✅ El criterio de éxito distingue g_pred de g_total
§5.5 del preprint y §15 del protocolo: **ρ_MDL ≪ 1, η_ε ≪ 1, g_pred ≪ 1**, con g_total **reportada como condición de amortización descriptiva y no como umbral**, más la predicción de escalamiento **g_total → g_pred** desde arriba al crecer el bloque de test o n, y la interpretación del caso contrario (g_total plana o divergente = firma de ajuste, no de compresión). Incorporado también a los falsadores (§5.6 / protocolo §16).

### ✅ Errata 1400 → 1288 documentada
`docs/ERRATA-piloto-v1-1.md`, Errata 5: valor viejo citado, valor nuevo **1288 bits**, composición (1096 fuente comprimida + 192 parámetros), origen del error (constante obsoleta 1252 en `verificacion_piso_y_eta.py`, con la verificación cruzada C(n=1000) = 1360 = 1096+192+72), y alcance (**no** afecta ρ_oracle = 0.0053 ni η_ε). Las cuatro erratas previas se listan **por referencia, sin duplicar cifras**. **El informe histórico no fue modificado.**

### ✅ No se ejecutó ningún dataset empírico
No se abrió, descargó, leyó ni procesó ningún dataset empírico. No se consultó NIST ASD ni ninguna otra base. El único script ejecutado en esta ronda es `src/g_metricas_oos.py`, que genera sus datos sintéticos con las semillas del piloto (autómatas con `default_rng(42)`, ruido con `default_rng(2026)`). §8 es diseño y predicción: **no contiene ninguna medición**.

### ✅ Ninguna cifra fue inventada
Todas las cifras de §6 siguen trazando a `results/*.txt`. Las nuevas de esta ronda (g_pred = 0.0000 / 0.0000 / 1.0000) provienen de un script versionado con su salida archivada. Los subtotales 1288 y 1248 siguen siendo **sumas declaradas** de cantidades impresas, con la advertencia de que un script debe emitirlos antes de que una tabla final los publique. `L_U(M₀)` **no se inventó**, y por eso ni ρ ni g_total se recalcularon.

### ✅ Ninguna referencia [VERIFY] fue desmarcada
**33 en v0.3, 33 en v0.4.** Ningún dato bibliográfico dudoso fue completado; las dos referencias sin localizar (Leyva-Acosta et al. 2026; regresión simbólica + MDL en astrofísica 2026) y la de Wheeler siguen señaladas.

### ✅ Ninguna claim de originalidad fue fortalecida
La reivindicación central conserva su formulación literal con "to the best of our knowledge". El mapa de §3.6 conserva su distribución exacta: **7 "not original", 1 "close antecedent", 2 "possible novelty" (η_ε marcada "unconfirmed"), 1 "most defensible contribution"**. Permanece "This is not a new theory of the compressibility of the universe". El único enunciado nuevo con sabor a novedad — la distancia entre Track A y Track B para un dominio físico — está redactado con "to our knowledge, has not been measured".

### ✅ Las versiones anteriores quedaron intactas
`preprint-v0-3.md`, `preprint-v0-1.md` (v0.2), `CHANGELOG-v0-2-to-v0-3.md` y `VALIDATION-REPORT-v0-3.md` **sin modificar**. Los documentos fuente de `/protocol` (`.docx` de v1.0 y del marco v5.2, `changelog-v1-0-a-v1-1.md`, `enmienda-6.md`, `README.md`) **sin modificar**: verificado por `sha256sum`. Los scripts previos de `/src` y todas las salidas previas de `/results` **sin modificar**; los archivos nuevos son adiciones.

---

## Búsquedas globales obligatorias (todo el repositorio)

| Término | Resultado |
|---|---|
| `Track A` / `Track B` | En v0.4: solo §8 y la advertencia de §6.3. En el protocolo consolidado: solo §11.1 y la nota de §9. En v0.1/v0.3 y sus informes: **ocurrencias históricas, intactas por diseño**. En PENDIENTES: reescrito como cerrado. **Sin residuo problemático.** |
| `Level A` / `Level B` | v0.4 y el protocolo: descomposición de Lorenz y niveles descriptivos. Correcto. |
| `g_total` / `g_pred` | Definidos en v0.4 §4.5 y protocolo §13.5; usados en §5.5, §6.2, §8; impresos por `g_metricas_oos.py`. |
| `g =` | Solo en los scripts históricos (`piloto_10_1.py`, `ruido_oos_semilla.py`), en el nuevo script como variable local, en el informe histórico y en los documentos que lo citan. **0 en v0.4.** |
| `g(T)` | **0 en v0.4**; solo en `VALIDATION-REPORT-v0-3.md`, histórico. |
| `necessarily` | **0 en v0.4.** Única ocurrencia en el repo: `preprint-v0-3.md`, histórico. |
| `L(M0)` / `L_U(M₀)` | Definido como deuda en el protocolo §7, en el Anexo A, en v0.4 §4.3/§4.5/§7.5 bis, en PENDIENTES y en el script nuevo. **Nunca con un valor asignado.** |
| `L0_full` / `L₀^full` | Protocolo §7 y §13.2; v0.4 §4.3 (6 ocurrencias con notación markdown). |
| `2655` | Siempre como `h(p,ε)` medido o piso float64. Nunca como horizonte de Lyapunov. |
| `Lyapunov horizon` | 3 en v0.4, todas negando la identificación o documentando la corrección. 0 como etiqueta en el protocolo. |
| `Rydberg` | v0.4 §8.2 (permitido en Track A, prohibido como primitiva en Track B) y protocolo §11.1. Coherente. |
| `does not contain the answer` | **0 como afirmación**; 1 ocurrencia en la historia de versiones de v0.4 citando el texto retirado. |
| `not settled` | **0 en v0.4.** |
| `could not be` | 1 en v0.4, en la historia de versiones citando la frase retirada. |
| `1400` / `1.400` | En v0.4: 2 en el texto contrastando con 1288, 1 en la historia. En el informe histórico y en las notas del investigador: intactos por diseño, cubiertos por la Errata 5. **`1,400`: 0 ocurrencias.** |

---

## Veredicto

**16 ✅ · 3 ⚠️ · 0 ❌.**

Las tres reservas son **una sola deuda con tres caras**: `L_U(M₀)` no está definido, y de eso dependen (a) que los ρ publicados usen el baseline completo, (b) que la g_total simétrica pueda calcularse, y (c) por extensión, la tabla de §6.2. Está declarada dentro del preprint, dentro del protocolo consolidado (§7 y Anexo A) y en PENDIENTES, no solo aquí.

Ningún dataset empírico fue abierto. Ninguna cifra fue inventada. El protocolo **no fue congelado**: no se calculó hash definitivo, no se etiquetó Git, no se depositó nada.

---

*Historia: v1 (2026-08-26) — redactado por el asistente de IA bajo supervisión de Maximiliano Winter.*

# Informe de validación — `preprint-v0-5.md`, `protocol/definicion-L-M0.md` y el consolidado

**Fecha:** 2026-08-26. **Objetos validados:** `docs/preprint/preprint-v0-5.md` (13.632 palabras), `protocol/definicion-L-M0.md`, `protocol/protocolo-v1-1-consolidado.md`, `src/contabilidad_completa.py` y sus salidas.

**Estados:** ✅ cumplido y verificado — ⚠️ cumplido con reserva declarada — ❌ incumplido.

> **Las tres ⚠️ del informe v0.4 pasan a ✅.** Eran una sola deuda con tres caras: `L_U(M₀)` sin definir. Está definido, y la recomputación se hizo.

---

## Checklist heredada (v0.4) — resolución

### ✅ ρ usa baseline completo *(era ⚠️)*
`L_U(M₀)` definido en `protocol/definicion-L-M0.md` e incorporado por referencia en §7 del consolidado. Para el piloto: familia de primer nivel {M₀ literal, zlib, bz2, lzma, generativo}, k = 5, **L_id = 3 bits para todo miembro**, spec = 0 solo para primitivas declaradas de U_ref → **`L_U(M₀) = 3 bits`**, `L₀_full = 3 + L₀`. `src/contabilidad_completa.py` recomputa **las siete filas** con ese baseline y con cada modelo pagando su identificador (`results/contabilidad-completa-salida.txt`).

### ✅ ρ ≤ 1 formalmente garantizado **y verificado fila por fila** *(era ⚠️)*
Verificación impresa por el script: ρ_full = 0.005290 / 0.010732 / 0.010732 / 0.001812 / **1.000000** / 0.994453 / 0.926134 → **ρ_full ≤ 1 en las siete**. El caso de igualdad es exactamente el previsto: la fila de ruido, donde gana M₀. El texto de §4.3 corrige además la formulación del empate ("possibly tied with another model").

### ✅ g_total tiene baseline completo **y está calculada** *(era ⚠️)*
Con `L_U(T_train) = 811 bits` (3 identificador + 800 fuente + 8 regla), `L_U(M₀) = 3` y `L_U(D_test|M₀) = 92 160` → denominador simétrico 92 163. **g_total = 0.0088 (R110), 0.0088 (R30), 1.0088 (ruido PCG64)**. La columna histórica g_total^bare se conserva al lado.

---

## Checklist de esta ronda

### ✅ La definición es simétrica y M₀ no es gratis
`L_U(T) = L_U(id(T)|M) + L_U(spec(T)|U_ref) + L_U(θ_T)` se aplica **a todo modelo, M₀ incluido, sin tratamiento especial** (§2 y §2.1 de la definición). M₀ paga sus 3 bits de identificador. El script lo verifica por construcción: `L_modelo("M0 literal")` usa la misma función que los demás y `assert` que una primitiva declarada no pague spec.

### ✅ Identificador prefix-free pre-declarado y familia enumerada
Código uniforme `L_id = ⌈log₂ k⌉`; se admite código no uniforme si es prefix-free, pre-registrado, documentado y verificado contra Kraft. Familia del piloto enumerada en tabla con spec y θ de cada miembro. Se declara explícitamente que la pila del piloto **declara primitivas** la codificación literal y los tres compresores, que es la condición bajo la cual **spec(M₀) = 0 es defendible** — la definición dice "si y solo si", y también qué hacer cuando una pila no las declare.

### ✅ Árbol de códigos para familias jerárquicas pre-registrado
§4 de la definición: `L(familia) + L(submodelo|familia) + L(θ)`, con `Σ_j ⌈log₂ k_j⌉` por ruta; árbol pre-registrado antes de mirar D_test; **ningún nivel puede omitirse** (k_j = 1 → 0 bits es el único identificador gratuito legítimo); Kraft verificado si el código es no uniforme; y el costo de **búsqueda** contabilizado aparte del de **señalar** (§8 del protocolo).

### ✅ Predicción pre-declarada: confirmada, no ajustada
Predicción: |δ| bajo el redondeo (~3 bits sobre denominadores ≥ 6×10⁴). **Confirmada en las 7 filas.** δ: Lorenz +6.2×10⁻⁶; R110 +2.9×10⁻⁵; R30 +2.9×10⁻⁵; PRNG +1.1×10⁻⁵; ruido +0.0; surrogate R110 +1.6×10⁻⁷; surrogate Lorenz +4.6×10⁻⁷. El script imprime además la comprobación agregada *"rho a 4 decimales cambia en alguna fila: **False**"*. **Ninguna fila se movió visiblemente**, de modo que no hubo hallazgo que reportar bajo esa cláusula; nada fue ajustado para que encajara.

### ✅ Subtotales de Nivel A y Nivel B impresos por script
`results/contabilidad-completa-salida.txt`: h(52, 8 bits) = 2655 medido; k = 8; identificador 3; **Nivel A = 1288 bits** (spec 1096 + θ 192) marcado *[fijo, no crece con n]*; **Nivel B = 1248 bits** (156 × 8) marcado *[crece con el horizonte]*; total 2539; Nivel A = 0.5073 del total; más el escalamiento por n. **Cierra la deuda 4 de C ter** y el punto 7 del Anexo A. §6.3 del preprint ya no deriva nada a mano.

### ✅ Los valores históricos no fueron reinterpretados
g_total^bare conserva su nombre y su columna en §6.2, junto a la g_total simétrica. El preprint declara explícitamente que la coincidencia a cuatro decimales entre ambas **se debe a que 3 bits son despreciables frente a 92 160**, no a que sean la misma cantidad. ρ_bare aparece como columna propia en la salida del script, con δ explícito.

### ✅ "from above" retirado del criterio de escalamiento
§5.5 del preprint y §15 del consolidado afirman **`g_total − g_pred → 0`** con costos fijos y test creciente, y dicen expresamente que **no** se afirma que el límite se alcance desde arriba, porque los denominadores difieren y el signo no está fijado en general. Se explica el caso del piloto: la diferencia es +0.0088 en los tres controles porque `L_U(T_train) = 811 ≫ L_U(M₀) = 3`, y ese 0.0088 es exactamente 811/92 163. Búsqueda: **0 ocurrencias de "necessarily"**.

### ✅ Reproducción sintética final registrada
`results/reproduccion-final-pre-congelamiento.txt`. Los cinco scripts en el orden pedido. **Idénticos byte a byte:** `ruido_oos_semilla`, `g_metricas_oos`, `contabilidad_completa`. **Una línea distinta, justificada:** `lorenz_checkpoints` (tiempo de cómputo 1.3 → 2.1 s, no es una medición) y `piloto_10_1` (fila `ruido` del OOS, `os.urandom` sin semilla). El control sin semilla se verifica **por invariantes**, no por identidad: p_error = 0.4992 (≈ 0.5 ✓), g_total^bare = 1.0088 (> 1 ✓), ρ_full = 1.000000 exacto con M₀ ganando ✓. La identidad de la regla espuria de esa corrida (208) **no se cita** como resultado, conforme a la Enmienda 6(b). Veredicto impreso: reproducción CORRECTA.

### ✅ El consolidado sigue NOT YET FROZEN
`protocol/protocolo-v1-1-consolidado.md` conserva `STATUS: Prepared for freezing — NOT YET FROZEN OR PREREGISTERED` y la advertencia de que no hay hash, tag ni OSF. La única modificación de contenido es la **incorporación por referencia** de la definición en §7, más los ajustes que E6 y E8 obligan en §13.5 y §15, el tachado de las deudas 1, 2, 3 y 7 del Anexo A, y la cabecera. **No se calculó hash, no se etiquetó Git, no se depositó nada.**

### ✅ Nomenclatura ratificada registrada
Tanto en `definicion-L-M0.md` como en §7 del consolidado: **v1.1 = v1.0 + Enmiendas 1–6 + esta definición; v1.2 reservada para modificaciones posteriores al congelamiento.** La cabecera del consolidado lo refleja.

### ✅ Ningún dataset empírico
No se abrió, descargó ni procesó ninguno. `contabilidad_completa.py` genera todo con las semillas del piloto (Lorenz determinista, autómatas con `default_rng(42)`, PRNG con `default_rng(7)`, ruido reproducible con `default_rng(2026)`) más `os.urandom` para la fila del control negativo histórico.

### ✅ Ninguna cifra inventada; ninguna calculada a mano
Toda cifra nueva de esta ronda proviene de `src/contabilidad_completa.py` con salida archivada. Los subtotales que antes eran sumas manuales ahora los imprime el script. `L_U(M₀) = 3 bits` **no es una suposición**: es ⌈log₂ 5⌉ sobre una familia enumerada explícitamente.

### ✅ Ninguna limitación ni errata eliminada
§7 conserva sus **9 subsecciones**. Las tres entradas de §7.5 bis pasan a "closed" **con su historia visible**, no borradas, y se agrega el párrafo *"What these closures do not buy"*: la contabilidad completa no convierte al piloto en evidencia sobre la naturaleza, no implementa las dos pilas U_ref y **no explica la discrepancia de pendiente**, que sigue sin causa asignada en §7.1 y no fue investigada en esta ronda por instrucción expresa. Las erratas 1–6 permanecen íntegras.

### ✅ Ninguna claim de originalidad fortalecida
Mapa de §3.6 sin cambios: **7 "not original", 1 "close antecedent", 2 "possible novelty" (η_ε "unconfirmed"), 1 "most defensible contribution"**. La reivindicación central conserva su formulación literal con "to the best of our knowledge".

### ✅ Todas las referencias [VERIFY] siguen marcadas
**33 en v0.4, 33 en v0.5.**

### ✅ Versiones anteriores intactas
Verificado por `sha256sum`: sin cambios en los dos `.docx`, `changelog-v1-0-a-v1-1.md`, `enmienda-6.md`, `protocol/README.md`, los cinco scripts previos, las cuatro salidas previas, `preprint-v0-1.md` (v0.2), `preprint-v0-3.md`, `preprint-v0-4.md`, sus dos changelogs, sus dos informes de validación, el informe del piloto y la errata. **Modificados solo los permitidos:** `PENDIENTES.md`, las líneas de estado de `README.md` y `CLAUDE.md`, y el consolidado (por referencia).

### ✅ Propagación de texto mínima, como se pidió
`preprint-v0-5.md` cambia **solo**: §4.3 y §4.5 (remisión a la definición y efecto medido), §5.5 (criterio de escalamiento), §6.2 (números ρ_full y g_total), §6.3 (subtotales impresos), §7.5 bis (tres cierres + qué no compran) y la historia de versiones. Nada más fue reescrito.

---

## Veredicto

**19 ✅ · 0 ⚠️ · 0 ❌.**

La deuda madre está cerrada: `L_U(M₀)` definido, incorporado al consolidado por referencia, y la recomputación hecha con resultado **confirmatorio de la predicción pre-declarada** — ninguna fila se mueve a cuatro decimales, ρ_full ≤ 1 en todas.

**Lo que sigue abierto no es contable:** dos pilas U_ref verdaderas, amortización de bibliotecas, precisión identificable en familias no regulares, instanciación por dominio, 33 referencias sin verificar, revisión humana experta, y la **discrepancia de pendiente de Lorenz sin causa asignada**. El protocolo consolidado está **listo para revisión y decisión del investigador**, y **no congelado**.

---

*Historia: v1 (2026-08-26) — redactado por el asistente de IA bajo supervisión de Maximiliano Winter.*

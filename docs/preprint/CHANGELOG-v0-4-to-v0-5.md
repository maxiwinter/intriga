# Changelog del preprint — v0.4 → v0.5

**Fecha:** 2026-08-26. **Archivo nuevo:** `preprint-v0-5.md`. **Conservados sin modificar:** `preprint-v0-4.md`, `preprint-v0-3.md`, `preprint-v0-1.md` (v0.2) y sus changelogs e informes de validación.

**Naturaleza de esta revisión.** Cierre de la **deuda madre**: la definición de `L_U(M₀)`. La revisión es contable, no interpretativa. **Propagación mínima de texto**, según lo pedido: solo §6.2 (números), §5.5 (criterio de escalamiento) y §4.3/§4.5 (remisión a la definición), más las tres limitaciones de §7.5 bis que pasan a cerradas y la historia de versiones. Ningún dataset empírico fue abierto; ninguna cifra fue calculada a mano; ninguna versión anterior fue modificada.

**Hecho central:** la predicción pre-declarada se **confirmó en las siete filas**. Ningún ρ cambia a cuatro decimales; el mayor desplazamiento es 2.9 × 10⁻⁵.

---

## Tabla de cambios

| # | Sección modificada | Problema | Corrección | ¿Fórmula? | ¿Código? | ¿Valores? | ¿Acción humana posterior? |
|---|---|---|---|---|---|---|---|
| **E1** | `protocol/definicion-L-M0.md` (archivo nuevo); consolidado §7 | **`L_U(M₀)` no estaba definido.** ρ ≤ 1 quedaba garantizado en el papel y no en las cifras; `g_total` simétrica no podía calcularse; el modelo nulo entraba en la contabilidad como si su descripción fuera gratuita — asimetría que lo favorece en el denominador y castiga a los modelos en el numerador. | Definición **simétrica, sin excepciones**: `L_U(T) = L_U(id(T)|M) + L_U(spec(T)|U_ref) + L_U(θ_T)`, aplicada también a M₀. Identificador prefix-free pre-declarado; con k alternativas de primer nivel, código uniforme `L_id = ⌈log₂ k⌉`. **spec(T) = 0 si y solo si T es primitiva declarada de U_ref** — declaración exigida en la especificación de la pila. **M₀ paga su identificador: no es gratis.** Árbol de códigos pre-registrado para familias jerárquicas: `L(familia) + L(submodelo|familia) + L(θ)`, con `Σ_j ⌈log₂ k_j⌉` por ruta, sin omitir niveles (k_j = 1 → 0 bits es el único identificador gratuito legítimo) y con verificación de Kraft si el código es no uniforme. | **SÍ** | No | **No por sí sola** | **SÍ** — instanciar la enumeración de primer nivel, el árbol y las primitivas **de cada dominio empírico** en su propio pre-registro. La definición fija la regla, no la familia de un dominio no medido. |
| **E2** | `definicion-L-M0.md` §3 | La familia de primer nivel del piloto no estaba enumerada. | Enumeración explícita: **{M₀ literal, zlib, bz2, lzma, generativo} → k = 5 → L_id = 3 bits** iguales para los cinco. La pila del piloto declara primitivas la codificación literal y los tres compresores (spec = 0), lo que **justifica spec(M₀) = 0**; el generativo paga su especificación completa. Resultado: **`L_U(M₀) = 3 + 0 + 0 = 3 bits`**. Se declara que esto **subsume y reemplaza** la convención anterior de cobrar log₂3 ≈ 1.6 bits por elegir entre los compresores genéricos. | **SÍ** | No | **Sí, indirectamente**: cambia el numerador de todas las filas en +3 bits y el denominador en +3 bits. | No |
| **E3** | `src/contabilidad_completa.py` y `results/contabilidad-completa-salida.txt` (nuevos) | Faltaba recomputar con el baseline completo. | Script nuevo que reproduce el orden exacto de consumo del PRNG del piloto (para regenerar los surrogates) y recomputa las 7 filas con `L₀_full = L_U(M₀) + L_U(D_ε|M₀)` y cada modelo pagando identificador. Imprime por fila `L0`, `L0_full`, `r_generic`, `ρ_bare`, `ρ_full`, **δ = ρ_full − ρ_bare** y el modelo ganador. **Ningún script ni salida previos fueron modificados.** | No | **SÍ** (script nuevo) | **Sí — y el resultado es que no se mueven.** Ver E4. | No |
| **E4** | §4.3; §6.2 | La predicción pre-declarada («\|δ\| cae bajo el redondeo, ~3 bits sobre denominadores ≥ 6×10⁴») estaba sin verificar. | **CONFIRMADA en las 7 filas.** δ por fila: Lorenz +6.2×10⁻⁶; R110 y R30 +2.9×10⁻⁵; PRNG +1.1×10⁻⁵; ruido +0.0 exacto; surrogate R110 +1.6×10⁻⁷; surrogate Lorenz +4.6×10⁻⁷. **Ninguna fila cambia a cuatro decimales** (verificado e impreso por el script). **Ninguna fila se movió visiblemente, de modo que no hubo hallazgo que reportar en este punto.** | No | No | **No** — las tablas de §6 quedan como estaban impresas; lo que cambió es que ahora el baseline está definido. | No |
| **E5** | §4.3; §6.2 | ρ_full ≤ 1 no estaba verificado empíricamente. | Verificación impresa fila por fila: **ρ_full ≤ 1 en las siete**, con **1.000000 exacto** en el control de ruido, donde gana M₀ — el caso de igualdad previsto por la definición. | No | No | No | No |
| **E6** | §4.5; §6.2; consolidado §13.5 | `g_total` simétrica seguía sin calcularse. | **Calculada.** Con `L_U(T_train) = 811 bits` (3 identificador + 800 fuente comprimida + 8 regla), `L_U(M₀) = 3` y `L_U(D_test\|M₀) = 92 160` (denominador simétrico 92 163): **R110 y R30 → g_total = 0.0088; ruido PCG64 → 1.0088**. La columna histórica **g_total^bare se conserva al lado** y **no se reinterpreta**. Se declara expresamente que la coincidencia a cuatro decimales entre ambas columnas se debe a que 3 bits son despreciables frente a 92 160, **no** a que sean la misma cantidad. | No | **SÍ** (mismo script) | **Sí: columna antes vacía, ahora con valores** — 0.0088 / 0.0088 / 1.0088. Ningún valor histórico fue alterado. | No |
| **E7** | §6.3; consolidado Anexo A punto 7 | Los subtotales de Nivel A y Nivel B eran sumas hechas a mano. | **Impresos por el script**: identificador 3, **Nivel A = 1288 bits** (spec 1096 + θ 192), **Nivel B = 156 × 8 = 1248 bits**, total 2539, Nivel A = 0.5073 del total, más el escalamiento por n (k = 1, 1, 2, 4, 8). **Cierra la deuda 4 de C ter.** | No | **SÍ** | **No** (mismos valores, ahora impresos en vez de derivados) | No |
| **E8** | §5.5; consolidado §15 | El criterio decía **«g_total → g_pred desde arriba»**. Con denominadores distintos el signo de la diferencia **no está fijado**. | Retirado «desde arriba». Se afirma **`g_total − g_pred → 0`** cuando los costos de descripción son fijos y el bloque de test crece, porque entran aditivamente mientras los términos de datos crecen sin cota. Se explica que en el piloto la diferencia es positiva **solo porque** `L_U(T_train) = 811 ≫ L_U(M₀) = 3`, lo que la fija en 811/92 163 = 0.0088 en los tres controles. Se conserva la lectura diagnóstica: una g_total cuya distancia a g_pred no se reduce al crecer el test es firma de ajuste, no de compresión. | **SÍ** | No | **No** | No |
| **E9** | §7.5 bis | Tres limitaciones estaban abiertas por depender de `L_U(M₀)`. | Marcadas **cerradas**, con la evidencia citada. Se agrega un párrafo **«What these closures do not buy»**: la contabilidad completa no convierte al piloto en evidencia sobre la naturaleza, no implementa las dos pilas U_ref y no explica la discrepancia de pendiente. **Ninguna otra limitación fue eliminada:** §7.1, §7.2, §7.3, §7.4, §7.6, §7.7 y §7.8 quedan intactas; §7 conserva sus 9 subsecciones. | No | No | No | No |
| **E10** | `results/reproduccion-final-pre-congelamiento.txt` (nuevo) | Faltaba una reproducción final ordenada. | Los cinco scripts corridos en orden. **`ruido_oos_semilla`, `g_metricas_oos` y `contabilidad_completa`: idénticos byte a byte.** `lorenz_checkpoints`: una línea distinta, el tiempo de cómputo (1.3 s → 2.1 s), que no es una medición. `piloto_10_1`: una línea distinta, la fila `ruido` del OOS (fuente `os.urandom` sin semilla), verificada **por invariantes**: p_error = 0.4992 ≈ 0.5, g_total^bare = 1.0088 > 1. Nota: `contabilidad_completa` usa `os.urandom` y **aun así reprodujo idéntico**, porque las cifras que imprime para esa fila (r_generic 1.0005, ρ_full 1.0000) son estables a cuatro decimales. | No | No | **No** | No |
| **E11** | `protocol/protocolo-v1-1-consolidado.md` (actualizado **solo** por referencia) | La definición no formaba parte del consolidado. | §7 incorpora `definicion-L-M0.md` **por referencia**, con la nomenclatura ratificada (**v1.1 = v1.0 + Enmiendas 1–6 + esta definición; v1.2 reservada para post-congelamiento**), la instanciación por dominio como pendiente y el estado de la deuda del piloto como cerrada. Anexo A: deudas 1, 2, 3 y 7 tachadas con su evidencia. §13.5 y §15 ajustados por E6 y E8. Cabecera y lista de fuentes actualizadas. **El bloque STATUS sigue diciendo `Prepared for freezing — NOT YET FROZEN OR PREREGISTERED`.** Sin hash, sin tag, sin OSF. | No | No | No | **SÍ** — revisión del investigador y decisión de congelar. |

---

## Lo que esta ronda deliberadamente NO hizo

- **No investigó la discrepancia de pendiente de Lorenz** (64.2 promedio de tramos / 67.6 ajuste contra 76.5 predicho): excluido por la consigna y sigue sin causa asignada.
- **No abrió ningún dataset empírico** ni ejecutó nada de espectros.
- **No congeló nada:** sin hash, sin tag de Git, sin depósito OSF.
- **No modificó ningún archivo previo**, salvo `PENDIENTES.md` y las líneas de estado de `README.md` y `CLAUDE.md`.
- **No tocó `verificacion_piso_y_eta.py`** ni ninguna salida archivada previa.

## Acciones humanas tras v0.5

1. **Revisar `protocol/protocolo-v1-1-consolidado.md` y `protocol/definicion-L-M0.md`** y decidir el congelamiento (PDF + SHA-256 + tag + OSF).
2. **Instanciar la familia de primer nivel, el árbol de códigos y las primitivas declaradas** de cada dominio empírico en su pre-registro.
3. **Implementar dos pilas U_ref verdaderas**; política de amortización de bibliotecas; regla de precisión identificable en familias no regulares.
4. **Verificar las 33 referencias `[VERIFY]`** contra fuente primaria.
5. **Revisión humana experta** (MDL/AIT + dominio físico) antes del primer resultado empírico.
6. Decidir si `ERRATA-piloto-v1-1.md` se incorpora al informe del piloto.
7. Afiliación, ORCID, licencia.
8. Investigar o reportar la discrepancia de pendiente de Lorenz.

---

*Historia: v1 (2026-08-26) — redactado por el asistente de IA bajo supervisión de Maximiliano Winter.*

# Changelog del preprint — v0.2 → v0.3

**Fecha:** 2026-08-26. **Archivo nuevo:** `preprint-v0-3.md`. **Archivo conservado sin modificar:** `preprint-v0-1.md` (contiene la v0.2; su nombre y su contenido habían divergido).

**Naturaleza de esta revisión.** Correcciones **formales y de redacción**. Ninguna cifra experimental se generó, alteró ni inventó; ninguna limitación se eliminó; ninguna referencia perdió su marca `[VERIFY]`; ninguna afirmación de originalidad se fortaleció. Dos correcciones (C1, C2) reparan definiciones que estaban mal y dejan una **deuda numérica declarada**, no absorbida: el texto dice qué falta calcular y por qué no se calculó aquí.

**Convención de versionado adoptada desde esta revisión:** un archivo por versión, nombre = contenido. Nada se edita en el lugar una vez publicada una versión.

---

## Tabla de cambios

| # | Sección modificada | Problema | Corrección | ¿Fórmula? | ¿Código? | ¿Valores? | ¿Acción humana posterior? |
|---|---|---|---|---|---|---|---|
| **C1** | Abstract; §4.3; §7.5 bis | `ρ_MDL ≤ 1` se afirmaba "by construction", pero con denominador = residuo literal el numerador incluye `L(M₀)` y el denominador no: la cota real era `1 + L(M₀)/L₀ > 1`. La afirmación era **falsa**. | Baseline **completo** `L₀^full = L_U(M₀) + L_U(D_ε\|M₀)`. Con M₀ miembro de la familia, `ρ ≤ 1` es consecuencia exacta, y `ρ = 1` se alcanza cuando gana M₀. Se explica por qué el baseline desnudo no sirve. | **SÍ** | No | **En principio sí, no aplicados.** Las cifras de §6 siguen contra el baseline desnudo; se declara explícitamente. Desplazamiento de orden `L(M₀)/L₀` (centenares de bits sobre 10⁵–10⁶), bajo el redondeo de las tablas. **Nada se ajustó en silencio.** | **SÍ** — definir `L_U(M₀)` en el código y recorrer los scripts bajo la regla de trazabilidad (Enmienda 6) para republicar los ρ con el baseline completo. |
| **C2** | Abstract; §4.5; §6.2; §6.3 punto 4; §6.6; §8.3; §7.5 bis | `g` estaba **definido** como solo-residuo `L(D_test\|T)/L(D_test\|M₀)` pero **reportado** como modelo+residuo (el script calcula `(L(T)+L(D_test\|T))/tot`). Dos cantidades distintas bajo un mismo símbolo. | Se definen y reportan por separado **`g_pred`** (solo residuo) y **`g_total`** (incluye el costo del modelo amortizado). Se explicita `g_total > g_pred` siempre, y que `g_total > 1` con predicción perfecta es una propiedad del tamaño del bloque de test, no un fallo de predicción. Ningún valor se cita como `g` a secas. | **SÍ** | No | **No** (re-etiquetado). Los valores del piloto son `g_total`: 0.0088 (R110/R30), 1.009 (urandom), 1.0088 (PCG64). Los `g_pred` (0 y ≈1) se **derivan** del error de test archivado y se marcan como derivados, no impresos. | **SÍ** — un script debe imprimir ambos antes de que cualquiera se cite en una tabla publicada. |
| **C3** | §4.7; §6.3; §7.5 bis | 2655 pasos se llamaba "**Lyapunov horizon**". Contradice el propio hallazgo del piloto: ese valor está **limitado por el piso aritmético float64** (queda clavado en 2655 para b = 6…10), no por la dinámica. | Se introduce **`h(p, ε)` — horizonte de re-sincronización medido**, con ambos argumentos siempre registrados, explícitamente distinto del horizonte de Lyapunov teórico `≈ p·ln2/λ`. Evidencia archivada de su dependencia de ε: 3194 / 2655 / 2655 / 2655 / 2458 para b = 4/6/8/10/12. | **SÍ** (definición) | No | **No** | **SÍ** — decidir si `h(p,ε)` entra al texto consolidado del protocolo **antes** del congelamiento o como v1.2. **No se aplicó a `/protocol`** (instrucción 0c); queda como propuesta en `PENDIENTES.md`. |
| **C4** | Título (nota); Abstract; §5.8; §8.5; §9; Data availability | Se afirmaba un preregistro y un congelamiento **que no existen**: "a preregistered protocol (v1.1, **frozen** before any empirical data set is examined)". | Nota al pie del título: "preregistered" describe la **disciplina de diseño**, no un depósito consumado. Abstract: "written to be preregistered — freezing and public deposit still pending". §5.8 abre con la advertencia explícita. §8.5: "Once frozen…". §9: "preregistration-ready". Data availability: "**No preregistration record exists yet to cite**". Sin hash, sin identificador, sin fecha. | No | No | **No** | **SÍ** — congelar v1.1 (PDF + SHA-256 + tag) y depositar en OSF. Solo entonces puede citarse un hash. |
| **C5** | §6.3; §8.4; §7.5 bis | El costo de la regla de Lorenz figuraba como "≈ 1400 bits", heredado de la constante obsoleta 1252 corregida por la Enmienda 6. | **1288 bits** (1096 de fuente comprimida + 192 de parámetros), trazado a `results/lorenz-checkpoints-salida.txt`. | No | No | **SÍ** — 1400 → **1288**. | **SÍ** — el informe del piloto sigue diciendo "~1.400"; falta **Errata 5** en su sección de erratas (no editado en esta tanda: no fue pedido). |
| **C6** | §6.3 (tabla nueva); §6.6 | La fila de Lorenz mezclaba en un solo ρ el costo de la **regla** (fijo) y el de la **trayectoria** (creciente). | Descomposición explícita **Track A (nivel A: la regla, 1288 bits fijos) / Track B (nivel B: esta trayectoria, 156·⌈n/h⌉ = 156…1248 bits)**, con la observación de que la regla pasa del 89 % al 51 % de la descripción entre n = 1000 y n = 20 000. Además, rótulo explícito en §6.6 separando **claims metrológicos** (todo §6) de **claims sobre la naturaleza** (ninguno). | No | No | **No** (reorganiza cifras archivadas; 1288 y 1248 son sumas de cantidades impresas). | **SÍ** — **confirmar la lectura**: se interpretó "Track" como el *nivel descriptivo* A/B del protocolo. Queda marcado en §7.8 como lectura tomada, no verificada. |
| **C7** | §1 (Structure); §9 | "was not settled **because it could not be**" — afirmación fuerte sobre un debate ajeno, y roza el marco prohibido de "el debate esperaba este experimento". | Reformulado a lo descriptivo: el intercambio **no convergió**; ambas partes medían cantidades distintas bajo convenciones no expuestas lado a lado. Se agrega: "We do not claim the dispute was unresolvable, nor that it was waiting for an instrument." | No | No | **No** | No |
| **C8** | §8.2 | "a model family that **does not contain the answer in advance**" — indemostrable: toda familia expresiva contiene la regularidad implícitamente. | La restricción se reformula al nivel de **primitivas y bibliotecas** (sin Rydberg, sin defecto cuántico, sin niveles como primitiva), reconociendo que una familia expresiva la contiene implícitamente y que lo que compra el pre-registro no es inocencia sino la **obligación de pagarla** en longitud de descripción. | No | No | **No** | No |
| **C9** | §7.5 bis y §7.8 (nuevas); §7.9 (renumerada); Data availability; historia de versiones | Higiene: las reparaciones anteriores no podían quedar sin registro en las limitaciones. | Dos subsecciones nuevas de limitaciones (deudas numéricas de C1/C2/C3 y C5; lectura no verificada de C6). §7 pasa de 8 a **10** subsecciones. Historia de versiones ampliada. | No | No | **No** | No |

---

## Acciones humanas consolidadas

1. **Definir `L_U(M₀)`** y recalcular todos los ρ con el baseline completo, bajo Enmienda 6 (script + salida archivada). Hasta entonces, las cifras publicadas son contra el baseline desnudo y así están declaradas.
2. **Script que imprima `g_pred` y `g_total`** por separado; hoy solo se imprime `g_total`.
3. **Errata 5 en el informe del piloto**: "~1.400 bits" → 1288 bits (Track A).
4. **Confirmar la lectura de Track A / Track B** (se tomó: niveles descriptivos A y B).
5. **Decidir el destino de `h(p, ε)`**: incorporarlo al texto consolidado del protocolo antes del congelamiento, o dejarlo para una v1.2. **No se tocó `/protocol`.**
6. **Congelar v1.1 y depositar** (PDF, SHA-256, tag, OSF) antes de citar cualquier hash.
7. **Verificar las 33 referencias `[VERIFY]`** contra fuente primaria (`PENDIENTES.md`).
8. **Revisión humana experta** (MDL/AIT + dominio físico) antes del primer resultado empírico.

---

*Historia: v1 (2026-08-26) — redactado por el asistente de IA bajo supervisión de Maximiliano Winter.*

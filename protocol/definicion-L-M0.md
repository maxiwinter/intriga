# Definición formal de L_U(T) y de L_U(M₀)
## Cierre de la deuda madre del pre-congelamiento

**Fecha:** 2026-08-26. **Estado:** incorporación al Protocolo v1.1 consolidado **antes del congelamiento**.

**Decisión de nomenclatura ratificada por el investigador:**

> **v1.1 = v1.0 + Enmiendas 1–6 + esta definición.**
> **v1.2 queda reservada para modificaciones posteriores al congelamiento.**

Esta definición no nace de resultados: nace de una deuda contable detectada durante la preparación del preprint (`docs/preprint/VALIDATION-REPORT-v0-4.md`, tres reservas), y se registra antes de que exista cualquier medición empírica.

---

## 1. El problema que cierra

El protocolo exigía normalizar por el baseline completo **L₀_full = L_U(M₀) + L_U(D_ε | M₀)** y calcular **g_total** con ese mismo baseline, pero **nunca definió L_U(M₀)**. Sin esa definición:

- ρ ≤ 1 quedaba garantizado en el papel y no en las cifras;
- g_total simétrica no podía calcularse;
- el modelo nulo entraba en la contabilidad como si su descripción fuera gratuita, mientras todo otro modelo pagaba la suya — una asimetría que favorece sistemáticamente a M₀ en el denominador y castiga a los modelos en el numerador.

## 2. Definición general (simétrica, sin excepciones)

Para **todo** modelo T de la familia M, incluido M₀ y sin tratamiento especial:

> **L_U(T) = L_U(id(T) | M) + L_U(spec(T) | U_ref) + L_U(θ_T)**

donde:

- **L_U(id(T) | M)** — **identificador**: los bits necesarios para señalar *cuál* miembro de la familia pre-registrada se está usando. Se codifica con un **código prefix-free pre-declarado**. Con *k* alternativas de primer nivel y código uniforme:

  > **L_id = ⌈log₂ k⌉ bits**

  El código debe quedar fijado antes de mirar D_test. Puede usarse un código no uniforme (asignando menos bits a modelos declarados a priori más plausibles) siempre que sea prefix-free y esté pre-registrado; en ese caso se documenta la asignación completa.

- **L_U(spec(T) | U_ref)** — **especificación estructural**: la descripción del modelo en la pila de referencia (código fuente, ecuaciones, operadores, bibliotecas cargadas). Vale 0 **si y solo si** el modelo es una **primitiva declarada** de U_ref.

- **L_U(θ_T)** — **parámetros**, bajo la regla MDL de precisión identificable pre-registrada (§5.2 del protocolo).

### 2.1 Aplicación a M₀ — el modelo nulo no es gratis

M₀ recibe exactamente el mismo tratamiento:

> **L_U(M₀) = L_id(M₀) + L_U(spec(M₀) | U_ref) + L_U(θ_M₀)**

- **L_id(M₀) = ⌈log₂ k⌉.** M₀ **paga su identificador** como cualquier otro miembro. Esto es lo que impide la asimetría descrita en §1.
- **spec(M₀) = 0 es defendible si y solo si la codificación literal es una primitiva declarada de la pila U_ref**, y esa declaración debe figurar explícitamente en la especificación de la pila (§6 del protocolo). Si una pila **no** declara la codificación literal como primitiva, M₀ debe pagar su especificación como cualquier otro modelo, y el baseline cambia en consecuencia.
- **θ_M₀ = 0** cuando el código literal no tiene parámetros libres. Si la representación literal exige declarar rangos, longitudes o alfabetos que no estén ya fijados por §4.1, esos bits se cuentan aquí.

**Consecuencia formal.** Como M₀ ∈ M y su costo total es L₀_full = L_U(M₀) + L_U(D_ε | M₀), se sigue **C ≤ L₀_full** y por tanto **ρ = C / L₀_full ≤ 1** de manera exacta, con ρ = 1 cuando la descripción nula es óptima, posiblemente empatada con otro modelo de igual costo total.

## 3. Familia de primer nivel del piloto §10.1 (enumeración explícita)

Para los controles sintéticos ya ejecutados, la familia de primer nivel queda enumerada así:

| # | Miembro | spec | θ |
|---|---|---|---|
| 1 | **M₀** — codificación literal | 0 (primitiva declarada) | 0 |
| 2 | **zlib** (nivel 9) | 0 (primitiva declarada) | 0 |
| 3 | **bz2** (nivel 9) | 0 (primitiva declarada) | 0 |
| 4 | **lzma** | 0 (primitiva declarada) | 0 |
| 5 | **generativo** — codificador de dos partes del dominio | gzip del fuente declarado | parámetros + condición inicial + checkpoints |

> **k = 5  →  L_id = ⌈log₂ 5⌉ = 3 bits**, iguales para los cinco miembros.

**Qué es y qué no es este 3.** La aritmética ⌈log₂ 5⌉ = 3 es exacta y no se ajustó a ningún resultado. Pero **elegir una familia de cinco miembros** y **elegir un código de identificador uniforme y prefix-free** son **convenciones de la pila U_ref**, declaradas de antemano. El valor 3 bits se sigue deterministamente de esas convenciones; **no es una cantidad canónica ni ontológica** del modelo nulo. Bajo otra familia declarada o un código no uniforme, L_U(M₀) sería otro número.

**Declaración de primitivas exigida por §2.1.** La pila de referencia del piloto declara como primitivas la **codificación literal** y los **tres compresores genéricos** {zlib, bz2, lzma}. Por eso spec = 0 para los miembros 1–4 y **spec(M₀) = 0 queda justificado**. El miembro 5 no es primitiva y paga su especificación completa.

**Nota sobre la convención anterior — corregida por la auditoría final (2026-08-26).** Informes anteriores **declaraban** un cargo de selección de log₂3 ≈ 1.585 bits por elegir el mejor compresor genérico dentro de su metaclase, pero **los totales numéricos trazados no incorporaban ese cargo**. La evidencia es directa: el total histórico de Lorenz es

> 1096 (fuente comprimida) + 192 (parámetros) + 1248 (checkpoints) = **2536 bits**,

que no contiene ningún sumando de selección, frente a

> 3 (identificador) + 1096 + 192 + 1248 = **2539 bits**

bajo la contabilidad presente. Por tanto:

> *Earlier reports stated a log₂3 selection charge for the generic-compressor meta-class, but the traced numerical totals did not include that charge. The unified 3-bit first-level identifier now replaces that stated convention and is explicitly included in all recomputed full-accounting results.*

El identificador de 3 bits **no** es un reetiquetado de 1.585 bits que ya estuvieran efectivamente pagados: numéricamente no lo estaban. La discrepancia queda registrada como **Errata 7** en `docs/ERRATA-piloto-v1-1.md`. Verificación impresa por `src/contabilidad_completa_v2.py`.

**Advertencia de alcance, sin cambios.** Estos cinco miembros **no** son dos pilas U_ref. Siguen siendo codificadores de una sola metaclase más un codificador generativo; la deuda de las dos pilas verdaderas e independientes permanece abierta (§6 del protocolo, Anexo A punto 4).

## 4. Árbol de códigos para familias jerárquicas (pre-registro)

Cuando la familia tenga estructura de árbol — el caso esperado en los dominios empíricos, donde una "familia" agrupa muchos submodelos — el identificador se descompone por niveles y **cada nivel paga**:

> **L_U(T) = L(familia | M) + L(submodelo | familia) + L(θ)**

y, en general, para una ruta de profundidad *m* en el árbol:

> **L_U(id(T)) = Σ_{j=1..m} ⌈log₂ k_j⌉**

donde *k_j* es el número de alternativas **en el nodo j** de la ruta. Reglas:

1. El árbol completo —nodos, aridades y orden— se pre-registra antes de mirar D_test. Agregar una rama después equivale a modificar la familia y está prohibido por §6 y §8 del protocolo.
2. Ningún nivel puede omitirse por ser "obvio": si en un nodo hay una sola alternativa, k_j = 1 y ⌈log₂ 1⌉ = 0 bits, lo cual es el único caso legítimo de identificador gratuito.
3. Si el árbol es no uniforme y se prefiere un código prefix-free no uniforme, se documenta la asignación completa de longitudes y se verifica la desigualdad de Kraft.
4. **El costo de búsqueda dentro de la familia** —selección de hiperparámetros o de arquitectura que use información del entrenamiento— se contabiliza aparte, según §8 del protocolo. El identificador cubre *señalar* el modelo elegido, no *encontrarlo*.

## 5. Efecto sobre las métricas

Con esta definición, y **sin cambiar ningún dato**:

- **ρ_full = C / L₀_full**, con C = min sobre T∈M de [L_U(T) + L_U(D_ε|T)] y todos los L_U(T) incluyendo su identificador. **ρ_full ≤ 1 exacto.**
- **g_total simétrica** pasa a ser calculable:
  > g_total(T) = [L_U(T_train) + L_U(D_test,ε | T_train)] / [L_U(M₀) + L_U(D_test,ε | M₀)]
- **g_pred** no cambia: no involucra costos de modelo en ninguno de sus dos lados.

Los valores históricos del piloto fueron calculados con la convención anterior (baseline desnudo, sin identificadores). Se conservan bajo los nombres **ρ_bare** y **g_total^bare** y **no se reinterpretan**; la comparación fila por fila se publica con su diferencia δ explícita (`src/contabilidad_completa.py`, `results/contabilidad-completa-salida.txt`).

## 6. Lo que esta definición NO cierra

- No implementa las dos pilas U_ref independientes.
- No fija la política de amortización de bibliotecas compartidas entre dominios.
- No resuelve la regla de precisión identificable para familias no regulares.
- No dice nada sobre la discrepancia de pendiente de Lorenz, que sigue sin causa asignada.
- Para cada dominio **empírico**, la enumeración de primer nivel, el árbol de códigos y la declaración de primitivas **deben instanciarse en su propio pre-registro**: esta sección fija la *regla*, no la *familia* de un dominio que todavía no se midió.

---

*Historia: v1 (2026-08-26) — redactada por el asistente de IA; **v1.1 (2026-08-26, auditoría final):** corregida la nota sobre la convención anterior (el cargo log₂3 estaba declarado pero no incorporado a los totales trazados; Errata 7) y añadida la advertencia de que 3 bits es consecuencia de convenciones pre-declaradas, no un valor canónico. Ninguna cifra cambió. — redactada por el asistente de IA bajo supervisión de Maximiliano Winter, para cerrar la deuda madre registrada en `docs/preprint/PENDIENTES.md` (C ter, punto 1) y en el Anexo A del protocolo consolidado. Incorporada al Protocolo v1.1 consolidado por referencia en §7. **El protocolo sigue NO CONGELADO.***

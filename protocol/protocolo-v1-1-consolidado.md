# Protocolo experimental — Programa I
## Medición de la estratigrafía de la comprimibilidad
### Versión 1.1 consolidada = v1.0 + Enmiendas 1–6 + definición de L_U(T)/L_U(M₀)

> ## STATUS
> ### **FROZEN 2026-08-27 — sha256 en /HASHES.txt — snapshot de fase IA, previo a revisión experta independiente**
>
> **Documentos fuente, no modificados:** `protocolo-experimental-programa-I-v1-0.docx` (texto maestro), `changelog-v1-0-a-v1-1.md` (Enmiendas 1–5), `enmienda-6.md` (trazabilidad y control de ruido dual), `definicion-L-M0.md` (contabilidad de identificador, especificación y parámetros; incorporada por referencia en §7). Ante cualquier discrepancia de redacción, **los documentos fuente prevalecen** hasta el congelamiento.

---

## 1. Objetivo

Este protocolo operacionaliza el Programa I — Compresibilidad de las regularidades. El objetivo no es demostrar que "el universo es comprimible", sino **medir cuánto del contenido informativo de conjuntos de observaciones puede trasladarse desde los datos hacia una descripción generalizable**.

Pregunta experimental: ¿cómo escala el costo descriptivo óptimo de un dominio cuando aumentan la cantidad, diversidad y resolución de sus observaciones?

Hipótesis principal: distintos dominios y distintos niveles descriptivos dentro de un mismo dominio pueden ocupar regiones diferentes de una superficie de comprimibilidad, indexada por (dominio, nivel descriptivo, n, ε), donde *n* controla cantidad y diversidad, *ε* la resolución exigida, *d* qué errores son físicamente relevantes y *U_ref* el sistema de codificación.

## 2. Hipótesis

- **H1 — Compresión estructural.** Existen dominios o niveles descriptivos para los cuales C(d,U_ref; D_n, ε) ≪ L_Uref(D_n,ε) de manera persistente cuando aumentan n y 1/ε.
- **H2 — Generalización.** La compresión no es únicamente retrospectiva: los modelos seleccionados sobre datos de entrenamiento conservarán ventaja descriptiva sobre observaciones no utilizadas en su construcción.
- **H3 — Robustez.** Las diferencias observadas sobrevivirán a cambios preespecificados de U_ref, resoluciones, variaciones admisibles de la métrica de distorsión, tamaño del corpus y partición train/test.
- **H4 — Estructura frente a contenido marginal.** La ventaja descriptiva disminuirá sustancialmente cuando la estructura relevante se destruya mediante surrogates que preserven características marginales.
- **H5 — Estratigrafía.** La comprimibilidad no será necesariamente uniforme entre dominios ni dentro de un mismo dominio.

## 3. Principio contable

Toda comparación se realiza mediante codificación de dos partes:

> **C(d,U; D_n, ε) = min sobre T∈M [ L_U(T) + L_U(Q(d,ε)(D_n) | T) ]**

La primera parte es el costo del modelo; la segunda, el costo de describir lo que el modelo no absorbió.

> **ΔC = C(nuevo) − C(anterior). Solo existe compresión efectiva si ΔC < 0.**

Reducir la cantidad de parámetros no constituye por sí mismo una mejora. Si una teoría elimina 100 bits de datos pero exige 500 bits nuevos de maquinaria, la descripción total empeoró.

## 4. Pre-registro obligatorio

Antes de ejecutar cualquier comparación quedan congelados los elementos siguientes.

**4.1 Representación de datos.** Estructura matemática de D, unidades, orden de las variables, normalización, tratamiento de datos faltantes, transformaciones permitidas, metadatos incluidos y excluidos. Toda transformación debe poder aplicarse de manera determinista desde el dataset original.

*Enmienda 1 (aplicada aquí):* para datasets empíricos se declara además el **piso de precisión del instrumento de medición**, con la misma obligatoriedad que las unidades. Ninguna afirmación sobre pendientes de resolución es interpretable en el régimen donde ε se aproxima a ese piso.

**4.2 Proveniencia y contaminación teórica.** Cada corpus se clasifica como: (1) medición instrumental primaria; (2) dato calibrado; (3) dato procesado; (4) producto de ajuste teórico. Se documenta qué modelos físicos, estadísticos o numéricos participaron en su producción. **Un dataset cuya generación ya incorpore la estructura que un modelo candidato intenta descubrir no puede utilizarse como evidencia principal a favor de ese modelo**; solo como prueba metodológica o control.

**4.3 Métrica de distorsión.** Se fija previamente d(D, D̂), que determina qué diferencia entre dato y reconstrucción constituye pérdida físicamente significativa. Debe depender del significado del observable, no de la conveniencia del algoritmo. Si existen varias métricas científicamente defendibles, se pre-registran todas.

**4.4 Resolución.** Conjunto discreto ε₁ > ε₂ > … > ε_m, expresado en relación con d. No se elige ε después de observar cuál favorece la hipótesis.

**4.5 Cuantizador.** Algoritmo determinista Q(d,ε): D → D_ε, congelado antes de comparar modelos.

**4.6 Puente entre distorsión y bits.** El residuo se codifica mediante una distribución predictiva explícita o una codificación secuencial/prequential equivalente previamente especificada: L_U(D_ε | T) = −log₂ P_T(D_ε). Para densidades continuas, P_T es la masa integrada sobre la celda de cuantización, no el valor puntual.

## 5. Contabilidad del modelo

**5.1 Estructura.** L_U(T) = L_U(estructura) + L_U(θ | estructura). Toda ecuación, operador, biblioteca o submodelo específico del dominio se contabiliza.

**5.2 Parámetros continuos.** No se penaliza por "cantidad de decimales escritos": se emplea una regla MDL de precisión identificable fijada de antemano. La precisión exigida a θ debe aumentar cuando sea necesario para sostener predicciones a menor ε, de modo que L(T) no se trate como constante cuando ε → 0.

**5.3 Codificadores con re-sincronización (Enmienda 2).** Para dominios con dinámica sensible a condiciones iniciales, la familia M **debe incluir codificadores con re-sincronización de estado** (checkpoints), con el costo de cada checkpoint contabilizado en L(T) o en el residuo según la convención pre-registrada. Su ausencia **invalida** cualquier conclusión de "agotamiento de la compresibilidad" en niveles B.

**5.4 Horizonte de re-sincronización h(p, ε) (Enmienda 6, incorporación formal).**

> **h(p, ε) = horizonte de re-sincronización medido**: número de pasos durante los cuales un estado especificado con precisión *p* reproduce la trayectoria de referencia a resolución *ε* bajo el criterio de fidelidad declarado.

Reglas de uso, no negociables:

1. **h se mide; no se deriva.** h(p, ε) **no es** p·ln2/λ ni ningún "horizonte de Lyapunov" teórico. El horizonte teórico puede usarse como referencia o predicción contra la cual comparar h, y esa comparación se reporta; nunca lo sustituye.
2. **Ambos argumentos se registran siempre.** h depende de la resolución además de la precisión: en el piloto, h = 3194, 2655, 2655, 2655, 2458 pasos a 4, 6, 8, 10 y 12 bits por coordenada.
3. **Se declara el piso** aritmético (sintéticos) o instrumental (empíricos) que acota h. Un h que no se mueve mientras cambia la resolución es firma de piso, no de dinámica: en el piloto, el tramo plano en 2655 corresponde al piso float64 de la referencia (Enmienda 1).
4. **Número de checkpoints:** N_checkpoints = ⌈n / h(p, ε)⌉, y **cada checkpoint paga su costo**.
5. **Si h se optimiza en lugar de fijarse previamente, debe pagarse el costo de seleccionarlo** dentro de la familia de modelos, como cualquier otra decisión de selección.

**5.5 Corolario sobre dinámica determinista (Enmienda 2, forma corregida; Enmienda 5).** Bajo dinámica determinista computable, K(S_t) ≲ K(S₀) + K(L) + K(t) + O(1): no aparecen bits nuevos. Lo que crece es la **precisión de S₀ que debe resolverse** para sostener la descripción de la historia a resolución fija, a tasa h_KS = (1/ln2)·Σλᵢ⁺ bits por unidad de tiempo **bajo las condiciones en que la relación de Pesin resulta aplicable** — condicionada por propiedades de la dinámica y de la medida invariante, no identidad universal. Esos bits se contabilizan en K(D|T,S₀). **Jamás se formula como creación de información.**

## 6. Pila de referencia

Se pre-registran **al menos dos pilas de codificación independientes** U_ref⁽¹⁾, U_ref⁽²⁾. Cada una especifica: intérprete; conjunto de primitivas; representación de números; operadores matemáticos disponibles; bibliotecas generales; bibliotecas específicas de dominio; costo de incorporar una biblioteca nueva; regla de amortización de bibliotecas reutilizadas.

*Enmienda 1 (aplicada aquí):* cada pila declara además **la aritmética de referencia** — formato de punto flotante, esquema de redondeo, orden de operaciones del integrador cuando aplique — **y el piso de precisión resultante**.

Ninguna primitiva puede agregarse después de observar D_test. El resultado principal se considera robusto solo si la jerarquía observada entre condiciones sobrevive a las pilas pre-registradas.

*Advertencia de estado:* un conjunto de compresores genéricos ejecutados en paralelo **no** constituye dos pilas: son codificadores competidores de una misma metaclase (Enmienda 5). Las pilas verdaderas siguen **sin implementar**; es deuda abierta.

## 7. Modelo nulo

Cada dominio tiene un código nulo M₀ que no explota la estructura que se intenta detectar. La familia de modelos **siempre** incluye una estrategia literal o casi literal, de modo que el procedimiento pueda concluir legítimamente *no existe compresión útil dentro de la familia evaluada*.

**Baseline completo (incorporación formal).** El costo de referencia contra el cual se normaliza es el costo **total** de la opción nula, descripción del modelo nulo incluida:

> **L₀_full = L_U(M₀) + L_U(D_n,ε | M₀)**

**Definición de L_U(M₀) — incorporada por referencia (2026-08-26).** La regla general que fija L_U(T) para todo modelo de la familia, **M₀ incluido y sin tratamiento especial**, es:

> **L_U(T) = L_U(id(T)|M) + L_U(spec(T)|U_ref) + L_U(θ_T)**

con identificador prefix-free pre-declarado (uniforme: L_id = ⌈log₂ k⌉ para k alternativas de primer nivel), spec(T) = 0 **si y solo si** T es primitiva declarada de U_ref, y el árbol de códigos para familias jerárquicas. **M₀ paga su identificador: no es gratis.** El texto completo, con la enumeración de la familia de primer nivel del piloto (k = 5 → L_id = 3 bits, L_U(M₀) = 3 bits) y las reglas del árbol jerárquico, es **`protocol/definicion-L-M0.md`**, que forma parte de esta versión consolidada.

**Nomenclatura ratificada:** v1.1 = v1.0 + Enmiendas 1–6 + esta definición. v1.2 queda reservada para modificaciones posteriores al congelamiento.

**Instanciación por dominio, pendiente.** Esta sección fija la *regla*. Para cada dominio empírico, la enumeración de primer nivel, el árbol de códigos y la declaración de primitivas deben instanciarse en su propio pre-registro, y toda cifra publicada debe indicar contra qué baseline fue calculada.

**Estado de la deuda del piloto: cerrada.** `src/contabilidad_completa.py` (salida en `results/contabilidad-completa-salida.txt`) recomputó las siete filas con L₀_full y con cada modelo pagando su identificador: **ninguna cambia a cuatro decimales** (mayor desplazamiento 2.9 × 10⁻⁵) y **ρ_full ≤ 1 se verifica fila por fila**, con 1.000000 exacto en el control de ruido. `src/contabilidad_completa_v2.py` (salida en `results/contabilidad-completa-v2-salida.txt`) reproduce esa tabla sin cambios y añade la verificación por assert de la identidad de §13.5.

**Advertencia sobre el valor 3 bits.** L_U(M₀) = 3 no es una propiedad canónica del modelo nulo: ⌈log₂ 5⌉ = 3 es aritmética exacta, pero *cuáles* cinco miembros forman la familia de primer nivel y *que* el código de identificador sea uniforme y prefix-free son **convenciones de la pila U_ref, declaradas de antemano**. Bajo otra familia declarada o un código no uniforme, L_U(M₀) toma otro valor y la contabilidad debe rehacerse bajo esa declaración.

## 8. Familias de modelos

Para cada dominio se congela previamente M = {T₁, …, T_k}: ecuaciones diferenciales, modelos probabilísticos, gramáticas, modelos simbólicos, compresores universales, modelos autoregresivos, sistemas dinámicos, arquitecturas de aprendizaje previamente definidas. **Se registra el costo de cualquier búsqueda de hiperparámetros o selección de arquitectura** que utilice información del entrenamiento.

*Enmienda 5:* el costo de selección se contabiliza **en dos niveles**: la clase (log₂k de la metaclase de codificadores) y el identificador del modelo ganador dentro de la familia.

## 9. Niveles descriptivos

Las comparaciones entre dominios se realizan entre niveles aproximadamente equivalentes:

- **Nivel A — Regularidades generales.** Estructuras reutilizables sobre muchas instancias.
- **Nivel B — Trayectorias o realizaciones particulares.** Historias concretas generadas bajo esas regularidades.
- **Nivel C — Microestado o detalle fino.** Descripción altamente específica de una realización.

No se compara una ley fundamental contra una historia microscópica particular como si fueran objetos del mismo nivel. El objeto experimental es C(dominio, nivel, n, ε, U_ref).

*Nota de nomenclatura (Enmienda 6 / v0.4 del preprint):* la descomposición **Nivel A / Nivel B** es esta, y solo esta. No debe confundirse con la distinción **Track A / Track B** de §11.1, que organiza el diseño de la medición empírica y es independiente de los niveles descriptivos.

## 10. Batería piloto

**10.1 Controles sintéticos.** Validan el instrumento, no son evidencia sobre la naturaleza. Control positivo de dinámica compacta (Lorenz); control determinista complejo (Regla 110); control pseudoaleatorio determinista (Regla 30 y, en grupo separado, PRNG); control negativo (ruido de fuente preespecificada).

**Control de ruido dual (Enmienda 6b).** El control negativo se desdobla:
1. **`os.urandom` se mantiene** como control declaradamente **irreproducible**: la fuente no depende de ningún generador determinista que la familia pudiera capturar. **Invariantes reportables:** p_error ≈ 0.5, g > 1 y, en la tabla principal, r_generic ≈ 1 y ρ_MDL = 1. **La identidad de la regla espuria es dependiente de corrida y no se cita.**
2. **Ruido PRNG con semilla declarada** (PCG64, semilla 2026) para la fila reproducible del test fuera de muestra, citable a la precisión impresa.

Todo control cuya fuente sea no determinista **declara de antemano qué invariantes reporta y qué identificadores no**.

**Estado:** ejecutado y aprobado; informe en `docs/piloto-seccion-10-1-informe-final.md`, con erratas de trazabilidad en el propio informe y en `docs/ERRATA-piloto-v1-1.md`.

**10.2 Surrogates.** Para cada dataset real, cuando sea científicamente posible: permutación temporal, phase randomization, permutación espacial, shuffling de bloques, preservación del histograma con destrucción de correlaciones. Definidos **antes** del análisis. La hipótesis estructural predice C(D) < C(D_surrogate) una vez normalizados tamaño y resolución.

## 11. Datasets empíricos piloto

**11.1 Física fundamental — primera medición.** Se priorizan mediciones instrumentales o datasets cuya cadena de procesamiento no incorpore explícitamente la teoría evaluada: espectros atómicos experimentales; datos orbitales primarios o astrometría previa al producto final de efemérides; datasets de scattering o transiciones con documentación completa de calibración. Los catálogos derivados por ajuste dinámico pueden usarse como demostración metodológica, **no** como evidencia principal.

### Diseño en dos tracks (incorporación formal)

La medición se organiza en **dos tracks que no deben conflarse**, porque responden preguntas que un solo número no separa. Es la contraparte empírica del resultado más agudo del piloto: la brecha entre lo que una familia *encuentra* y lo que *existe*.

> **EXISTENCIA DE ESTRUCTURA COMPRIMIBLE ≠ CAPACIDAD DE UNA FAMILIA DE MODELOS PARA DESCUBRIRLA.**

**Track A — known-physics benchmark.** *¿Cuánto costo descriptivo pueden absorber regularidades físicas conocidas?*
Mide **existencia y magnitud** de compresión conocida sobre datos experimentales independientes de esas leyes. **La familia SÍ puede contener explícitamente** la fórmula de Rydberg, modelos físicos conocidos apropiados y otras regularidades cuya comprimibilidad se quiera medir.
**Condición crítica, sin la cual el track es nulo:** el dataset no puede haber sido construido, calibrado ni ajustado utilizando la misma estructura que se evalúa (§4.2). Longitudes de onda medidas: admisibles. Niveles de energía ajustados con un modelo de niveles, y probabilidades de transición calculadas a partir de él: clase 4, solo control.
**Reporta:** ρ_MDL; η_ε; g_pred; g_total; escalamiento con n; robustez frente a U_ref; surrogates.

**Track B — blind discovery.** *¿Puede una familia genérica descubrir la compresión?*
Mide si la estructura que Track A muestra que existe puede ser **hallada** por una familia que no la recibió. **No puede recibir como primitivas ni como bibliotecas contabilizadas:** fórmula de Rydberg, parametrización de defecto cuántico, estructura de niveles, tablas físicas equivalentes. **Puede incluir:** regresión simbólica, familias algebraicas genéricas, búsqueda estructural, métodos genéricos previamente registrados. **Toda estructura descubierta paga su longitud de descripción en su totalidad.**
**Lectura obligatoria de un resultado de Track B:** un ρ_MDL alto **no demuestra que los espectros sean incomprimibles**; demuestra que la familia declarada no encontró la estructura. Igual que en el piloto un r_generic ≈ 1 (Regla 30, PCG64) convivió con generadores de pocos cientos de bits, **un ratio cercano a 1 nunca certifica incompresibilidad**.

La cantidad de interés es la **distancia entre ambos tracks**: el análogo empírico de la brecha del oráculo.

**11.2 Sistemas físicos estocásticos.** El CMB se trata como dominio físico estocástico estructurado, **no** como ruido, y **nunca** como primera medición. La comparación debe separar señal cosmológica, ruido instrumental, máscaras, efectos de selección y productos procesados.

**11.3 Biología.** Secuencias genómicas, regiones codificantes y no codificantes por separado, series de expresión y otros corpus con estructura definida, respetando el nivel descriptivo.

**11.4 Meteorología u otros sistemas complejos.** Series con resolución temporal y espacial conocidas, pipeline documentado y partición temporal válida para test fuera de muestra.

## 12. Escalamiento en tamaño y diversidad

Corpus anidados D₁ ⊂ D₂ ⊂ … ⊂ D_n. El aumento de n debe incorporar **mayor diversidad**, no solo más muestras redundantes. Se analiza C(d,U;D_n,ε) como función conjunta de n, ε y diversidad. **No se supone de antemano una ley de potencia:** el objeto experimental es la curva o superficie de escalamiento descriptivo.

## 13. Métricas primarias

**13.1 Costo descriptivo.** C(d,U; D_n, ε) = min sobre T∈M [L_U(T) + L_U(D_n,ε | T)].

**13.2 Razón descriptiva, con baseline completo.**

> **ρ(d,ε,U;D_n) = C(d,U;D_n,ε) / L₀_full**,  con **L₀_full = L_U(M₀) + L_U(D_n,ε | M₀)**

Como M₀ ∈ M, se cumple **ρ ≤ 1** por construcción; **ρ = 1 cuando la descripción nula es óptima, posiblemente empatada con otro modelo** de igual costo total. Normalizar por el residuo desnudo daría solo ρ ≤ 1 + L_U(M₀)/L_U(D_ε|M₀) > 1, porque cobraría el modelo en el numerador sin acreditar M₀ en el denominador. **No se interpreta el límite ε → 0 de ρ de manera aislada.**

**13.3 Tres columnas obligatorias (Enmienda 5).** Todo reporte separa:
- **r_generic** — ratio bruto del mejor compresor genérico. **Puede superar 1** por overhead de cabecera.
- **ρ_oracle** — razón con generador conocido. **Solo controles sintéticos.** Cota de existencia: mide "existe descripción corta", no "nuestra familia la encuentra".
- **ρ_MDL** — mínimo efectivo sobre la familia pre-registrada, **incluyendo M₀** y los costos de identificación de clase y de modelo. Con L₀_full, **≤ 1** por construcción. En dominios empíricos no hay oráculo: solo existe ρ_MDL, y es **permanentemente cota superior**. **Ningún ρ_MDL alto puede leerse como veredicto de incompresibilidad.**

**13.4 Pendiente de resolución.** s_C(n,ε) = ∂C/∂log₂(1/ε); s₀(n,ε) = ∂L₀/∂log₂(1/ε); **η_ε(n) = s_C/s₀**, estimada por diferencias finitas entre resoluciones pre-registradas. η_ε ≈ 1: cada bit de precisión se paga casi literalmente. η_ε ≪ 1: la estructura reutilizable absorbe gran parte del refinamiento.

*Enmienda 3 (alcance):* **η_ε se define solo para variables continuas.** Para sistemas discretos no existe un ε → 0 físico comparable: se estudia por separado el escalamiento con tamaño, horizonte temporal y granularidad de representación, **sin identificar esas variables con ε**.

**13.5 Generalización fuera de muestra: dos razones con baselines simétricos (incorporación formal).** Antes de entrenar o seleccionar se congela D = D_train ∪ D_test. No se modifica estructura, hiperparámetros, biblioteca, cuantizador, métrica ni representación después de consultar D_test.

> **g_pred(T) = L_U(D_test,ε | T_train) / L_U(D_test,ε | M₀)**
> *«Conocido el modelo entrenado, ¿con qué eficiencia codifica datos no vistos?»*
>
> **g_total(T) = [ L_U(T_train) + L_U(D_test,ε | T_train) ] / [ L_U(M₀) + L_U(D_test,ε | M₀) ]**
> *«¿Amortiza el modelo su propio costo de descripción sobre el bloque de test?»*

Lecturas: g_pred ≪ 1, fuerte compresión predictiva; g_pred = 0, el modelo reproduce el test exactamente; g_pred ≈ 1, sin generalización útil; **g_pred > 1, el modelo predice peor que el baseline**. Y separadamente: **g_total > 1, modelo + test cuestan más que modelo nulo + test**.

**Identidad exacta de la diferencia.** Con las abreviaturas

> **A = L_U(T_train) ; B = L_U(M₀) ; G = L_U(D_test,ε | T_train) ; H = L_U(D_test,ε | M₀)**
>
> g_pred = G/H ;  g_total = (A+G)/(B+H)

se cumple

> **g_total − g_pred = (A − B·g_pred) / (B + H) = (A·H − B·G) / [H·(B + H)]**

y de ahí las tres reglas de lectura:

1. **No existe desigualdad general entre g_total y g_pred.** Tienen denominadores distintos: g_total > g_pred **no se sigue** y no debe afirmarse.
2. **El signo de la diferencia es el signo de A − B·g_pred.** Positivo cuando la descripción del modelo entrenado supera a la del modelo nulo escalada por la razón predictiva; negativo en caso contrario. Ninguna dirección es universal.
3. **La reducción a A/(B + H) vale únicamente en el caso especial g_pred = 0.** Usarla con g_pred > 0 sobreestima la diferencia en B·g_pred/(B + H).

**Convergencia, con sus condiciones explícitas.** Si A y B permanecen fijos y g_pred permanece acotado, al crecer el bloque de test H → ∞ y por tanto

> **g_total − g_pred → 0**

porque los costos fijos de descripción se amortizan sobre más datos. **No se afirma que el límite se alcance "desde arriba"** ni por ningún lado en particular, ni que g_total > g_pred sea necesario.

Lo que sí ocurre, y es relevante: un modelo puede presentar **g_pred ≪ 1 y g_total > 1 simultáneamente** si el bloque de test es demasiado pequeño para amortizar L_U(T_train). Eso es una propiedad del bloque, no un fallo de predicción.

*Nomenclatura histórica, conservada:* los scripts originales del piloto calculan **g_total^bare = [L_U(T_train) + L_U(D_test|T_train)] / L_U(D_test|M₀)**, asimétrica. Los valores históricos (0.0088; 1.009; 1.0088) son g_total^bare y **no deben reinterpretarse** como g_total. Desde 2026-08-26 la g_total simétrica **sí está calculada** (`src/contabilidad_completa.py`), con L_U(M₀) = 3 bits según §7: para Reglas 110 y 30 da 0.0088 y para el ruido con semilla 1.0088, y ambas columnas se publican juntas. Que coincidan a cuatro decimales es consecuencia de que 3 bits son despreciables frente a un bloque de test de 92 160, **no** de que sean la misma cantidad.

## 14. Robustez

Todo resultado principal se repite bajo: más de una pila U_ref; distintas resoluciones pre-registradas; métricas alternativas científicamente defendibles; distintos tamaños n; distintas particiones train/test; controles surrogate; modelos nulos alternativos previamente declarados. **No se exige igualdad numérica entre codificaciones: se exige estabilidad cualitativa de las separaciones relevantes.**

## 15. Criterio primario de éxito

No se declara éxito porque una sola métrica resulte pequeña. La evidencia a favor de comprimibilidad estructural extraordinaria requiere **conjuntamente**:

> **ρ_MDL ≪ 1,  η_ε ≪ 1,  g_pred ≪ 1**

con **g_total reportada como condición de amortización descriptiva, no como umbral**. La asimetría es deliberada: g_pred mide generalización predictiva y debe ser pequeña para que la afirmación se sostenga; g_total depende del tamaño del bloque de test, y exigirle ≪ 1 a todo tamaño penalizaría una estructura reutilizable correcta por haber sido evaluada sobre una muestra chica. Lo que se le exige a g_total es una **predicción de escalamiento**: si la estructura es genuinamente reutilizable, al crecer el bloque de test o n,

> **g_total − g_pred → 0**

bajo las condiciones explícitas de §13.5: A = L_U(T_train) y B = L_U(M₀) fijos y g_pred acotado, de modo que al crecer H los costos fijos se amortizan. **No se afirma que el límite se alcance "desde arriba"** ni por ningún lado en particular: por la identidad g_total − g_pred = (A − B·g_pred)/(B + H), el signo depende de A − B·g_pred y no está fijado en general. En el piloto la diferencia es positiva porque A = 811 bits supera a B = 3 bits, pero **no vale el mismo número en los tres controles**: 811/92 163 = 0.0087996 para las Reglas 110 y 30, donde g_pred = 0 exacto, y (A − B·g_pred)/(B + H) ≈ 808/92 163 = 0.0087671 para el ruido, donde g_pred ≈ 1. Ambas redondean a 0.0088 y ninguna cifra publicada cambia. Una g_total que se mantiene plana, o cuya distancia a g_pred no se reduce al crecer el test, indica un modelo cuya descripción crece con los datos que explica: firma de ajuste, no de compresión, y se reporta como tal.

Además, la ventaja debe: (1) persistir al aumentar n; (2) persistir al aumentar la resolución dentro del régimen estudiado; (3) sobrevivir en D_test; (4) disminuir significativamente en surrogates; (5) sobrevivir a distintas pilas U_ref; (6) no explicarse por contaminación teórica del pipeline; (7) compararse entre dominios solo a niveles descriptivos equiparables.

## 16. Resultados que falsarían o debilitarían la hipótesis

- ρ_MDL converge sistemáticamente hacia valores próximos a 1;
- la ventaja desaparece fuera de muestra (g_pred ≈ 1);
- g_total no se aproxima a g_pred al crecer el bloque de test;
- cambia radicalmente al modificar U_ref;
- no existe diferencia entre datos reales y sus surrogates;
- la aparente ventaja de la física desaparece al igualar niveles descriptivos;
- la ventaja se explica por procesamiento previo del dataset;
- el refinamiento en ε obliga al modelo a pagar prácticamente todos los bits adicionales (η_ε ≈ 1);
- otros dominios muestran curvas indistinguibles de la física fundamental.

**Un resultado negativo forma parte del programa y se publica igual.** Nótese que **un ρ_MDL alto en Track B no está en esta lista**: no falsa nada, por §11.1.

## 17. Trazabilidad obligatoria (Enmienda 6a)

**Todo número publicado en un informe del programa —tabla, texto o adenda— debe ser generado por un script versionado en `/src`, con su salida archivada en `/results`**, de modo que ejecutar el script reproduzca el número a la precisión reportada. Corolarios:

1. Ninguna constante derivada (longitud de código fuente comprimido, costo de un checkpoint, horizonte de re-sincronización) se cablea a mano en un segundo script: se recalcula o se lee de la salida archivada del script que la produjo, con referencia explícita.
2. Un número derivado por cálculo manual a partir de salidas archivadas (una pendiente, un promedio, un subtotal) **no es citable** hasta que un script lo imprima.
3. Si un número publicado no puede regenerarse, el informe lo declara en una sección de erratas, con el valor viejo visible, el valor nuevo y el script que lo produce. **Nada se reescribe silenciosamente.**
4. Los tiempos de cómputo impresos por los scripts no son mediciones y no se comparan.

## 18. Revisión humana experta obligatoria

El marco y este protocolo fueron desarrollados mediante rondas de crítica cruzada entre múltiples sistemas de IA con supervisión humana. Ese proceso da robustez frente a los errores **no compartidos** entre los sistemas; ninguna frente a los sesgos que comparten por construcción (corpus solapados, convenciones de formalización similares).

> **Antes del primer dataset empírico con pretensión publicable, este protocolo debe pasar por al menos un revisor humano experto en MDL/teoría de la información algorítmica y uno en el dominio físico elegido.**

Es la aplicación al propio método de trabajo de la frontera que el marco llama R_observabilidad: la crítica interna no puede medir el punto ciego común de quienes la ejercen.

## 19. Regla de desviaciones posterior al congelamiento

Desde el momento del congelamiento (hash + fecha + tag + depósito), **nada de lo hallado durante §11 modifica esta versión**. Todo hallazgo que entre en conflicto con el protocolo se registra como **desviación documentada**, o motiva una **v1.2 explícita** con su propio changelog. Toda modificación posterior a §11 debe tratarse como potencialmente adaptativa a resultados y documentarse como tal.

## 20. Resultado experimental principal y alcance de la conclusión

El producto del experimento no es un ranking simple sino una familia de superficies 𝒞(dominio, nivel, n, ε, U_ref) con sus ρ, η_ε, g_pred y g_total.

Pregunta de salida: ¿qué fracción del contenido informativo de cada estrato puede trasladarse desde observaciones particulares hacia reglas reutilizables capaces de generalizar?

**Alcance permanente:** incluso un resultado positivo **no demostraría** que el universo completo posea baja complejidad de Kolmogórov. Demostraría algo más acotado: que dentro de los dominios, escalas y resoluciones estudiados, cantidades crecientes de información observacional pueden ser reemplazadas por estructuras descriptivas reutilizables cuyo costo crece mucho más lentamente que el de los datos que explican, y que esa ventaja generaliza fuera de muestra.

---

## Anexo A — Deudas abiertas al momento de preparar el congelamiento

Ninguna bloquea el congelamiento; todas deben estar visibles en él.

1. ~~**L_U(M₀) sin definir**~~ — **CERRADA (2026-08-26):** `protocol/definicion-L-M0.md`, incorporada por referencia en §7. Falta **instanciar la familia de primer nivel de cada dominio empírico** en su propio pre-registro.
2. ~~**Recalcular ρ con L₀_full**~~ — **CERRADA:** `src/contabilidad_completa.py` → `results/contabilidad-completa-salida.txt`; ninguna fila cambia a cuatro decimales; ρ_full ≤ 1 verificado.
3. ~~**Imprimir g_pred y g_total desde script**~~ — **CERRADA:** g_pred en `src/g_metricas_oos.py`; g_total simétrica en `src/contabilidad_completa.py`, con g_total^bare conservada como columna histórica.
4. **Pilas U_ref verdaderas** (§6): dos convenciones completas e independientes, aún no implementadas.
5. **Política de amortización de bibliotecas** compartidas entre dominios (§6).
6. **Regla de precisión identificable** para parámetros continuos en familias no regulares (§5.2).
7. ~~**Subtotales por nivel impresos por script**~~ — **CERRADA:** `src/contabilidad_completa.py` imprime identificador, Nivel A (1288 bits), Nivel B (156·⌈n/h⌉) y total, con su escalamiento en n.
8. **Discrepancia de pendiente en Lorenz** sin causa asignada: 64.2 promedio de tramos (rango 29–98), 67.6 por ajuste, contra 76.5 predicho. Se reporta, no se corrige.
9. **Revisión humana experta** (§18), pendiente.
10. **Congelamiento y depósito**: PDF, SHA-256, tag, OSF.

---

*Historia: protocolo v1.0 (docx del investigador) → Enmiendas 1–5 (`changelog-v1-0-a-v1-1.md`, surgidas del piloto §10.1) → Enmienda 6 (`enmienda-6.md`, surgida de la verificación de herencia, no de resultados) → **v1.1 consolidada, 2026-08-26**, que además incorpora formalmente: baseline completo L₀_full (§7, §13.2), h(p, ε) (§5.4), g_pred / g_total simétricas (§13.5), diseño en dos tracks para §11.1, criterio de éxito con g_total como predicción de escalamiento (§15). Consolidación redactada por el asistente de IA bajo supervisión de Maximiliano Winter. **Los documentos fuente no fueron modificados.** Estado: preparada para congelamiento; NO congelada. — **2026-08-26 (tercera incorporación pre-congelamiento, auditoría final):** §13.5 incorpora la **identidad exacta g_total − g_pred = (A − B·g_pred)/(B + H) = (A·H − B·G)/[H·(B + H)]** con sus tres reglas de lectura y la convergencia condicionada; §15 corregido en consecuencia (la diferencia **no** vale lo mismo en los tres controles); §7 añade la advertencia de que L_U(M₀) = 3 bits es consecuencia de convenciones pre-declaradas y no un valor canónico, y remite a `contabilidad_completa_v2.py`. Ninguna cifra experimental cambió. — **2026-08-26 (segunda incorporación pre-congelamiento):** `definicion-L-M0.md` incorporada por referencia en §7; deudas 1, 2, 3 y 7 del Anexo A cerradas; §13.5 y §15 ajustados en consecuencia (g_total simétrica calculada; retirada la expresión "desde arriba"). **STATUS sin cambios: NOT YET FROZEN OR PREREGISTERED.** No se calculó hash, no se etiquetó Git, no se depositó nada.*

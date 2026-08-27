# La intriga, en dos programas

## Versión 5

**La pregunta central, en su forma más limpia tras siete rondas de auditoría:**

> **¿Por qué el costo descriptivo de las regularidades físicas crece tan lentamente frente a la cantidad de mundo que explican?**

Esta versión no depende de Koide, del paisaje, de Penrose, de la unitariedad, ni de que el universo completo sea comprimible. Es el fenómeno empírico que todas las demás capas intentan explicar — y tiene forma de exponente de escalamiento: cómo crece K(T) cuando la cantidad y la resolución de los datos explotan. Los exponentes se miden.

**Arquitectura (nueva en v5):** el documento contenía dos programas mezclados. Se separan. **II presupone I; I no presupone II**; y los resultados de I acotan a II, porque cualquier descripción de la historia completa debe contener las regularidades compresivas como caso particular.

---

# Programa I — Compresibilidad de las regularidades
### (empírico, atacable, con MDL y generalización)

## El núcleo que resiste

> Existen descripciones relativamente cortas que comprimen grandes conjuntos de regularidades físicas, **y algunas han permitido anticipar fenómenos no utilizados en su construcción.**

Esto no requiere afirmar que conocemos el estado completo del universo, que las condiciones iniciales son simples, que todos los parámetros son reducibles, que la realidad es matemática, ni que conocemos K(universo). Ninguna hipótesis posterior tiene este estatus.

## La función de compresión, con resolución

Los datos físicos no tienen longitud informativa independiente de la resolución: x = 1.234±0.001 contiene más información que x = 1.2±0.5; "galaxia espiral" cuesta pocos bits, la posición de cada átomo costaría una cantidad gigantesca. Por eso la variable de escala ε es parte de la función, no un detalle:

> **C(D, ε) = min sobre T de [ K(T) + L(D_ε|T) ]**

con la regla contable general (MDL, Rissanen 1978): solo hay compresión real si **ΔC < 0** comparando modelo+residuo contra modelo+residuo — menos parámetros no es mejor explicación si la maquinaria nueva cuesta más de lo que ahorra.

**La pregunta operativa de I:** cómo escala la descripción óptima cuando aumentan simultáneamente cantidad y resolución de los datos. Si |D_ε| se vuelve enorme y K(T) crece muy lentamente, esa pendiente es la señal cuantificable de comprimibilidad extraordinaria.

## Generalización: el criterio fuera de muestra

Junto a la compresión, la segunda función: **G(T) = K(D_nuevo|T)**. Una teoría físicamente interesante hace pequeñas las dos. El protocolo ideal D = D_train + D_test es artificial: la ciencia real ajusta, reinterpreta y agrega parámetros después de las primeras formulaciones. Los casos históricos son **aproximaciones particularmente claras al criterio**, no corridas literales del protocolo: el positrón es un caso muy fuerte; el Higgs lo es respecto de la existencia del mecanismo y del campo, **no de su masa, que el Modelo Estándar no predijo** (quedó como parámetro libre hasta medirla — la única "predicción" de ese número fue el caso condicionado de Shaposhnikov-Wetterich).

**El respaldo teórico, en sus dos preguntas separadas.** El teorema de completitud de Solomonoff da convergencia del predictor universal para fuentes computables, bajo sus condiciones. Eso deja dos intrigas de rango distinto: *¿por qué las regularidades físicas parecen computables?* y — la del programa — *¿por qué parecen computables por programas tan cortos?* Un mundo computable pero de K(fuente) enorme sería aprendible en principio e inabordable en la práctica. No vivimos en ese.

## La estratigrafía de la comprimibilidad (operacionaliza el viejo supuesto 1)

El "censo de lo no matematizable" era un eje mal elegido. El eje operacional es **grado de compresibilidad por dominio**, a resolución declarada:

> **ρ_ε(D) = [L(T) + L(D_ε|T)] / L(D_ε)**

Conjetura de trabajo: física fundamental ρ≪1; meteorología mayor; biología histórica mayor; biografías concretas quizás mucho mayor; ruido ρ≈1. No hace falta K exacta: las comparaciones aproximadas con compresores reales son práctica establecida (distancia de compresión normalizada, Cilibrasi-Vitányi). **La pregunta empírica:** ¿la capacidad de compresión está distribuida uniformemente por la realidad, o existen estratos de comprimibilidad? Esto convierte una cuestión filosófica de demarcación en una curva medible.

---

# Programa II — Compresibilidad de la historia completa
### (fundacional: estado inicial, contingencia, unitariedad, U, observabilidad)

## La función objetivo de II

> **min sobre T de [ K(T) + K(S₀|T) + K(C|T,S₀) + K(D|T,S₀,C) ]**

donde S₀ es la condición inicial y C la contingencia fundamental que hiciera falta; el último término (o −log P(D|·) para datos ruidosos) es lo que separa "compatible con los datos" de "los comprime". **Advertencia de alcance permanente:** D son mediciones (D_medido, no D_ideal — realidad → observables → mediciones, con aparatos, selección, resolución y ruido), de modo que esta función busca *la descripción corta que explica nuestros datos*, no automáticamente *el programa mínimo que genera el universo real*: la diferencia es exactamente el supuesto 8, y "mínima" es objetivo ideal — K es incomputable, aproximable solo desde arriba, y una cota K(x) < 10⁶ nunca dice si el mínimo es 10⁶ o 100.

## El residuo: cinco fuentes, tres niveles

**Nivel 1 — bits del objeto:** R_libres (parámetros sin derivar; nombre neutro deliberado: "ley" prejuzgaría el veredicto), R_estado, R_contingencia. La contabilidad es relativa a T, y la migración de bits entre cuentas al cambiar de teoría muestra que **nuestras categorías actuales no son fundamentales** — no que no existan categorías fundamentales: la migración audita el mapa, no legisla el territorio.
**Nivel 2 — límite del acceso:** R_observabilidad, la brecha entre lo que D acota y lo que U es.
**Nivel 3 — convención de la medida:** R_lenguaje, la máquina de referencia que fija la moneda.
Debajo de todo, el suelo ontológico: qué objeto matemático es U (supuesto 9).

Cada teoría nueva vacía R_libres en tres direcciones: bits que migran a K(T) como ley derivada, bits que migran a R_estado como domicilio, y lo que no migra nunca — el candidato a hecho bruto, con dirección contable. La partición ley/domicilio/bruto sigue siendo **conjetura interna** de esta cuenta, sin testigos estrella (retirados en v4: Weinberg 1987 fue cota que sobreestimaba ~10×, con la predicción del valor recién en Martel-Shapiro-Weinberg 1998; Shaposhnikov-Wetterich fue condicional).

**Estado experimental de R_contingencia:** la versión sin parámetro libre de Diósi-Penrose está descartada (Donadi et al., *Nature Physics* 17, 74, 2021); sobreviven las versiones con R₀ libre (~6 órdenes de brecha; Figurato et al. 2024); para CSL, gran parte del espacio (λ, r_C) excluido (Majorana Demonstrator, *PRL* 129, 080401, 2022; XENONnT, *PRL* 136, 120201, 2026; revisión: Carlesso et al., *Nature Physics* 18, 243, 2022). Nota de inferencia: cada exclusión reduce el espacio de mecanismos *especificados* compatibles con R_contingencia > 0; no aumenta la probabilidad de la unitariedad, que exigiría una previa sobre un espacio no enumerado.

## Historia como ejecución (rebajado a candidatura)

Bajo dinámica determinista computable, K(S_t) ≲ K(S₀) + K(L) + K(t) + c: la evolución no necesita introducir complejidad algorítmica comparable a la que la historia aparenta. **La profundidad lógica de Bennett (1988) es una candidata natural para caracterizar parte de la complejidad histórica acumulada** — tiempo de cómputo desde descripciones cortas, relativa a un nivel de significación, con su slow growth law — pero su aplicación al universo es interpretación especulativa, no consecuencia matemática. El estado inicial: su baja entropía está *fuertemente inferida* (no observada directamente; el CMB muestra homogeneidad, leerla como baja entropía gravitacional requiere interpretación y no hay definición aceptada de entropía gravitacional); su simplicidad algorítmica es hipótesis con carga de prueba propia.

---

## Niveles de solidez (evaluación global tras siete rondas)

| Nivel | Contenido |
|---|---|
| **Muy sólido** | Las regularidades físicas poseen descripciones cortas con poder predictivo; MDL como formalización legítima de teoría-contra-residuo |
| **Sólido con condiciones** | La cota sobre K(S_t) bajo dinámica determinista computable; convergencia de Solomonoff para fuentes computables |
| **Hipótesis productivas** | Profundidad lógica cosmológica; simplicidad del estado inicial; partición de parámetros entre estructura y estado; contingencia física fundamental |
| **Frontera filosófico-física** | Si U tiene representación canónica; si K(D) permite inferir algo sobre K(U); si la comprimibilidad observada pertenece al mundo o a la representación |

## Los nueve supuestos, reasignados

| # | Supuesto | Programa | Estado |
|---|---|---|---|
| 1 | Comprimibilidad del mundo, no del recorte | I | Operacionalizado como estratigrafía ρ_ε |
| 2 | Ley/estado/parámetro categorías reales | II | Abierto; la migración audita el mapa |
| 3A | Reducción teórica del residuo | II | Activo (Koide como problema de escala: 10⁻⁵ con masas polo, ~10⁻³ con corridas; Sumino 2009) |
| 3B | Incompresibilidad algorítmica de los valores | II | Casi inatacable en directo; vía práctica: 3A |
| 4 | Baja entropía = simplicidad algorítmica | II | Hipótesis, formal y física |
| 5 | Unitariedad (despliega vs. genera) | II | El más vivo experimentalmente |
| 6 | El compresor no contamina | I | Formalizado como criterio fuera de muestra |
| 7 | Longitud mínima significativa | I y II | Contabilidad total + separación de escalas |
| 8 | K(D) pequeño ⇒ K(U) pequeño | II | Límite de inferencia; frontera |
| 9 | U es objeto definible | II | Suelo ontológico; frontera |

## Lo que sigue

Programa I tiene un experimento listo para correr sin acelerador ni telescopio: la estratigrafía ρ_ε con compresores reales sobre corpus de dominios distintos, y la medición del exponente de escalamiento de K(T) contra |D_ε|. Programa II espera: una relación explicada (3A), el cierre o la detección en colapso (5), la contabilidad de la biblioteca (7), las masas de neutrinos, Hyper-Kamiokande.

---

*Historia: v1 (seis supuestos) → v2 (siete; costo del lenguaje) → v3 (nueve; Bennett; partición) → v4 (auditoría externa con fuentes primarias; cinco cuentas) → v4.1 (taxonomía de tres niveles; inferencia de colapso corregida) → v4.2 (R_libres; MDL como regla general; función objetivo) → v4.3 (término de datos; familia-MDL; fuera de muestra; triangulación) → v5 (séptima ronda: el programa partido en I y II; resolución ε y estratigrafía ρ_ε; pregunta central como exponente de escalamiento; rebajas: Higgs sin masa predicha, Bennett como candidata, migración como auditoría del mapa, Solomonoff en dos preguntas).*

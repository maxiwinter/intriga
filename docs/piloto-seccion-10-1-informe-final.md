# Piloto §10.1 — Validación del instrumento
## Programa I — Protocolo v1.1
### Informe final del piloto sintético

**Alcance declarado (§10.1 del protocolo):** los controles validan el instrumento, no dicen nada sobre la naturaleza. Todos los datasets fueron generados por el propio ejecutor, de modo que la "contaminación teórica" es total y deliberada: el modelo generativo *es* el generador. Eso es exactamente lo que un control positivo debe ser.

**Setup (declarado antes de correr):** semillas fijas (42, 7); Lorenz σ=10, ρ=28, β=8/3, RK4, dt=0.01, 20.000 pasos, cuantización 8 bits/coordenada sobre rangos [-25,25]×[-30,30]×[0,55]; autómatas de 256 celdas × 400 pasos, frontera periódica; PRNG PCG64; ruido de os.urandom. Modelo nulo: codificación literal. Familia genérica: {zlib, bz2, lzma} — tres codificadores competidores dentro de una misma metaclase, no dos pilas U_ref; la selección del mejor paga log₂3 ≈ 1.6 bits, incluidos en ρ_MDL. Las pilas U_ref verdaderas (convenciones completas e independientes de codificación) quedan pendientes para la etapa empírica. Modelos generativos de dos partes: código fuente comprimido + parámetros + condición inicial a precisión p. **Predicción pre-registrada:** el exponente de Lyapunov de Lorenz (λ≈0.906) predice ~76 pasos de fidelidad-ε comprados por cada bit adicional de condición inicial.

## Resultados

Tres columnas distintas que la contabilidad exige separar: **r_generic** (ratio del mejor compresor genérico; puede superar 1 por overhead de cabecera), **ρ_oracle** (cota generativa *conocida*: el generador y su semilla están disponibles porque los datos son sintéticos — mide "existe descripción corta", no "nuestra familia la encuentra"), y **ρ_MDL** (mínimo efectivo sobre la familia incluyendo el modelo nulo M₀ y el costo de selección; por construcción ρ_MDL ≤ 1).

| Dominio | L₀ (bits) | r_generic | ρ_oracle | ρ_MDL |
|---|---|---|---|---|
| Lorenz (20k pasos, con checkpoints)† | 480.000 | 0.53 | **0.0053** | 0.0053 |
| Regla 110 | 102.400 | 0.50 | **0.0107** | 0.0107 |
| Regla 30 | 102.400 | 1.0009 | **0.0107** | 0.0107 |
| PRNG (PCG64) | 262.144 | 1.0005 | **0.0018** | 0.0018 |
| Ruido (urandom) | 262.144 | 1.0005 | — | **1** (gana M₀) |
| Surrogate R110 (bits permutados) | 102.400 | 0.9945 | — | 0.9945 |
| Surrogate Lorenz (bytes permutados) | 480.000 | 0.9261 | — | 0.9261 |

† Valor confirmado por script el 2026-08-26 (Errata 1). Nota: en los controles sintéticos ρ_MDL ≃ ρ_oracle (no igualdad exacta: la contabilidad estricta incluye L(identificador del modelo ganador) — qué generador de la familia se usa — además del log₂3 de la metaclase de compresores; el efecto desaparece en el redondeo de la tabla) porque la familia contenía al generador — privilegio de laboratorio que ningún dominio empírico va a conceder; allí solo tendremos ρ_MDL y la advertencia permanente de que es cota superior.

**Generalización fuera de muestra (regla inferida de 40 filas, congelada, testeada en 360):** Regla 110 → regla recuperada exactamente, 0.0% error en test, g = 0.0088. Regla 30 → ídem, g = 0.0088. Ruido tratado como autómata → "regla" espuria (~~166~~ — identificador dependiente de corrida, no se cita; Errata 2), ~~50.01%~~ ≈50 % error en test, **g = 1.009 > 1** (el modelo empeora al baseline: paga su propio costo sin comprar nada).

**Pendiente de Lyapunov medida:** 66 pasos por bit de condición inicial (predicción: ~76; mismo orden, ver desviación abajo).

## Lo que el instrumento demostró saber hacer

1. **Detecta estratos (H5).** Cuatro niveles limpiamente separados: generador conocido (ρ ~ 0.002–0.01), estructura visible a compresor genérico (ρ ~ 0.5), estructura invisible al genérico pero con generador corto (Regla 30, PRNG: ρ_genérico ≈ 1, ρ_generativo ≈ 0.002–0.01), y ruido verdadero (ρ ≈ 1 en todo).
2. **La brecha Regla-30/PRNG es el resultado conceptual clave del piloto:** "incompresible para gzip" no es "incompresible" — la distancia entre r_generic ≈ 1.0 y ρ_oracle ≈ 0.002–0.01 es la distancia entre *lo que nuestra familia de modelos encuentra* y *lo que existe*. Es una demostración operacional de la dependencia respecto de la familia de modelos — el problema que la incomputabilidad de K vuelve inevitable (ilustra el problema; no es una demostración experimental del teorema de Chaitin): el fracaso del compresor nunca certifica incompresibilidad. En datos reales no habrá oráculo, y esta brecha es la razón por la que ningún ρ_MDL alto podrá leerse como veredicto de incompresibilidad.
3. **Los surrogates colapsan (H4).** Permutar bits de la Regla 110 lleva ρ de 0.50/0.0107 a 0.99: la ventaja medía estructura, no marginales. (El surrogate de Lorenz retiene ρ=0.93 porque la permutación de bytes preserva el histograma no uniforme — compresión de marginales, exactamente lo que el control debe aislar.)
4. **La generalización discrimina (H2).** Regla exacta recuperada de 40 filas y sostenida 360 filas fuera de muestra con g≈0.009; sobre ruido, el procedimiento no se engaña: g>1.
5. **La métrica recuperó empíricamente la escala de predictibilidad asociada al exponente de Lyapunov.** 66 pasos/bit medidos contra ~76 predichos (λ/ln2 ≈ 1.307 bits por unidad de tiempo → ln2/λ ≈ 0.765 u.t./bit → ~76.5 pasos/bit con dt=0.01). La discrepancia del ~13% se reporta sin corregir; causas candidatas, ninguna verificada: piso de precisión float64 de la referencia, exponentes de Lyapunov de tiempo finito, umbral de divergencia elegido, cuantización, timestep, error del integrador RK4 y orientación inicial respecto de las variedades inestables.

## Las dos lecciones que van más allá de la validación

**La desviación honesta:** la predicción de 76 pasos/bit falló por ~13%, y las longitudes de coincidencia saturan en ~2.655 pasos aun con 52 bits/dimensión. Causa: la referencia misma vive en float64 — el instrumento chocó contra el piso de ruido de su propia aritmética. Lección para el protocolo: la pila U_ref no solo fija el lenguaje; fija también el piso de precisión contra el cual toda fidelidad se mide. En datos reales, ese piso es el instrumento de medición.

**Costo operacional del caos (nivel A vs. nivel B, medido — interpretación corregida en v1.1):** la *regla* de Lorenz cuesta ~1.400 bits fijos (nivel A). Mantener una precisión observacional fija sobre la *trayectoria particular* (nivel B) durante un horizonte t exige especificar progresivamente más bits del estado inicial, a una tasa operacional asintótica de información requerida para seguimiento a resolución fija que, bajo las condiciones en que resulta aplicable la relación de Pesin, es h_KS = (1/ln2)·Σλᵢ⁺ bits por unidad de tiempo — la suma de los exponentes positivos, no en general solo el mayor; la relación con la entropía de Kolmogorov-Sinai está condicionada por propiedades de la dinámica y de la medida invariante, no es identidad universal. Para Lorenz, con un exponente positivo dominante, ~0.906/ln2 ≈ 1.3 bits/u.t. es la predicción correcta del piloto. El codificador ingenuo sin re-sincronización degenera (ρ sube a 0.87 en 20k pasos); el codificador con checkpoints lo corrige (0.0053).

**Este crecimiento no implica creación de información fundamental.** Bajo dinámica determinista computable, K(S_t) ≲ K(S₀) + K(L) + K(t) + O(1): si S₀ y la ley se conocen exactamente, no aparecen bits nuevos. Lo que crece es la *precisión de S₀ que debe resolverse* para localizar una trayectoria a resolución finita durante un horizonte creciente. El caos no acuña bits: los **bombea** — transfiere microdetalle no resuelto del estado inicial hacia el flujo observacional, a tasa medible. Para el Programa II: **no crece R_estado; crece la precisión de R_estado que necesitamos resolver**, y esos bits revelados aparecen en la contabilidad como K(D|T,S₀), no como creación dinámica — consistente con el enrutamiento ontológico de la tabla de resultados cuánticos del marco (v5.2, §12.1).

## Lo que este piloto NO muestra

Nada sobre la naturaleza. Los datasets son sintéticos y auto-contaminados por diseño; los compresores genéricos son aproximaciones groseras de K; la familia generativa contenía al generador verdadero, lujo que ningún dominio empírico va a conceder. El piloto valida que las métricas ρ, g y la pendiente de resolución se comportan como el protocolo exige cuando la verdad es conocida. La siguiente etapa es §11.1: datos empíricos con cadena de procesamiento documentada — espectros atómicos experimentales contra el modelo nulo y contra familias que no contienen la respuesta de antemano.

*Corrida original ejecutada conforme a §10.1 del Protocolo v1.0. Las correcciones y verificaciones posteriores fueron realizadas conforme a las enmiendas documentadas, antes de cualquier dataset empírico. Código y semillas declarados arriba; corrida única, sin selección posterior de resultados.*

---

## Adenda final de verificación — Protocolo v1.1 (Enmiendas 1 y 3 ejecutadas)

**Verificación del piso float64 (desplazamiento con precisión extendida).** Referencia recomputada en aritmética de 160 bits (mpmath), mismo integrador y cuantización: las longitudes de coincidencia dejan de saturar — p=52: 3052 pasos (vs. 2655 con referencia float64), p=64: 4228, p=76: 5011, todas crecientes y sin tope. El punto de saturación se desplazó al mejorar la aritmética: **la hipótesis del piso queda confirmada como causa de la saturación**, por el criterio pre-declarado. Nota adicional dentro del piso: con referencia float64, el horizonte queda clavado en ~2655 para cuantizaciones de 6 a 10 bits — la firma de un piso aritmético, no de la dinámica.

**Hallazgo que la verificación NO resolvió:** la pendiente en precisión extendida sigue siendo ~64 pasos/bit contra ~76 predichos (Errata 3: promedio de tramos 64.2, rango 29–98, ajuste lineal global 67.6; `src/lorenz_checkpoints.py`). El piso explicaba la saturación, no la discrepancia de pendiente, que queda **sin causa asignada** entre las candidatas restantes (exponentes de Lyapunov de tiempo finito, umbral de divergencia, cuantización, timestep, error RK4, orientación respecto de las variedades inestables) y así se reporta.

**Barrido de ε (controles continuos, conforme a la Enmienda 3 corregida).** Lorenz con codificador generativo + checkpoints, resoluciones de 4 a 12 bits/coordenada: ρ_MDL ~~entre 0.029 y 0.011~~ entre 0.027 y 0.010 (Errata 4), y **η_ε ≈ 0 a 0.005** (sin cambio) por diferencias finitas — la descripción generalizable absorbe casi todo bit nuevo de resolución. Ruido continuo uniforme: r_generic ≈ 1.0005–1.0007 en b=8 y b=16, ρ_MDL = 1 (gana M₀), **η = 1** — cada bit de resolución se paga literal. Comportamiento de η validado en ambos extremos.

**Resultado operacional central de los controles:** para el ruido, ΔC ≃ ΔL₀ al aumentar resolución; para Lorenz, ΔC ≪ ΔL₀. El instrumento ya midió, en laboratorio, la idea central del Programa I: más precisión observacional no exige proporcionalmente más descripción estructural cuando existe una regularidad generativa reutilizable. No es un resultado sobre la naturaleza (datos autogenerados, familia con oráculo); es la prueba de que el instrumento hace lo que fue construido para hacer.

**Estado formal: Programa I — instrumento validado en controles sintéticos. Protocolo v1.1 — listo para congelamiento** (fecha, hash del documento y commit del código: actos del investigador humano). **Siguiente etapa: §11.1, primera medición empírica.** A partir del congelamiento, ningún problema hallado durante §11.1 modifica v1.1: se registra como desviación del protocolo o motiva explícitamente una futura v1.2.

---

## Erratas de trazabilidad (verificación de herencia, 2026-08-26 — Enmienda 6)

La reproducción del piloto desde el repositorio ensamblado (`docs/preprint/reproduccion-2026-08-26.md`) reprodujo todas las salidas con semilla, pero encontró números de este informe que ningún script versionado generaba. La Enmienda 6 (`protocol/enmienda-6.md`) exige que todo número publicado provenga de un script en `/src` con salida en `/results`. Las erratas siguientes cierran ese requisito. Los valores viejos quedan visibles; nada se reescribe silenciosamente.

**Errata 1 — ρ_oracle de Lorenz (20 000 pasos, con checkpoints) = 0.0053: confirmado, no corregido.** El valor no lo producía ningún script (`piloto_10_1.py` imprime la fila con el codificador ingenuo, 0.5307). Ahora lo genera `src/lorenz_checkpoints.py` (`results/lorenz-checkpoints-salida.txt`): horizonte h = 2655 pasos, k = ⌈20000/2655⌉ = 8 checkpoints de 156 bits, código fuente comprimido 1096 bits, parámetros 192 bits → C = 2536 bits → **ρ = 0.0053**. Escalamiento con checkpoints: n = 1000 / 2500 / 5000 / 10 000 / 20 000 → ρ = 0.0602 / 0.0241 / 0.0133 / 0.0080 / 0.0053 (contra 0.057 / 0.024 / 0.48 / 0.74 / 0.87 del codificador ingenuo). El registro de reproducción había conjeturado que 0.0053 correspondía a 7 checkpoints; esa conjetura era errónea y se retira.

**Errata 2 — "regla espuria 166" y "50.01 % error".** ~~"regla" espuria 166, 50.01 % error en test~~. El control negativo usa `os.urandom` sin semilla: el identificador de la regla espuria y el error de test **dependen de la corrida** (informe: 166 / 50.01 %; salida archivada: 9 / 50.07 %; reproducción: 199 / 50.23 %) y no se citan como resultado. Los invariantes reportables del control son p_error ≈ 0.5 y g > 1 (g = 1.0088 en todas las corridas). Conforme a la Enmienda 6(b) se agrega la fila reproducible con ruido PRNG (PCG64, semilla 2026; `src/ruido_oos_semilla.py`, `results/ruido-oos-semilla-salida.txt`): **p_error = 0.5001, g = 1.0088**.

**Errata 3 — pendiente en precisión extendida.** ~~"~64 pasos/bit"~~ se derivaba a mano de los matches archivados. `src/lorenz_checkpoints.py` la imprime: matches p = 40 / 52 / 64 / 76 → 2699 / 3052 / 4228 / 5011 (idénticos a la Adenda); pendientes por tramo 29.4 / 98.0 / 65.2 pasos/bit; **promedio de tramos 64.2, rango 29–98; ajuste lineal global 67.6**; predicción pre-registrada ln 2/(λ·dt) = 76.5. Discrepancia −11.6 % (ajuste) a −16 % (promedio). **Sigue sin causa asignada**; se reporta, no se corrige. La no uniformidad por tramos (29–98) es en sí un dato que cualquier hipótesis causal futura debe explicar.

**Errata 4 — ρ_MDL del barrido de resolución (Adenda).** `verificacion_piso_y_eta.py` cablea `code_bits = 1252` como "gzip del fuente declarado"; el gzip del fuente declarado en `piloto_10_1.py` mide **1096 bits** (verificable en la salida archivada del codificador ingenuo: C(n = 1000) = 1360 = 1096 + 192 + 72). Con la constante trazada, los ρ_MDL del barrido a n = 5000 son ~~0.0293 / 0.0195 / 0.0146 / 0.0117 / 0.0106~~ → **0.0267 / 0.0178 / 0.0133 / 0.0107 / 0.0098** (b = 4 … 12), es decir ~~"entre 0.029 y 0.011"~~ **entre 0.027 y 0.010**. **η_ε no cambia** (0.0000 / 0.0000 / 0.0000 / 0.0052): es una diferencia y la constante se cancela. `verificacion_piso_y_eta.py` y su salida archivada no se modifican; quedan como registro de la corrida original, superados por `lorenz_checkpoints.py` en esa columna.

**Sin cambio.** Tabla principal (las siete filas), pendiente float64 66.1 pasos/bit, verificación del piso (saturación 2655 → 3052 / 4228 / 5011 con referencia de 160 bits), generalización fuera de muestra de las Reglas 110 y 30 (g = 0.0088), η_ε y η del ruido continuo.

---

*Historia: informe final del piloto (Protocolo v1.1, Enmiendas 1–5) → 2026-08-26: sección "Erratas de trazabilidad" (Enmienda 6; verificación de herencia). Cuerpo original intacto salvo las marcas † / tachado que remiten a las erratas.*

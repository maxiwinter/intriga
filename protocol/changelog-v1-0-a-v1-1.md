# Protocolo experimental — Changelog v1.0 → v1.1

**Naturaleza de este documento.** Enmiendas surgidas de la corrida piloto de §10.1 (controles sintéticos, informe adjunto: piloto-seccion-10-1-informe.md), registradas **antes de tocar cualquier dataset empírico**, conforme al paso previsto en el propio protocolo: el piloto sintético existe para descubrir estos problemas, y su documentación explícita es lo que distingue una corrección metodológica de un ajuste silencioso.

---

## Enmienda 1 — El piso de precisión de la aritmética de referencia (afecta §6, Pila de referencia)

**Hallazgo del piloto.** La predicción pre-registrada (≈76 pasos de fidelidad-ε por bit de condición inicial, derivada del exponente de Lyapunov de Lorenz) se midió en 66 pasos/bit, y las longitudes de coincidencia saturaron en ~2.655 pasos aun con precisión máxima de condición inicial. Hipótesis causal principal: el piso float64 de la trayectoria de referencia. **Verificada por desplazamiento** (ver Adenda final de verificación del informe): al recomputar la referencia en aritmética de 160 bits, la saturación desaparece y las longitudes de coincidencia crecen hasta p=76 sin tope. La discrepancia de pendiente (~64 vs ~76 pasos/bit) sobrevive a la corrección y queda sin causa asignada; se reporta sin corregir.

**Enmienda.** La especificación de cada pila U_ref debe incluir, además de intérprete, primitivas y bibliotecas: **la aritmética de referencia (formato de punto flotante, esquema de redondeo, orden de operaciones del integrador cuando aplique) y el piso de precisión resultante**. Ninguna afirmación sobre pendientes de resolución η_ε es interpretable en el régimen donde ε se aproxima a ese piso. Para datasets empíricos, el piso de precisión es el del instrumento de medición y debe declararse en §4.1 (representación de datos) con la misma obligatoriedad que las unidades.

## Enmienda 2 — Regla de codificación con re-sincronización para trayectorias de nivel B (afecta §5, Contabilidad del modelo)

**Hallazgo del piloto.** Un codificador de dos partes ingenuo (condición inicial única + residuo literal tras la divergencia) produce un artefacto: ρ del modelo generativo *crece* con n para sistemas caóticos (0.024 en n=2.500 → 0.87 en n=20.000), sugiriendo falsamente que la ventaja descriptiva se agota. Un codificador con checkpoints (re-especificación del estado a cada horizonte de Lyapunov) elimina el artefacto (ρ=0.0053 en n=20.000) y revela el costo verdadero: la regla se paga una vez; la trayectoria particular paga además ~λ/ln2 bits por unidad de tiempo, de manera irreducible.

**Enmienda.** La familia de modelos M para dominios con dinámica sensible a condiciones iniciales **debe incluir codificadores con re-sincronización de estado**, con el costo de cada checkpoint contabilizado en L(T) o en el residuo según la convención pre-registrada. La ausencia de esta clase de codificadores invalida cualquier conclusión de "agotamiento de la compresibilidad" en niveles B. Corolario contable para el marco general (v5.2, §9), **en su formulación corregida**: en sistemas caóticos deterministas no crece R_estado — crece la *precisión de R_estado que debe resolverse* para sostener la descripción de la historia a resolución fija, a tasa ~λ/ln2 bits por unidad de tiempo (Pesin/KS); los bits revelados se contabilizan en K(D|T,S₀). Esta tasa es medible y debe reportarse como parte de la superficie de resultados.

## Enmienda 3 — η_ε como requisito pendiente de la suite de sanidad (afecta §10.1 y §13.3)

**Estado.** La corrida piloto ejecutó los controles de §10.1 a **una sola resolución** (8 bits/coordenada). Las métricas ρ y g quedaron validadas; **η_ε no se midió**. La suite de sanidad no se considera completa —y ningún dataset empírico debe procesarse— hasta ejecutar el barrido de resoluciones pre-registrado (ε₁ > … > ε_m) **sobre los controles de variable continua** — inicialmente Lorenz y ruido continuo — y verificar que η_ε ≪ 1 para los generadores conocidos dentro del régimen válido (Enmienda 1) y η_ε ≈ 1 para el ruido. Para sistemas discretos (Regla 30/110, símbolo elemental binario) no existe un ε→0 físico comparable: se estudiará por separado el escalamiento con tamaño, horizonte temporal y granularidad de representación, sin identificar esas variables con ε. **Cumplida** (Adenda final de verificación: η_ε(Lorenz) ≈ 0–0.005; η(ruido continuo) = 1).

## Enmienda 4 — Registro del piloto como corrida de validación (afecta §10)

La corrida del piloto queda registrada con: semillas (42, 7), corrida única sin selección posterior, cuatro tests de sanidad superados (ruido ρ≈1.0005; Lorenz generativo ρ=0.0053; colapso de surrogates 0.50→0.99; brecha Regla 30 entre ρ_genérico≈1.0009 y ρ_generativo≈0.0107), generalización fuera de muestra funcionando en ambas direcciones (recuperación exacta de reglas con g≈0.009; rechazo del ruido con g>1). Limitaciones declaradas: datasets auto-generados (contaminación total por diseño, rol legítimo de control), compresores genéricos como aproximación gruesa de K, familia generativa que contenía al generador verdadero.

## Enmienda 5 — Contabilidad de ρ e interpretación de la tasa de Lyapunov (afecta §13 y el informe piloto)

**Hallazgos de la auditoría del piloto.** (a) Los compresores genéricos usados en paralelo son codificadores competidores de una misma metaclase, no pilas U_ref; la selección del mejor paga log₂k bits. (b) La razón generativa con generador conocido debe etiquetarse ρ_oracle (cota de existencia), distinta de ρ_MDL (mínimo efectivo de la familia, con M₀ incluido, por construcción ≤ 1) y de r_generic (ratio bruto del compresor, que puede superar 1 por overhead). (c) La interpretación de la tasa de Lyapunov como "crecimiento de R_estado" era incorrecta; la formulación válida es la del corolario corregido de la Enmienda 2.

**Enmienda.** El reporte estándar de resultados usará las tres columnas r_generic / ρ_oracle (solo controles sintéticos) / ρ_MDL, con el costo de selección contabilizado en ambos niveles — la clase (log₂k de la metaclase de compresores) y el identificador del modelo ganador dentro de la familia (por lo cual ρ_MDL ≃ ρ_oracle, no igualdad exacta, aun cuando la familia contenga al generador); y toda afirmación sobre tasas de información en dinámica determinista se formulará como precisión requerida del estado inicial, nunca como creación de información fundamental.

---

## Riesgo metodológico registrado (no es enmienda; es advertencia de proceso)

El marco conceptual (v5.2) y este protocolo fueron desarrollados mediante rondas de crítica cruzada entre múltiples sistemas de IA con supervisión humana. Ese proceso da robustez frente a los errores *no compartidos* entre los sistemas; no da ninguna frente a los sesgos que los sistemas comparten por construcción (corpus de entrenamiento solapados, convenciones de formalización similares). **Antes del primer dataset empírico con pretensión publicable, el protocolo debe pasar por al menos un revisor humano experto en MDL/teoría de la información algorítmica y uno en el dominio físico elegido.** Esta es la aplicación al propio método de trabajo de la frontera de observabilidad que el marco llama R_observabilidad: la crítica interna no puede medir el punto ciego común de quienes la ejercen.

---

*Cambios pendientes de decisión (no bloquean v1.1): política exacta de amortización de bibliotecas compartidas entre dominios (§6); regla de precisión identificable para parámetros continuos en familias no regulares (§5.2).*

**Protocolo v1.1 = Protocolo v1.0 + Enmiendas 1–5.** Enmiendas 1 y 3 verificadas/cumplidas (Adenda final de verificación del informe). **Estado: listo para congelar** — fecha, hash y commit son actos del investigador; tras el congelamiento, toda modificación posterior a §11.1 debe tratarse como potencialmente adaptativa a resultados y documentarse como tal.

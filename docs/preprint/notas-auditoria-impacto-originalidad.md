# Adiciones post-ensamblado (auditorías de impacto y originalidad — consolidado)

**Naturaleza de este documento.** Texto del investigador, entregado el 2026-08-26 como insumo obligatorio para el preprint (hito 1). Se transcribe verbatim; cualquier reformulación vive en el preprint, no aquí.

---

### Postura del preprint (usar casi textual en la introducción)
"No decidimos por argumento si los datos científicos son algorítmicamente comprimibles.
Medimos operacionalmente cuánto costo descriptivo puede transferirse de los datos a
estructuras reutilizables, cómo escala esa transferencia con n, ε y nivel descriptivo,
y cuánto generaliza fuera de muestra."
Marco dialéctico: el trabajo retoma la controversia explícita McAllister (2003) vs
Twardy-Gardner-Dowe (2005) — con la réplica de McAllister (2005): compresión MML ≠
compresibilidad algorítmica exacta, por lo que aquel debate NO era este programa —
y propone una metrología que permite reformularla en términos cuantitativos y
dependientes de escala. El protocolo puede medir la FRONTERA entre ambas posiciones
en vez de elegir una: ρ pequeño con residuo algorítmicamente aleatorio es compatible
con las dos (la regularidad comprime la mayor parte; la perturbación irreducible
vive en el residuo). Nunca presentar el debate como "esperando este experimento".

### Reivindicación de originalidad (usar esta formulación, no otra más fuerte)
"To the best of our knowledge, previous work has studied algorithmic compressibility,
MDL/MML inference, algorithmic rate-distortion and practical complexity estimators
separately, but has not combined them into a preregistered cross-domain framework for
measuring descriptive scaling across dataset size, resolution and descriptive level,
with out-of-sample and surrogate controls."
Título propuesto del preprint: "A Preregistered Metrological Framework for Measuring
the Scale- and Resolution-Dependent Descriptive Compressibility of Empirical
Regularities". No vender como nueva teoría de la compresión del universo.

### Antecedentes obligatorios adicionales (sumar a la lista de deudas)
- De Rooij & Vitányi: rate-distortion algorítmico para objetos individuales, con
  compresores reales, experimentos de compresión con pérdida y denoising en varios
  dominios. ANTECEDENTE PRINCIPAL de C(D,ε). Diferenciación: ellos construyen la
  curva por objeto; nosotros medimos escalamiento comparativo dominio × nivel × n × ε
  con costo de teoría, pre-registro, surrogates y generalización.
- McAllister 2005 (réplica a Twardy et al.): la distinción MML vs Kolmogórov exacto.
- Leyva-Acosta, Acuña Yeomans & Hernández-Quiroz (2026): correlación débil entre
  estimadores por compresión y por ejecución (CTM/BDM) — sostiene tanto la exigencia
  de ≥2 U_ref como la separación r_generic / ρ_MDL, y el piloto (Regla 30, PCG64) la
  reproduce operacionalmente.
- Regresión simbólica exhaustiva + MDL en astrofísica (2026) — verificar referencia
  primaria. Diferenciación: seleccionan la mejor ecuación de un dataset; nosotros
  medimos escalamiento de la transferencia descriptiva.

### Mapa de originalidad por componente (guía para related work)
No originales: leyes-como-compresión (Wheeler, best-system), MDL/MML científico,
rate-distortion algorítmico, compresores≈K, comparación de estimadores, surrogates,
out-of-sample, dependencia de U_ref. Con antecedente cercano: superficie C(D_n,ε)
(De Rooij-Vitányi). Posibles novedades: η_ε como pendiente normalizada de resolución
(PENDIENTE: búsqueda matemática exhaustiva — puede existir bajo otro nombre en
rate-distortion); estratigrafía dominio × nivel × n × ε. Aporte más defendible:
la combinación completa en un protocolo pre-registrado común.

### Escenarios de resultado valioso aunque la hipótesis falle
(a) ρ_física ≈ ρ_otros al igualar nivel y resolución → la excepcionalidad aparente
de la física venía del estrato elegido, no del dominio. (b) Estratigrafía universal
leyes → realizaciones → microhistoria en todos los dominios. Nota: el piloto ya midió
(b) en miniatura dentro de Lorenz (regla ~1.400 bits fijos; trayectoria ~λ/ln2 bits
por u.t.; microestado literal).

### Escalera de impacto (estado actual: peldaño 3 de 6)
marco → protocolo → piloto sintético reproducible → multi-dominio robusto →
estratigrafía reproducida independientemente → regularidad física nueva y predictiva.
El piloto NO es el descubrimiento: valida la metrología. La prueba de originalidad
científica empieza con las primeras superficies sobre datos empíricos reales.

---

*Historia: v1 (2026-08-26) — transcripción verbatim del texto entregado por Maximiliano Winter.*

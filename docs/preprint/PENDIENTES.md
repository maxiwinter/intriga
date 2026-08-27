# PENDIENTES antes de enviar el preprint

Lista de verificación obligatoria. Nada de lo que sigue está resuelto; el borrador vigente `preprint-v0-6.md` marca con `[VERIFY]` cada referencia no confirmada contra fuente primaria. **Ninguna cita se considera válida hasta que el investigador (o un revisor humano) haya leído la fuente.** Datos bibliográficos incompletos o dudosos se dejan explícitamente en blanco en lugar de completarse de memoria.

## A. Citas a verificar contra fuente primaria

Disputa destinataria (central — verificar título exacto, volumen, páginas y argumento):
1. McAllister, J. W. (2003). "Algorithmic randomness in empirical data." *Studies in History and Philosophy of Science* 34. — Confirmar la tesis exacta ("los datos empíricos son algorítmicamente aleatorios") y su alcance.
2. Twardy, C. R., Gardner, S., & Dowe, D. L. (2005). "Empirical data sets are algorithmically compressible: Reply to McAllister." *Studies in History and Philosophy of Science* 36. — Confirmar que la respuesta se apoya en MML.
3. McAllister, J. W. (2005). Réplica a Twardy, Gardner & Dowe. *Studies in History and Philosophy of Science* 36. — Confirmar la distinción MML ≠ compresibilidad algorítmica exacta, que sostiene la afirmación del preprint de que "aquel debate no era este programa". **Si la réplica no dice esto, reescribir §2 del preprint.**

Rate-distortion algorítmico (antecedente principal de C(D,ε)):
4. de Rooij, S., & Vitányi, P. M. B. "Approximating rate-distortion graphs of individual data: experiments in lossy compression and denoising." *IEEE Transactions on Computers* (¿2012?). — Confirmar año, volumen y dominios de los experimentos.
5. Vereshchagin, N. K., & Vitányi, P. M. B. (2010). "Rate distortion and denoising of individual data using Kolmogorov complexity." *IEEE Transactions on Information Theory* 56(7). — Confirmar.

Estimadores de complejidad y su correlación:
6. Zenil, H., Soler-Toscano, F., Delahaye, J.-P., Gauvrit, N., y otros: CTM/BDM (e.g., "A decomposition method for global evaluation of Shannon entropy and local estimations of algorithmic complexity", *Entropy* 2018; "Calculating Kolmogorov complexity from the output frequency distributions of small Turing machines", *PLoS ONE* 2014). — Confirmar cuál se cita.
7. Leyva-Acosta, Acuña Yeomans & Hernández-Quiroz (2026): correlación débil entre estimadores por compresión y por ejecución. — **Referencia no verificada en absoluto** (título, venue, DOI). Mencionada por el investigador; hay que localizarla. Si no se encuentra, retirar del preprint y reformular la justificación de ≥2 U_ref solo sobre la invariancia hasta constante aditiva.

Fundamentos:
8. Solomonoff, R. J. (1964). "A formal theory of inductive inference", Parts I–II. *Information and Control* 7. — Confirmar; y el resultado de convergencia (Solomonoff 1978, *IEEE Trans. IT*).
9. Hutter, M. (2005). *Universal Artificial Intelligence*. Springer. — Confirmar.
10. Rissanen, J. (1978). "Modeling by shortest data description." *Automatica* 14. — Confirmar.
11. Grünwald, P. D. (2007). *The Minimum Description Length Principle*. MIT Press. — Confirmar.
12. Wallace, C. S. (2005). *Statistical and Inductive Inference by Minimum Message Length*. Springer; y Wallace & Boulton (1968), *Computer Journal* 11. — Confirmar.
13. Wheeler, B. (teoría algorítmica de las leyes; "laws as compression"). — **Localizar la referencia exacta** (título, año, venue). No completar de memoria.
14. Lewis, D. (1973/1983), best-system account — *Counterfactuals* y "New work for a theory of universals" (*AJP* 61). — Confirmar cuál se usa para "best-system".
15. Li, M., & Vitányi, P. M. B. *An Introduction to Kolmogorov Complexity and Its Applications*. Springer (edición vigente). — Confirmar edición.
16. Chaitin, G. J. — resultado de incomputabilidad / no certificación de incompresibilidad (e.g., 1975, *J. ACM* 22, o *Information, Randomness & Incompleteness*). — Confirmar cuál.
17. Cilibrasi, R., & Vitányi, P. M. B. (2005). "Clustering by compression." *IEEE Trans. IT* 51(4). — Confirmar.
18. Crutchfield, J. P. (1994). "The calculi of emergence." *Physica D* 75; Shalizi & Crutchfield (2001), *J. Stat. Phys.* 104. — Confirmar cuál se cita.
19. Bennett, C. H. (1988). "Logical depth and physical complexity." En *The Universal Turing Machine: A Half-Century Survey*. — Confirmar.

Regresión simbólica y modelos de lenguaje:
20. Schmidt, M., & Lipson, H. (2009). "Distilling free-form natural laws from experimental data." *Science* 324. — Confirmar.
21. Udrescu, S.-M., & Tegmark, M. (2020). "AI Feynman." *Science Advances* 6. — Confirmar.
22. Regresión simbólica exhaustiva + MDL en astrofísica (2026). — **Referencia no verificada.** Candidata: línea de trabajo de Bartlett, Desmond & Ferreira ("Exhaustive symbolic regression", *IEEE TEVC* 2023, y aplicaciones cosmológicas posteriores). Localizar la referencia de 2026 que el investigador tiene en mente.
23. Delétang, G., et al. (2023/2024). "Language modeling is compression." arXiv:2309.10668 / ICLR 2024. — Confirmar venue final.

Dinámica y física:
24. Pesin, Ya. B. (1977). "Characteristic Lyapunov exponents and smooth ergodic theory." *Russian Math. Surveys* 32. — Confirmar; y Eckmann & Ruelle (1985), *Rev. Mod. Phys.* 57, para las condiciones de la relación de Pesin.
25. Lorenz, E. N. (1963). *J. Atmos. Sci.* 20. — Confirmar. Valor λ₁ ≈ 0.906 para (σ,ρ,β) = (10, 28, 8/3): Sprott, *Chaos and Time-Series Analysis* (2003) u otra fuente. — **Confirmar el valor y su fuente**; el preprint lo usa para la predicción de 76.5 pasos/bit.
26. Wolfram, S. (1983/2002) para las Reglas 30 y 110; Cook, M. (2004), *Complex Systems* 15, para la universalidad de la Regla 110. — Confirmar.
27. O'Neill, M. E. (2014). PCG: "A family of simple fast space-efficient statistically good algorithms for random number generation." — Confirmar (informe técnico HMC-CS-2014-0905).
28. Theiler, J., et al. (1992). "Testing for nonlinearity in time series: the method of surrogate data." *Physica D* 58. — Confirmar (fundamento de §10.2).
29. Tegmark, Aguirre, Rees & Wilczek (2006). *Phys. Rev. D* 73, 023505. — Confirmar (solo si se cita el censo de parámetros).
30. NIST Atomic Spectra Database (Kramida et al.) — citar versión y fecha de acceso cuando se use en §11.1; clasificar su contaminación teórica (§4.2) antes de citarla como dato.

## B. Búsquedas bibliográficas pendientes

- **η_ε**: determinar si la pendiente normalizada de resolución s_C/s_0 existe bajo otro nombre en la literatura de rate-distortion (clásica o algorítmica). Hasta entonces, el preprint la presenta como "posible novedad, no confirmada".
- **Estratigrafía dominio × nivel × n × ε**: buscar mediciones comparativas entre dominios con compresores (más allá de NCD para clustering).
- Preregistros previos de experimentos de compresión (OSF, AsPredicted) para sostener la afirmación de que no existe un instrumento sistemático pre-registrado.

## C. Huecos de código y datos detectados en la verificación de herencia (2026-08-26)

Ver `reproduccion-2026-08-26.md`, §4 y §4 bis. **Cerrados el mismo día por la Enmienda 6** (`protocol/enmienda-6.md`; sección "Erratas de trazabilidad" del informe):
- ~~Script para ρ_oracle = 0.0053~~ → `src/lorenz_checkpoints.py`: 0.0053 confirmado (k = 8, code_bits = 1096; la conjetura "7 checkpoints" era errónea).
- ~~Semilla para el control negativo~~ → control dual: `os.urandom` (invariantes p_error ≈ 0.5, g > 1) + `src/ruido_oos_semilla.py` (PCG64, semilla 2026).
- ~~Conciliar "166"~~ → formulación invariante en el informe (Errata 2).
- ~~Documentar "~64"~~ → impreso por script: promedio de tramos 64.2, rango 29–98, ajuste 67.6 (Errata 3).

Siguen abiertos:
- `verificacion_piso_y_eta.py` cablea `code_bits = 1252` (trazado: 1096). No se modificó; su columna ρ del barrido está superada por `lorenz_checkpoints.py` (Errata 4). Decidir si se deja como registro histórico con nota en cabecera o se retira del flujo de reproducción.
- Decidir si `piloto_10_1.py` integra el codificador con checkpoints en su tabla principal (hoy imprime el ingenuo, 0.5307) o si la tabla publicada cita ambos scripts.
- Nomenclatura del congelamiento: v1.1 = v1.0 + Enmiendas 1–6, o 1–5 + v1.2.
- Pilas U_ref verdaderas (≥ 2 convenciones completas e independientes) siguen sin implementar.

## C bis. Convención de versionado y deudas abiertas por el preprint v0.3 (2026-08-26)

**Convención adoptada:** *un archivo por versión, nombre = contenido*. Nada se edita en el lugar una vez publicada una versión; cada revisión crea un archivo nuevo y un changelog. El archivo `preprint-v0-1.md` conserva la v0.2 (nombre y contenido divergieron antes de adoptar la regla) y se mantiene sin modificar como registro. La versión vigente es `preprint-v0-3.md`.

Deudas abiertas por la revisión v0.3 (detalle y trazabilidad en `CHANGELOG-v0-2-to-v0-3.md` y `VALIDATION-REPORT-v0-3.md`):

1. **Definir `L_U(M₀)`** — el costo de descripción del modelo nulo — y recalcular todos los ρ contra el baseline completo `L₀^full = L_U(M₀) + L_U(D_ε|M₀)`, bajo la regla de trazabilidad de la Enmienda 6. Hasta entonces los ρ publicados son contra el residuo literal, y así está declarado en el preprint (§4.3, §7.5 bis). El desplazamiento cae bajo el redondeo de las tablas, pero no fue calculado.
2. **Script que imprima `g_pred` y `g_total`** por separado. Hoy solo se imprime `g_total`; los `g_pred` (0 para R110/R30, ≈1 para ruido) están derivados del error de test archivado y marcados como derivados.
3. **Errata 5 del informe del piloto**: el costo de la regla de Lorenz es **1288 bits** (1096 + 192), no "~1.400" — cifra heredada de la constante obsoleta 1252 que corrigió la Enmienda 6. El preprint v0.3 ya usa 1288; el informe todavía no.
4. ~~**Confirmar la lectura de "Track A / Track B"**~~ — **CERRADO (2026-08-26, v0.4).** La lectura de v0.3 era **errónea**. Resolución definitiva: la descomposición de Lorenz regla/trayectoria se llama **Level A / Level B** y pertenece a los niveles descriptivos (§4.6 del preprint, §9 del protocolo). **Track A / Track B quedan reservados en exclusiva para el primer experimento empírico de espectros**: Track A = *known-physics benchmark* (la familia sí contiene Rydberg y modelos conocidos; condición crítica de proveniencia), Track B = *blind discovery* (sin esas primitivas; toda estructura descubierta paga su longitud). La limitación §7.8 de v0.3 fue retirada por resuelta.
5. ~~**Propuesta para el protocolo — `h(p, ε)`**~~ — **CERRADO (2026-08-26, v0.4): incorporado** a `protocol/protocolo-v1-1-consolidado.md` §5.4, con las cinco reglas de uso (se mide y no se deriva; ambos argumentos siempre registrados; piso declarado; N_checkpoints = ⌈n/h⌉ con costo por checkpoint; costo de selección si h se optimiza). El protocolo consolidado **no está congelado**; la redacción queda sujeta a revisión del investigador. Texto original de la propuesta, conservado como referencia: El horizonte de re-sincronización debe definirse como una cantidad **medida**, función de la precisión del checkpoint *p* y de la resolución *ε*, explícitamente distinta del horizonte de Lyapunov teórico ≈ *p*·ln2/λ. Justificación: los 2655 pasos usados por el piloto están limitados por el piso aritmético float64 (quedan clavados en 2655 para b = 6…10, mientras que a b = 4 dan 3194 y a b = 12 dan 2458), de modo que llamarlos "horizonte de Lyapunov" contradice el hallazgo de la Enmienda 1. **Decisión del investigador:** incorporarlo al texto consolidado del protocolo antes del congelamiento, o registrarlo como v1.2. **No se modificó `/protocol`.**
6. **Imprimir los subtotales por track** (Track A y Track B) en `lorenz_checkpoints.py`: hoy 1288 y 1248 son sumas de cantidades impresas, no cantidades impresas.

## C ter. Deudas abiertas tras el preprint v0.4 (2026-08-26)

Detalle en `CHANGELOG-v0-3-to-v0-4.md` y `VALIDATION-REPORT-v0-4.md`.

**Cerradas en esta ronda:** significado de Track A / Track B; destino de `h(p, ε)`; `g_pred` ahora impresa por script (`src/g_metricas_oos.py` → `results/g-metricas-oos-salida.txt`: 0.0000 / 0.0000 / 1.0000); nomenclatura `g_total^bare` de los valores históricos, registrada en `docs/ERRATA-piloto-v1-1.md`; errata 1400 → 1288 documentada.

**Siguen abiertas:**

1. ~~**Definición concreta de `L_U(M₀)`**~~ — **CERRADA (2026-08-26, v0.5):** `protocol/definicion-L-M0.md`, incorporada por referencia en §7 del consolidado. `L_U(T) = L_id + spec + θ` para todo modelo, M₀ incluido; familia de primer nivel del piloto k = 5 → **L_id = 3 bits**, spec(M₀) = 0 por ser primitiva declarada → **L_U(M₀) = 3 bits**. *Queda abierto:* instanciar familia, árbol de códigos y primitivas **de cada dominio empírico** en su pre-registro.
2. ~~**Recalcular ρ con `L₀_full`**~~ — **CERRADA:** `src/contabilidad_completa.py` → `results/contabilidad-completa-salida.txt`. Predicción pre-declarada **confirmada en las 7 filas**: ninguna cambia a 4 decimales (mayor δ = 2.9×10⁻⁵) y **ρ_full ≤ 1 verificado fila por fila**, con 1.000000 exacto en el ruido.
3. ~~**Calcular e imprimir `g_total` simétrica**~~ — **CERRADA:** mismo script. R110 y R30 → 0.0088; ruido PCG64 → 1.0088, con g_total^bare conservada al lado y **no reinterpretada**.
4. ~~**Imprimir los subtotales de Nivel A y Nivel B**~~ — **CERRADA:** mismo script imprime identificador 3, Nivel A 1288, Nivel B 156·⌈n/h⌉ = 1248, total 2539 y el escalamiento por n.
5. **Dos pilas U_ref verdaderas** — dos convenciones completas e independientes de codificación. Sin implementar; los compresores genéricos son una sola metaclase.
6. **Política de amortización de bibliotecas** compartidas entre dominios (§6 del protocolo).
7. **Regla de precisión identificable** para parámetros continuos en familias no regulares (§5.2 del protocolo).
8. **Verificar las 33 referencias `[VERIFY]`** contra fuente primaria (sección A de este documento).
9. **Revisión humana experta** (MDL/AIT + dominio físico) antes del primer resultado empírico publicable.
10. **Afiliación, ORCID, licencia** del repositorio.
11. **Congelamiento y depósito OSF** del protocolo consolidado: PDF, SHA-256, tag de Git, depósito. **No hecho: el protocolo dice NOT YET FROZEN.**
12. **Discrepancia de pendiente en Lorenz** sin causa asignada (64.2 promedio de tramos, rango 29–98, ajuste 67.6, contra 76.5 predicho). Se reporta, no se corrige.
13. **Decidir si `ERRATA-piloto-v1-1.md` se incorpora** al informe del piloto o permanece como archivo adjunto.
14. **Ejecutar la medición de espectros atómicos** (Tracks A y B). **No iniciada.**

## C quater. Auditoría final (2026-08-26) — dos correcciones cerradas

Detalle en `CHANGELOG-v0-5-to-v0-6.md` y `VALIDATION-REPORT-v0-6.md`.

**CERRADAS:**
1. ~~**Error algebraico de g_total − g_pred**~~ — la expresión `A/(B+H)` valía solo con `g_pred = 0`. Identidad exacta fijada: **`g_total − g_pred = (A − B·g_pred)/(B + H) = (A·H − B·G)/[H·(B + H)]`**, incorporada a §13.5 del consolidado y a §4.5 del preprint, verificada por `assert` en `src/contabilidad_completa_v2.py`. Retirada la afirmación falsa de que la diferencia valía 811/92 163 en los tres controles: es 0.0087996 en Reglas 110/30 (g_pred = 0) y 0.0087671 en el ruido (g_pred ≈ 1). **Ambas redondean a 0.0088: ninguna cifra publicada cambia.** Registrado como Errata 8.
2. ~~**Trazabilidad del antiguo log₂3**~~ — el cargo de log₂3 ≈ 1.585 bits estaba **declarado pero no incorporado** a los totales históricos: Lorenz histórico = 1096 + 192 + 1248 = 2536 bits, sin sumando de selección, contra 2539 con el identificador actual. Corregida la nota de `definicion-L-M0.md`, la descripción del setup en §6.1 del preprint y registrado como **Errata 7**. El identificador de 3 bits **no** se presenta como reetiquetado de bits ya pagados.

**Corrección de encuadre asociada:** `L_U(M₀) = 3 bits` se presenta ahora como **consecuencia determinista de convenciones pre-declaradas** (familia de cinco miembros + código uniforme prefix-free de la pila U_ref), **no** como valor canónico ni ontológico.

**SIGUEN ABIERTAS** (sin cambios respecto de C ter):
- dos pilas U_ref verdaderas;
- política de amortización de bibliotecas compartidas;
- regla de precisión identificable en familias no regulares;
- instanciación de familia, árbol de códigos y primitivas de cada dominio empírico;
- las 33 referencias `[VERIFY]`;
- revisión humana experta (MDL/AIT + dominio físico);
- afiliación, ORCID, licencia;
- **discrepancia de pendiente de Lorenz** (64.2 promedio de tramos / 67.6 ajuste contra 76.5 predicho), sin causa asignada — **no investigada en esta ronda por instrucción expresa**;
- congelamiento: PDF, SHA-256, tag de Git, depósito OSF. **No hecho.**
- primera medición empírica (§11.1, Tracks A y B). **No iniciada.**

## D. Administrativo

- Afiliación del autor; ORCID.
- Licencia del repositorio (CITATION.cff dice "completar licencia antes de publicar").
- Congelamiento formal de v1.1: PDF consolidado, hash, tag `protocolo-v1.1-congelado`, preregistro OSF con el mismo hash. El preprint debe citar ese hash una vez exista.
- Revisión humana experta (MDL/AIT + dominio físico) **antes** del primer resultado empírico, no antes del preprint metodológico; pero el preprint debe declarar que esa revisión es condición del programa.
- Decisión final del título (auditoría de originalidad vs. título original de la consigna; ver nota al pie del preprint).

---

*Historia: v1 (2026-08-26) — lista inicial, redactada por el asistente de IA bajo supervisión de Maximiliano Winter.*

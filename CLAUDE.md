# Contexto del proyecto — leer antes de trabajar

## Qué es esto
Programa de investigación sobre la **comprimibilidad de las regularidades físicas** ("La intriga").
Aporte pretendido: no la idea (tiene linaje: Solomonoff, best-system/teoría algorítmica de las leyes,
Wigner), sino la **metrología**: medición pre-registrada, entre dominios, de cuánta descripción
estructural exige el mundo por bit de observación. Destinatario académico identificado: la disputa
McAllister (2003, "los datos empíricos no comprimen") vs. Twardy-Gardner-Dowe (2005, "sí comprimen"),
nunca zanjada con un instrumento sistemático.

## Estado (al 2026-08-27)
- Marco conceptual: **v5.2** (docx del investigador, en /protocol) — CONGELADO. Cambios → v5.3+, registrados.
- Protocolo experimental: **v1.1 = v1.0 + Enmiendas 1–6 + definición de L_U(T)/L_U(M₀)** (nomenclatura RATIFICADA;
  v1.2 reservada para post-congelamiento). Consolidado en /protocol/protocolo-v1-1-consolidado.md — **CONGELADO
  2026-08-27** por acto del investigador: PDF en /protocol/protocolo-v1-1-congelado.pdf, sha256 de los cuatro
  documentos congelados en /HASHES.txt, tag anotado **`fase-ia-v1.1`** (commit 8539670). **Preregistro público
  OSF: hecho — https://osf.io/yq9hr** (27-08-2026, template Open-Ended, licencia CC BY 4.0; PDF congelado y
  HASHES.txt archivados adentro). Congelar ≠ preregistrar, pero ambas cosas están hechas: v1.1 **ya puede
  citarse como pre-registro público**.
- Documentos congelados (no se editan; editarlos rompe /HASHES.txt): protocolo-v1-1-consolidado.md,
  protocolo-v1-1-congelado.pdf, definicion-L-M0.md, DECLARACION.md. Verificar con `sha256sum -c HASHES.txt`.
- Piloto §10.1 (controles sintéticos): **APROBADO** — informe final en /docs, código en /src, salidas en /results.
- Siguiente etapa: **§11.1, primera medición empírica** (espectros atómicos primero; nunca CMB primero).
- Hitos: congelar v1.1 → **HECHO (2026-08-27, tag `fase-ia-v1.1`)**. Preregistro OSF → **HECHO (2026-08-27, osf.io/yq9hr)**. Pendientes: preprint metodológico (borrador **v0.6**, un archivo por versión, citas sin verificar) → revisión experta humana independiente (Regla 8) → repo público → dataset real (§11.1 espectros: Track A benchmark / Track B blind discovery, NO iniciado).

## Reglas duras (no negociables)
1. **v1.1 no se modifica** tras el congelamiento. Problemas en §11.1 = desviación documentada o futura v1.2.
2. Contabilidad MDL siempre: ΔC = Δ(modelo+residuo); solo hay compresión si ΔC < 0. Menos parámetros ≠ mejor.
3. Tres columnas en todo reporte: r_generic / ρ_oracle (solo sintéticos; exige generador conocido) / ρ_MDL
   (≤ 1; incluye M₀ y los costos de identificación de clase y de modelo).
4. η_ε solo para variables continuas; sistemas discretos: escalamiento por tamaño/horizonte/granularidad, sin llamarlo ε.
5. Dinámica determinista: jamás afirmar "creación de información"; formular como precisión requerida del
   estado inicial (Pesin/KS bajo sus condiciones de aplicabilidad).
6. Pre-registrar TODO antes de mirar D_test: representación, d, Q(d,ε), ε, regla de precisión de parámetros,
   U_ref (≥ 2 pilas), M₀, familia M, partición train/test.
7. Datasets: clasificar contaminación teórica (§4.2 del protocolo). Un dataset que incorpora la teoría
   evaluada no es evidencia principal de esa teoría.
8. **Revisión humana experta obligatoria** (MDL/AIT + dominio físico) antes del primer resultado empírico publicable.
9. Resultado negativo = resultado. Se publica igual.

## Deudas conocidas
- Discrepancia de pendiente en Lorenz: ~64 pasos/bit medidos (promedio de tramos; tramos 29–98; ajuste lineal 67.6;
  src/lorenz_checkpoints.py) vs 76.5 predichos; sobrevivió a la corrección del piso float64 (verificada por
  desplazamiento con referencia de 160 bits). SIN causa asignada. No "corregir": investigar o reportar.
- Trazabilidad (Enmienda 6): todo número publicado sale de un script en /src con salida en /results. Pendiente de decisión:
  si piloto_10_1.py integra el codificador con checkpoints en su tabla (hoy imprime el ingenuo). verificacion_piso_y_eta.py
  cablea code_bits=1252 (el trazado es 1096): no se modifica; su columna ρ del barrido está superada por lorenz_checkpoints.py.
- Contabilidad CERRADA (2026-08-26): L_U(M₀) definido (L_id + spec + θ para todo modelo, M₀ incluido; piloto k=5 → 3 bits).
  Recomputación con L₀_full: ninguna fila cambia a 4 decimales, ρ_full ≤ 1 verificado. g_total simétrica calculada; los valores
  históricos 0.0088/1.009/1.0088 son **g_total^bare** y no se reinterpretan. Abierto: instanciar la familia de cada dominio empírico,
  dos pilas U_ref verdaderas, amortización de bibliotecas, precisión identificable en familias no regulares.
- Revisión de literatura pendiente para el preprint. Citar y diferenciar como mínimo: McAllister 2003;
  Twardy-Gardner-Dowe 2005; Wheeler (teoría algorítmica de las leyes); Rissanen/Grünwald (MDL); Wallace (MML);
  Solomonoff/Hutter; Cilibrasi-Vitányi (NCD); Zenil (CTM/BDM; incl. el resultado 2026 de correlación débil entre
  estimadores, que sostiene la exigencia de ≥ 2 U_ref); Crutchfield (mecánica computacional); Schmidt-Lipson y
  AI Feynman (regresión simbólica); "language modeling is compression". Originalidad siempre como "hasta donde sabemos".
- Pilas U_ref verdaderas (dos convenciones completas e independientes de codificación) aún no implementadas:
  los compresores genéricos del piloto son una sola metaclase.

## Convenciones
- Idioma de documentos y comentarios: español. Preprint: inglés.
- Historia de versiones al pie de cada documento. Nada se reescribe silenciosamente.
- El proceso hasta aquí fue crítica cruzada entre varios sistemas de IA con supervisión humana
  (Maximiliano Winter). Robusto ante errores no compartidos; ciego a los compartidos — de ahí la regla 8.

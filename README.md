# La intriga — Programa I: metrología de la comprimibilidad

¿Por qué el costo descriptivo de las regularidades físicas crece tan lentamente frente a la
cantidad, diversidad y precisión del mundo que explican?

Este repositorio contiene el marco conceptual (v5.2), el protocolo experimental congelado (v1.1),
el instrumento de medición y el piloto sintético aprobado (§10.1). Ver DECLARACION.md para qué es
este repositorio y cómo se produjo; CLAUDE.md para el estado del proyecto y las reglas de trabajo;
/protocol para el protocolo y su congelamiento.

El estado congelado corresponde al tag **`fase-ia-v1.1`** (2026-08-27): fin de la fase de desarrollo
asistido por IA, previo a revisión experta humana independiente. **Congelar no es preregistrar:** no
hay depósito OSF, de modo que nada de v1.1 puede citarse como pre-registro público.

## Estructura
- /protocol — protocolo v1.0 (docx) + changelog v1.1 + enmienda-6 + definicion-L-M0 + **protocolo-v1-1-consolidado.md** (CONGELADO 2026-08-27) + **protocolo-v1-1-congelado.pdf**, marco v5.2 (docx)
- /HASHES.txt — sha256 de los cuatro documentos congelados; verificar con `sha256sum -c HASHES.txt`
- DECLARACION.md — qué es este repositorio, quién hizo qué, y qué no está validado
- /docs — marco conceptual (v5 md; v5.2 docx en /protocol), reglas y parámetros, informe final del piloto
- /src — instrumento: piloto_10_1.py (controles sintéticos), verificacion_piso_y_eta.py, lorenz_checkpoints.py (checkpoints a 20k, pendientes), ruido_oos_semilla.py (control negativo reproducible)
- /results — salidas archivadas de las cuatro corridas
- /docs/preprint — hito 1: borrador del preprint (inglés), PENDIENTES, registro de reproducción
- /configs, /tests — reservados para §11.1

## Licencia
- **Documentos** (protocolo, marco conceptual, preprint, informes, `DECLARACION.md`): **CC BY 4.0** — ver `LICENSE`.
  Se pueden copiar, adaptar y redistribuir, incluso comercialmente, **citando la fuente**.
- **Código** (`/src`): **MIT** — ver `src/LICENSE`.

La licencia cubre todo el repositorio, incluido el estado etiquetado como `fase-ia-v1.1`.
Para citar el trabajo, ver `CITATION.cff`. Licenciar no es avalar: ver `DECLARACION.md` §5
sobre qué no está validado.

## Reproducir el piloto
    pip install numpy mpmath
    python src/piloto_10_1.py
    python src/verificacion_piso_y_eta.py
    python src/lorenz_checkpoints.py
    python src/ruido_oos_semilla.py

## Estado
Instrumento validado en controles sintéticos; reproducción final registrada en results/reproduccion-final-pre-congelamiento.txt.
Protocolo v1.1 = v1.0 + Enmiendas 1–6 + definición de L_U(T)/L_U(M₀): **CONGELADO el 2026-08-27** (tag `fase-ia-v1.1`, PDF en /protocol, sha256 en /HASHES.txt). **Sin depósito OSF: no es un pre-registro público.**
Revisión experta humana independiente: **pendiente**. Es la primera prueba externa del material, no un trámite posterior.
Preprint metodológico: borrador v0.6 en /docs/preprint (citas sin verificar).
Siguiente etapa: revisión experta humana independiente; luego §11.1 — primera medición empírica (espectros atómicos).

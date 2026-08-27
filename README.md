# La intriga — Programa I: metrología de la comprimibilidad

¿Por qué el costo descriptivo de las regularidades físicas crece tan lentamente frente a la
cantidad, diversidad y precisión del mundo que explican?

Este repositorio contiene el marco conceptual (v5.2), el protocolo experimental pre-registrado (v1.1),
el instrumento de medición y el piloto sintético aprobado (§10.1). Ver CLAUDE.md para el estado del
proyecto y las reglas de trabajo; /protocol para el protocolo y su congelamiento.

## Estructura
- /protocol — protocolo v1.0 (docx) + changelog v1.1 + enmienda-6 + definicion-L-M0 + **protocolo-v1-1-consolidado.md** (preparado para congelar, NO congelado), marco v5.2 (docx)
- /docs — marco conceptual (v5 md; v5.2 docx en /protocol), reglas y parámetros, informe final del piloto
- /src — instrumento: piloto_10_1.py (controles sintéticos), verificacion_piso_y_eta.py, lorenz_checkpoints.py (checkpoints a 20k, pendientes), ruido_oos_semilla.py (control negativo reproducible)
- /results — salidas archivadas de las cuatro corridas
- /docs/preprint — hito 1: borrador del preprint (inglés), PENDIENTES, registro de reproducción
- /configs, /tests — reservados para §11.1

## Reproducir el piloto
    pip install numpy mpmath
    python src/piloto_10_1.py
    python src/verificacion_piso_y_eta.py
    python src/lorenz_checkpoints.py
    python src/ruido_oos_semilla.py

## Estado
Instrumento validado en controles sintéticos; reproducción final registrada en results/reproduccion-final-pre-congelamiento.txt.
Protocolo v1.1 = v1.0 + Enmiendas 1–6 + definición de L_U(T)/L_U(M₀): **consolidado y preparado para congelar; NO congelado, sin hash ni depósito OSF**.
Preprint metodológico: borrador v0.6 en /docs/preprint (citas sin verificar).
Siguiente etapa: §11.1 — primera medición empírica (espectros atómicos).

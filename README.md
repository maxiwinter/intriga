# La intriga — Programa I: metrología de la comprimibilidad

¿Por qué el costo descriptivo de las regularidades físicas crece tan lentamente frente a la
cantidad, diversidad y precisión del mundo que explican?

Este repositorio contiene el marco conceptual (v5.2), el protocolo experimental congelado (v1.1),
el instrumento de medición y el piloto sintético aprobado (§10.1). Ver DECLARACION.md para qué es
este repositorio y cómo se produjo; CLAUDE.md para el estado del proyecto y las reglas de trabajo;
/protocol para el protocolo y su congelamiento.

El estado congelado corresponde al tag **`fase-ia-v1.1`** (2026-08-27): fin de la fase de desarrollo
asistido por IA, previo a revisión experta humana independiente. El lazo está cerrado: **el protocolo
v1.1 está congelado y públicamente preregistrado** en OSF — **https://osf.io/yq9hr** (27-08-2026,
template Open-Ended, licencia CC BY 4.0), con el PDF congelado y `HASHES.txt` archivados dentro del
registro. v1.1 ya puede citarse como pre-registro público.

## Estructura
- /protocol — protocolo v1.0 (docx) + changelog v1.1 + enmienda-6 + definicion-L-M0 + **protocolo-v1-1-consolidado.md** (CONGELADO 2026-08-27) + **protocolo-v1-1-congelado.pdf**, marco v5.2 (docx)
- /HASHES.txt — sha256 de los cuatro documentos congelados; verificar con `sha256sum -c HASHES.txt`
- DECLARACION.md — qué es este repositorio, quién hizo qué, y qué no está validado
- POST-FREEZE-NOTES.md — anotaciones sobre documentos congelados (no se editan; se anota aquí)
- /docs — marco conceptual (v5 md; v5.2 docx en /protocol), reglas y parámetros, informe final del piloto
- /src — instrumento (7 scripts): piloto_10_1.py y verificacion_piso_y_eta.py (piloto histórico), lorenz_checkpoints.py, ruido_oos_semilla.py, g_metricas_oos.py, contabilidad_completa.py, contabilidad_completa_v2.py (correcciones y contabilidad final). Ver "Reproducir el piloto"
- /results — salidas archivadas de cada corrida, una por script (Enmienda 6)
- /docs/preprint — hito 1: borrador del preprint (inglés), PENDIENTES, registro de reproducción. **Artefactos históricos previos al snapshot**: ver docs/preprint/README.md
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

**Piloto histórico §10.1** — la tabla tal como se publicó en su momento. Se conservan sin
modificar por trazabilidad; su contabilidad es la ingenua (no cobra M₀ en el denominador):

    python src/piloto_10_1.py
    python src/verificacion_piso_y_eta.py

**Correcciones y contabilidad final** — posteriores al piloto, cierran la contabilidad bajo
`protocol/definicion-L-M0.md`. **Ante discrepancia con las cifras del piloto histórico, estas
prevalecen:**

    python src/lorenz_checkpoints.py        # codificador con checkpoints; supera la columna ρ de verificacion_piso_y_eta
    python src/ruido_oos_semilla.py         # control negativo reproducible (Enmienda 6)
    python src/g_metricas_oos.py            # separa g_pred / g_total_bare / g_total_full
    python src/contabilidad_completa.py     # recomputa con L₀_full = L_U(M₀) + L_U(D_ε|M₀)
    python src/contabilidad_completa_v2.py  # + identidad exacta g_total − g_pred, verificada por assert

Cada script archiva su salida en `/results` (Enmienda 6: todo número publicado sale de un
script versionado). Los valores históricos 0.0088 / 1.009 / 1.0088 son **g_total^bare** y se
conservan como columna histórica; no se reinterpretan.

## Estado
Validación interna sobre controles sintéticos; validación experta externa pendiente. Reproducción final registrada en results/reproduccion-final-pre-congelamiento.txt.
Protocolo v1.1 = v1.0 + Enmiendas 1–6 + definición de L_U(T)/L_U(M₀): **CONGELADO el 2026-08-27** (tag `fase-ia-v1.1`, PDF en /protocol, sha256 en /HASHES.txt).
Preregistro público OSF: **hecho — https://osf.io/yq9hr** (registrado el 27-08-2026, template Open-Ended, licencia CC BY 4.0; el PDF congelado y `HASHES.txt` están archivados dentro del registro). El congelamiento y el preregistro son ahora un solo hecho verificable: el hash depositado es el de `/HASHES.txt`.
Revisión experta humana independiente: **pendiente**. Es la primera prueba externa del material, no un trámite posterior.
Preprint metodológico: borrador v0.6 en /docs/preprint (citas sin verificar).
Siguiente etapa: revisión experta humana independiente; luego §11.1 — primera medición empírica (espectros atómicos).

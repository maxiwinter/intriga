# Notas posteriores al congelamiento

**Este archivo es el lugar designado para toda anotación futura sobre documentos congelados.**

Los documentos congelados no se editan nunca: sus hashes SHA-256 están registrados en
`/HASHES.txt` y cualquier edición los rompería, invalidando la verificación que un revisor
externo puede correr con `sha256sum -c HASHES.txt`. Cuando haga falta señalar algo sobre
ellos — una errata, una expresión que envejeció, una aclaración, una desviación durante
§11.1 — se anota **aquí**, con fecha, y el documento congelado se deja intacto.

## Documentos congelados

Congelados el **2026-08-27**, tag `fase-ia-v1.1` (commit `8539670`):

- `protocol/protocolo-v1-1-consolidado.md`
- `protocol/protocolo-v1-1-congelado.pdf`
- `protocol/definicion-L-M0.md`
- `DECLARACION.md`

---

## Nota 1 — 2026-08-27 — Expresiones pre-congelamiento que sobreviven en el consolidado

El consolidado congelado fue redactado durante su fase preparatoria, y conserva formulaciones
escritas cuando el congelamiento todavía no había ocurrido. **No se modificaron**, con la única
excepción del bloque `STATUS` de la cabecera, que sí se actualizó como parte del acto de
congelamiento y antes de calcular los hashes.

Las que quedaron:

| Dónde | Qué dice | Cómo leerlo |
|---|---|---|
| Cabecera, párrafo de documentos fuente | "…los documentos fuente **prevalecen** hasta el congelamiento" | Cláusula cumplida y agotada. El congelamiento ocurrió el 2026-08-27; desde entonces el texto congelado es el de referencia. |
| Título del **Anexo A** | "Deudas abiertas al momento de **preparar** el congelamiento" | Inventario levantado antes del freeze. Sigue siendo el inventario válido: ninguna de sus deudas se cerró por el hecho de congelar. |
| Anexo A, deuda 10 | "**Congelamiento y depósito**: PDF, SHA-256, tag, OSF" | **Deuda cerrada.** PDF, SHA-256 y tag: cumplidos el 2026-08-27. OSF: **hecho** el 2026-08-27 — https://osf.io/yq9hr. Ver **Nota 2**. |
| Anexo A, deuda 9 | "Revisión humana experta (§18), pendiente" | Sigue **pendiente**. Es el siguiente hito real. |
| Pie, sección Historia | "Estado: preparada para congelamiento; NO congelada" y "**STATUS sin cambios: NOT YET FROZEN OR PREREGISTERED.** No se calculó hash, no se etiquetó Git, no se depositó nada" | Registro fechado el 2026-08-26, verdadero ese día. **Íntegramente superado**: hash y tag el 2026-08-27, y depósito OSF el mismo día (Nota 2). La frase describe el 26 de agosto, no el estado vigente. |

**Regla de lectura general:** en el consolidado congelado, toda expresión en futuro o en
pendiente referida al *acto de congelar* o al *depósito público* describe su fase de redacción.
El estado vigente está en `/README.md`, `/protocol/README.md`, el tag `fase-ia-v1.1` y el
registro OSF https://osf.io/yq9hr.

**Actualización (2026-08-27, misma fecha, posterior a esta nota):** la última fila de esta tabla
y el párrafo que la seguía decían que no había depósito OSF y que nada de la v1.1 podía citarse
como pre-registro público. **Dejó de ser cierto el mismo día:** el depósito se consumó. Ver
**Nota 2**. La redacción original de esa afirmación se conserva descrita aquí, no borrada.

---

## Nota 2 — 2026-08-27 — Preregistro público OSF: hecho

Documentos afectados: ninguno congelado se modificó. Esta nota cierra la deuda 10 del Anexo A
del consolidado y corrige las afirmaciones de la Nota 1 sobre la ausencia de depósito.

| | |
|---|---|
| Registro | **https://osf.io/yq9hr** |
| Fecha de registro | 2026-08-27 |
| Template | Open-Ended Registration |
| Licencia | CC BY 4.0 |
| Contenido archivado | `protocol/protocolo-v1-1-congelado.pdf` y `HASHES.txt` |

**Qué cambia.** El lazo congelamiento → depósito está cerrado. Desde el 2026-08-27 la v1.1
**sí puede citarse como pre-registro público**: el PDF congelado y los SHA-256 que lo verifican
están archivados dentro del registro, de modo que un revisor externo puede correr
`sha256sum -c HASHES.txt` sobre el repositorio y contrastar el resultado contra el depósito,
sin depender de este repositorio para la fecha.

**Qué no cambia.**
- Los documentos congelados siguen sin editarse; sus hashes siguen siendo los de `/HASHES.txt`.
- La regla dura 1 sigue en vigor: nada hallado en §11.1 modifica v1.1. Ahora, además, hay un
  depósito público con fecha contra el cual se lee cualquier desviación.
- **Preregistrar no es validar.** La revisión experta humana independiente (regla dura 8,
  deuda 9 del Anexo A) sigue **pendiente**, y es el siguiente hito real. Un preregistro dice
  qué se comprometió a hacer el programa antes de mirar los datos; no dice que el diseño sea
  correcto.

---

## Cómo agregar una nota

Numerada, fechada, sin tocar el documento congelado:

    ## Nota N — AAAA-MM-DD — Título breve
    Documento afectado: <ruta>
    Qué se observó, y qué se hace con eso (nada, desviación documentada, o motiva v1.2).

Las desviaciones halladas durante §11.1 se registran aquí y **no** modifican v1.1
(regla dura 1 del proyecto).

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
| Anexo A, deuda 10 | "**Congelamiento y depósito**: PDF, SHA-256, tag, OSF" | PDF, SHA-256 y tag: **cumplidos** el 2026-08-27. OSF: **pendiente**. |
| Anexo A, deuda 9 | "Revisión humana experta (§18), pendiente" | Sigue **pendiente**. Es el siguiente hito real. |
| Pie, sección Historia | "Estado: preparada para congelamiento; NO congelada" y "**STATUS sin cambios: NOT YET FROZEN OR PREREGISTERED.** No se calculó hash, no se etiquetó Git, no se depositó nada" | Registro fechado el 2026-08-26, verdadero ese día. Superado por el freeze del 2026-08-27 en cuanto a hash y tag; **sigue vigente en cuanto a depósito**: no se depositó nada. |

**Regla de lectura general:** en el consolidado congelado, toda expresión en futuro o en
pendiente referida al *acto de congelar* describe su fase de redacción. El estado vigente está
en `/README.md`, `/protocol/README.md` y el tag `fase-ia-v1.1`.

**Lo que no cambió y conviene no malinterpretar:** congelar no es preregistrar. No hay depósito
OSF. Nada de la v1.1 puede citarse como pre-registro público, ni antes ni después del freeze.

---

## Cómo agregar una nota

Numerada, fechada, sin tocar el documento congelado:

    ## Nota N — AAAA-MM-DD — Título breve
    Documento afectado: <ruta>
    Qué se observó, y qué se hace con eso (nada, desviación documentada, o motiva v1.2).

Las desviaciones halladas durante §11.1 se registran aquí y **no** modifican v1.1
(regla dura 1 del proyecto).

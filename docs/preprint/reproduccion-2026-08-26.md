# Registro de reproducción del piloto §10.1 — 2026-08-26

**Propósito.** Verificación de herencia previa al hito 1 (preprint metodológico): confirmar que el repositorio ensamblado reproduce las salidas registradas en `/results` antes de redactar cualquier documento que las cite. Este registro es un acto de lectura; no modifica ningún archivo congelado.

## 1. Documentos maestros en `/protocol`

| Archivo | SHA-256 |
|---|---|
| `protocolo-experimental-programa-I-v1-0.docx` | `55e8fdd7efbe20159eac536b1e03f2660b56330808824a55378abac33133643a` |
| `la-intriga-version-5-2.docx` | `6257a4917b85044708dfaa7418dd79b9ea5f31f91d292f83b115b9ba46467a55` |

Ambos presentes (agregados por el investigador el 2026-08-26). El texto extraído del docx del protocolo v1.0 coincide en estructura (§1–§19) con las secciones citadas en el changelog v1.0→v1.1 y en el informe final del piloto. Nota: la copia desde Windows dejó dos archivos `*.docx:Zone.Identifier` (25 bytes cada uno, metadatos del navegador). No son parte del protocolo; se recomienda borrarlos o agregar `*:Zone.Identifier` al `.gitignore` (acto del investigador).

Hashes de los demás archivos congelados al momento de la verificación:

```
c65e5f7a…e38f51  protocol/README.md
de202cf6…9ef7b3  protocol/changelog-v1-0-a-v1-1.md
4f25b40d…ffd75b  docs/la-intriga-v5.md
ab28ee9d…da87524 docs/piloto-seccion-10-1-informe-final.md
820eb618…ae505e  docs/reglas-y-parametros-del-universo.md
1134a7ac…c616e18 src/piloto_10_1.py
0eb131b3…c52a801 src/verificacion_piso_y_eta.py
e30d4518…1ac9f850 results/piloto-10-1-salida.txt
5cd6f17d…26be8d3 results/verificacion-piso-y-eta-salida.txt
```

## 2. Entorno de reproducción

- Linux 5.15 (WSL2), Python 3.12.3, numpy 2.5.2, mpmath 1.4.1 (entorno virtual aislado; el sistema no permite `pip install` global).
- Comandos: `python src/piloto_10_1.py`, `python src/verificacion_piso_y_eta.py`. Ambos terminaron con código de salida 0.

## 3. Comparación con `/results`

### `piloto_10_1.py` → `results/piloto-10-1-salida.txt`

Idéntico en todas las líneas que dependen de semillas fijas (42, 7):

- tabla principal (7 filas: L₀, r_generic, ρ_generativo);
- pendiente de Lorenz: 66.1 pasos/bit de condición inicial;
- longitudes de coincidencia p=12…52 (62, 187, 417, 1137, 1460, 1372, 1469, 1846, 2222, 2511, 2655);
- escalamiento de Lorenz (n = 1000…20000);
- generalización fuera de muestra R110 y R30 (regla exacta, 0.0 % error, g = 0.008767…).

**Única diferencia:** la fila `ruido` del test fuera de muestra.

| | regla espuria | error en test | g |
|---|---|---|---|
| `/results` | 9 | 0.50067 | 1.008766 |
| esta corrida | 199 | 0.50228 | 1.008752 |

Causa: el control negativo usa `os.urandom` sin semilla, por diseño declarado en el informe ("ruido de os.urandom"). El resultado cualitativo pre-registrado se mantiene (error ≈ 50 %, g > 1: el modelo paga su costo sin comprar nada). La fila del ruido en la tabla principal (r_generic = 1.0005) coincidió a cuatro decimales, como es esperable para 32 768 bytes de una fuente de alta entropía.

**Decisión:** se registra como **reproducido**; la diferencia es la esperada para una fuente sin semilla.

### `verificacion_piso_y_eta.py` → `results/verificacion-piso-y-eta-salida.txt`

Idéntico en todos los números (matches en precisión extendida p=40/52/64/76: 2699/3052/4228/5011; barrido b=4…12: ρ 0.0293→0.0106, η_ε 0/0/0/0.0052; ruido continuo r_generic 1.0007 y 1.0005, η=1). Difiere solo el tiempo de cómputo de la referencia extendida (0.7 s vs 1.4 s), que no es una medición.

## 4. Inconsistencias pre-existentes detectadas (no corregidas; se reportan)

1. **"Regla espuria 166".** El informe final del piloto dice que el ruido tratado como autómata produjo la "regla" 166; `/results` registra 9; esta corrida, 199. Consistente con una fuente sin semilla, pero el informe cita un número que no corresponde a la salida archivada. Sugerencia (no aplicada): dejar de citar el identificador de la regla espuria, o fijar una semilla para el control negativo en futuras corridas, documentándolo como cambio de v1.2.
2. **ρ_oracle(Lorenz, 20 000 pasos, con checkpoints) = 0.0053** — el número principal de la fila de Lorenz en la tabla del informe — **no lo produce ningún script de `/src`**. `piloto_10_1.py` calcula la fila con el codificador ingenuo (sin re-sincronización) e imprime 0.5307; `verificacion_piso_y_eta.py` implementa el codificador con checkpoints pero solo a n = 5000 (ρ = 0.0146 a 8 bits). Con las constantes que ese script declara (1252 bits de código + 192 de parámetros + 156 por checkpoint, horizonte 2655 pasos) a n = 20 000: 7 checkpoints → 2536 bits → ρ = 0.0053; ⌈20000/2655⌉ = 8 checkpoints → 2692 bits → ρ = 0.0056. El valor 0.0053 es por tanto reconstruible con la regla de 7 checkpoints, pero el código que lo generó no está en el repositorio. El preprint cita 0.0053 como número documentado y declara este hueco.
3. **Pendiente "~64 pasos/bit en precisión extendida".** El script no la imprime; se deriva de los matches (5011 − 2699)/(76 − 40) = 64.2 pasos/bit. La pendiente por tramos no es uniforme: (3052 − 2699)/12 = 29.4; (4228 − 3052)/12 = 98.0; (5011 − 4228)/12 = 65.3. El valor "~64" es la pendiente del ajuste global p = 40…76. Se reporta tal cual; forma parte de la discrepancia sin causa asignada.
4. **Predicción 76 pasos/bit.** Verificada la aritmética: ln 2 / 0.906 / 0.01 = 76.5.

## 4 bis. Post-scriptum (mismo día, Enmienda 6)

La conjetura del §4.2 — que 0.0053 correspondía a 7 checkpoints — **era errónea y se retira**. Al escribir `src/lorenz_checkpoints.py` se encontró que la constante `code_bits = 1252` cableada en `verificacion_piso_y_eta.py` no es el gzip del fuente declarado (que mide 1096 bits; verificable en la salida archivada del codificador ingenuo, C(n = 1000) = 1360 = 1096 + 192 + 72). Con 1096 y k = ⌈20000/2655⌉ = 8, el script reproduce **exactamente 0.0053**: el informe tenía razón; el hueco era de trazabilidad, no de valor. La constante 1252 sí afecta los ρ del barrido de resolución de la Adenda (corregidos en la Errata 4 del informe); η_ε no cambia. Cierre de los tres puntos del §4: `protocol/enmienda-6.md`, sección "Erratas de trazabilidad" del informe, `results/lorenz-checkpoints-salida.txt`, `results/ruido-oos-semilla-salida.txt`. Los archivos `*:Zone.Identifier` ya no existían al ejecutar el borrado (habían desaparecido a las 16:40).

## 5. Conclusión

Herencia verificada. El instrumento reproduce todas las salidas con semilla; el control sin semilla se comporta cualitativamente igual. Los tres puntos del §4 se trasladan a `PENDIENTES.md` y a la sección de limitaciones del preprint.

---

*Historia: v1 (2026-08-26) — registro inicial, redactado por el asistente de IA bajo supervisión de Maximiliano Winter, como parte del hito 1.*

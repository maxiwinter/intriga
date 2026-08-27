# Informe de validación — `preprint-v0-3.md`

**Fecha:** 2026-08-26. **Objeto validado:** `docs/preprint/preprint-v0-3.md` (11.476 palabras). **Referencia de contraste:** `results/*.txt`, `docs/piloto-seccion-10-1-informe-final.md`, `protocol/changelog-v1-0-a-v1-1.md`, `protocol/enmienda-6.md`.

**Convención de estados:** ✅ cumplido y verificado — ⚠️ cumplido **con reserva declarada en el propio preprint** — ❌ incumplido. No se usa ✅ para nada que dependa de una acción humana pendiente.

---

## Checklist

### ⚠️ ρ_MDL usa baseline completo
**Corregido en la definición; las cifras publicadas todavía no.** §4.3 define `ρ = C / L₀^full` con `L₀^full = L_U(M₀) + L_U(D_ε|M₀)` y explica por qué el baseline desnudo no sirve. **Reserva, declarada en §4.3 y §7.5 bis:** el código del piloto nunca define `L_U(M₀)`, de modo que **todos los ρ de §6 siguen normalizados por el residuo literal**. No se inventó un valor de `L_U(M₀)` ni se ajustó ninguna cifra. La diferencia es de orden `L(M₀)/L₀` — centenares de bits sobre 10⁵–10⁶ — y cae bajo el redondeo de las tablas, pero existe. *Acción pendiente 1 del changelog.*

### ⚠️ ρ_MDL ≤ 1 queda formalmente garantizado
**Garantizado en la definición.** Con M₀ miembro de la familia, `C ≤ L_U(M₀) + L_U(D_ε|M₀) = L₀^full`, luego `ρ ≤ 1` es consecuencia exacta y `ρ = 1` se alcanza cuando gana M₀. Se eliminó la frase falsa "By construction ρ_MDL ≤ 1" (0 ocurrencias de "By construction" en v0.3) y se sustituyó por la versión condicionada al baseline completo. **Reserva:** la garantía rige para las cifras futuras calculadas con `L₀^full`; las de §6 heredan la cota vieja `1 + L(M₀)/L₀`. El texto lo dice en §7.5 bis en lugar de silenciarlo.

### ⚠️ g_pred y g_total no están mezclados
**Separados en todo el texto.** §4.5 define ambos, con las tres consecuencias explícitas (`g_total > g_pred` siempre; `g_total > 1` posible con predicción perfecta si el bloque de test es chico; ninguna cifra se cita como `g` a secas). Búsqueda global: **0 ocurrencias de `g =` y 0 de `g(T)`**. Valores re-etiquetados: R110/R30 → `g_pred = 0`, `g_total = 0.0088`; urandom → `g_pred ≈ 1`, `g_total = 1.009`; PCG64 semilla 2026 → `g_total = 1.0088`. **Reserva, declarada en §6.2 y §7.5 bis:** los scripts imprimen **solo `g_total`**; los `g_pred` se derivan del error de test archivado (0 % → residuo 0 bits; ≈50 % → 1 bit/celda) y están marcados como **derivados, no impresos**. *Acción pendiente 2.*

### ✅ Los valores del piloto fueron contrastados con los scripts
Contraste cifra por cifra (tabla al final): **33 de 35 cantidades aparecen literalmente en `results/*.txt`**. Las dos restantes, **1288** (= 1096 + 192, Track A) y **1248** (= 156 × 8, Track B a n = 20 000), son sumas aritméticas de cantidades impresas; el preprint remite a `results/lorenz-checkpoints-salida.txt` para ambos sumandos. Bajo lectura estricta de la Enmienda 6 convendría que el script imprimiera también los subtotales por track (añadido a las acciones pendientes).

### ✅ 2655 no se llama "Lyapunov horizon"
Las cuatro ocurrencias de 2655 en v0.3 son: (a) §4.7, como uno de los valores medidos de `h(p, ε)` en la serie 3194/2655/2655/2655/2458; (b) §6.3, como `h(52, 8 bits) = 2655 measured steps`; (c)–(d) §6.4, en la verificación del piso. **Ninguna lo llama horizonte de Lyapunov.** Las dos ocurrencias de la expresión "Lyapunov horizon" que quedan son deliberadas y de signo contrario: §4.7 dice que `h(p,ε)` **no debe identificarse** con él, y la historia de versiones registra el reemplazo. §4.7 añade el argumento del piloto: un horizonte que no se mueve mientras cambia la resolución es firma de piso aritmético, no de tiempo de Lyapunov.

### ⚠️ Track A y Track B están separados
**Separados y cuantificados** en la tabla nueva de §6.3: Track A = 1288 bits fijos (no crece con n); Track B = 156·⌈n/h⌉ = 156, 156, 312, 624, 1248 bits; suma = C archivado; la regla cae del 89 % al 51 % de la descripción entre n = 1000 y n = 20 000. Se agregó además, en §6.6, la separación explícita entre **claims metrológicos** (todo §6) y **claims sobre la naturaleza** (ninguno hasta §8). **Reserva:** "Track" se interpretó como el **nivel descriptivo A/B del protocolo**, que es la distinción en la que las cifras del piloto se descomponen. La lectura queda marcada como no verificada en **§7.8** del propio preprint. *Acción pendiente 4.*

### ✅ No se afirma preregistro público si no existe
Retiradas todas las afirmaciones de depósito o congelamiento consumados. Nota al pie del título: "preregistered" describe la disciplina de diseño, **no** un depósito; "protocol v1.1 has **not** been frozen and **no public preregistration exists**". Abstract: "written to be preregistered — freezing and public deposit still pending". §5.8 abre con la advertencia en negrita. §8.5: "Once frozen…". §9: "preregistration-ready". Data availability: "**No preregistration record exists yet to cite**". Búsquedas de control: **0 ocurrencias** de "preregistered protocol" como afirmación de hecho, de "v1.1, frozen" y de "The frozen protocol". **No se inventó hash, identificador de registro ni fecha de depósito.**

### ✅ No se fortalecieron claims de originalidad
La reivindicación central conserva su formulación literal ("*to the best of our knowledge, previous work has studied … separately, but has not combined them…*"). El mapa de originalidad de §3.6 conserva su distribución exacta de categorías: **7 "not original", 1 "close antecedent", 2 "possible novelty" (una marcada "unconfirmed"), 1 "most defensible contribution"**. η_ε sigue como posible novedad **no confirmada**, con §7.9 declarando que la búsqueda bibliográfica no se hizo. La frase "This is not a new theory of the compressibility of the universe" permanece. Los cambios de C7 y C8 **debilitan** claims; ninguno los refuerza.

### ✅ Todas las referencias `[VERIFY]` siguen marcadas
**33 marcas en v0.2, 33 en v0.3.** Ninguna referencia fue promovida a verificada; ningún dato bibliográfico dudoso fue completado. Las dos referencias sin localizar (Leyva-Acosta et al. 2026; regresión simbólica + MDL en astrofísica 2026) siguen señaladas como no verificadas, igual que la de Wheeler, cuyos datos permanecen en blanco.

### ✅ Ninguna limitación fue eliminada
§7 pasó de **8 a 10 subsecciones**: se conservan íntegras 7.1 (discrepancia 64/76.5 sin causa asignada), 7.2 (una sola metaclase, no dos U_ref), 7.3 (datos autogenerados con oráculo), 7.4 (η_ε solo en dos controles continuos), 7.5 (huecos de trazabilidad y su cierre), 7.6 (decisiones abiertas del protocolo), 7.7 (método multi-IA y revisión humana obligatoria); y se **agregan** 7.5 bis (deudas numéricas de C1, C2, C3 y C5) y 7.8 (lectura de Track A/B no verificada). La antigua 7.8 pasa a 7.9 sin cambios de contenido. §6.6 ("What the pilot does NOT show") permanece íntegra y reforzada.

### ✅ Ninguna cifra experimental fue inventada
No se ejecutó ningún experimento nuevo para esta revisión. Toda cifra de §6 procede de `results/*.txt` (tabla de contraste). Los únicos números que no se leen literalmente de una salida son 1288 y 1248, sumas declaradas de sumandos archivados. Los valores `g_pred` = 0 y ≈ 1 se marcan como derivados en el propio texto. La corrección 1400 → 1288 **cambia una cifra hacia el valor trazado**, no hacia uno nuevo. `L_U(M₀)` **no se inventó**, y por eso los ρ no se recalcularon.

---

## Búsquedas globales solicitadas (sobre `preprint-v0-3.md`)

| Término | Ocurrencias | Resolución |
|---|---|---|
| `g =` | 0 | Eliminado: todo es `g_pred` o `g_total`. |
| `g(T)` | 0 | Eliminado; `G(T)` (bits, no ratio) se conserva y está definido. |
| `rho` / `ρ` | — | Toda ocurrencia es `r_generic`, `ρ_oracle`, `ρ_MDL` o `ρ` genérico ya definido con `L₀^full`. |
| `2655` | 4 | Ninguna como "Lyapunov horizon"; todas como `h(p,ε)` medido o piso float64. |
| `Lyapunov horizon` | 2 | Ambas deliberadas: §4.7 lo distingue de `h(p,ε)`; la historia registra el reemplazo. |
| `preregistered` | varias | Todas como disciplina de diseño o descripción del protocolo a preregistrar; ninguna afirma depósito. Nota del título lo fija. |
| `frozen` | varias | Ninguna afirma que el protocolo esté congelado; §8.5 usa "Once frozen"; §4.2 "family frozen in advance" y §6.2 "rule … frozen" se refieren a modelos, no al protocolo. El marco v5.2 sí está congelado y así se dice. |
| `Rydberg` | 1 | En la restricción reformulada sobre primitivas (§8.2). |
| `does not contain the answer` | 1 | Solo en la historia de versiones, citando el texto **retirado**. |
| `not settled` | 0 | Reemplazado por "did not converge". |
| `could not be` | 1 | Solo en la historia de versiones, citando la frase **retirada**. |

## Contraste cifra por cifra

Todas verificadas contra `results/`: r_generic 0.5307 / 0.5019 / 1.0009 / 1.0005 / 0.9945 / 0.9261 · ρ 0.0053 / 0.0107 / 0.0018 · checkpoints 0.0602 / 0.0241 / 0.0133 / 0.0080 / 0.0053 · codificador ingenuo 0.057 / 0.024 / 0.48 / 0.74 / 0.87 · constantes 1096 / 192 / 156 / 2536 · horizontes 2655 y 3194 / 2655 / 2458 · matches 2699 / 3052 / 4228 / 5011 · pendientes 64.2 / 67.6 / 29.4 / 98.0 / 65.2 / 66.1 / 76.5 · barrido 0.0267 / 0.0178 / 0.0133 / 0.0107 / 0.0098 · η_ε 0 / 0 / 0 / 0.0052 · g_total 0.0088 / 1.009 / 1.0088 · p_error 0.5001. **Derivadas por suma:** 1288 (1096+192) y 1248 (156×8).

## Integridad del repositorio

`sha256sum` de `protocol/*`, `src/*.py` y `results/*.txt` antes y después de esta revisión: **sin cambios**. `preprint-v0-1.md` (v0.2) conservado sin modificación alguna. No se ejecutó el experimento de espectros; no se tocó ningún dataset; no se modificó el protocolo.

## Veredicto

**7 ✅ · 4 ⚠️ · 0 ❌.** Las cuatro reservas son las mismas tres deudas — `L_U(M₀)` sin definir, `g_pred` sin imprimir, lectura de Track A/B sin confirmar — y todas están declaradas dentro del preprint, no solo aquí. El documento es internamente consistente y **no contiene ninguna afirmación que sus propios archivos no sostengan**. No es publicable todavía: faltan las 8 acciones humanas del changelog, empezando por la verificación de las 33 referencias y la revisión humana experta.

---

*Historia: v1 (2026-08-26) — redactado por el asistente de IA bajo supervisión de Maximiliano Winter.*

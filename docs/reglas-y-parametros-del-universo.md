# El archivo comprimido del universo

**Dos ecuaciones y unos treinta y dos números.** Eso es todo lo que hace falta, hoy, para describir cuantitativamente el universo conocido: desde la desintegración de un núcleo hasta la colisión de dos agujeros negros a mil millones de años luz.

Este documento reúne esas reglas y esos parámetros, y —más importante— marca con precisión dónde termina la compresión.

---

## 1. Por qué hay tan pocas reglas: el teorema de Noether

Antes de la lista conviene el principio que la genera, porque las leyes no son un inventario arbitrario que la naturaleza casualmente cumple.

**Teorema de Noether (Emmy Noether, 1918):** toda simetría continua de un sistema físico produce una cantidad conservada.

| Simetría | Cantidad conservada |
|---|---|
| Traslación en el tiempo | Energía |
| Traslación en el espacio | Momento lineal |
| Rotación | Momento angular |
| Fase global U(1) | Carga eléctrica |
| Fase local (gauge) | Estructura de las fuerzas mismas |

Esto es lo que hace posible la compresión. No hay que enumerar las leyes: hay que enumerar las **simetrías**, y las leyes caen solas. Las cuatro fuerzas conocidas son consecuencia de exigir invariancia local bajo tres grupos: SU(3) × SU(2) × U(1).

---

## 2. Las dos reglas

### 2.1 Modelo Estándar de partículas

Todo el contenido no gravitatorio del universo se escribe como un único lagrangiano. En forma compacta:

```
𝓛 = −¼ Fμν F^μν            (campos de fuerza)
    + i ψ̄ D̸ ψ + h.c.        (materia y su movimiento)
    + ψ̄ᵢ yᵢⱼ ψⱼ φ + h.c.     (materia acoplada al Higgs → masas)
    + |Dμ φ|² − V(φ)         (el campo de Higgs consigo mismo)
```

Cuatro términos. Cubren el electromagnetismo, la fuerza nuclear fuerte, la fuerza nuclear débil, y todas las partículas conocidas: 6 quarks, 6 leptones, 4 bosones de gauge y el Higgs.

**Grupo de simetría:** SU(3)_C × SU(2)_L × U(1)_Y

### 2.2 Relatividad general

La gravedad queda afuera del Modelo Estándar y se describe con las ecuaciones de campo de Einstein (1915):

```
Gμν + Λ gμν = (8πG / c⁴) Tμν
```

A la izquierda, la geometría del espaciotiempo. A la derecha, la materia y la energía. Diez ecuaciones acopladas escritas en una línea.

### 2.3 Un tercer principio, sin ecuación propia

**Unitariedad.** La evolución cuántica se escribe |ψ(t)⟩ = U(t)|ψ(0)⟩ con la condición U†U = I. El operador es invertible: toda evolución hacia adelante tiene exactamente una inversa. La información no se destruye. La entropía de von Neumann de un sistema cerrado no cambia; lo que crece es la entropía *aparente*, la que se mide cuando se observa una parte y no el todo.

---

## 3. Los parámetros

Ninguno de estos números se deduce de la teoría. Se miden y se cargan a mano.

### 3.1 Modelo Estándar — 19 parámetros

**Masas de fermiones cargados (9)**

| Partícula | Masa aproximada |
|---|---|
| Quark up | 2,2 MeV |
| Quark down | 4,7 MeV |
| Quark strange | 93 MeV |
| Quark charm | 1,27 GeV |
| Quark bottom | 4,18 GeV |
| Quark top | 172,7 GeV |
| Electrón | 0,511 MeV |
| Muón | 105,7 MeV |
| Tau | 1776,9 MeV |

Notar el rango: del quark up al quark top hay cinco órdenes de magnitud, sin explicación.

**Constantes de acoplamiento (3)** — las intensidades de las tres fuerzas

- Electromagnética: α ≈ 1/137,036
- Fuerte: α_s(M_Z) ≈ 0,118
- Débil / ángulo de Weinberg: sin²θ_W ≈ 0,231

**Matriz CKM (4)** — cómo se mezclan los quarks entre generaciones: tres ángulos de mezcla y una fase que introduce violación de CP.

**Sector de Higgs (2)** — valor esperado del vacío v ≈ 246 GeV, masa del Higgs ≈ 125,25 GeV.

**Ángulo theta de QCD (1)** — experimentalmente compatible con cero, |θ| < 10⁻¹⁰. Que sea tan chico sin razón conocida es el *problema CP fuerte*.

### 3.2 Neutrinos — 7 parámetros más

Tres masas (aún no medidas individualmente; se conocen las diferencias al cuadrado), tres ángulos de mezcla y una fase CP. Si los neutrinos resultaran ser partículas de Majorana, se agregan dos fases más.

Este sector es el agregado más reciente: hasta el descubrimiento de las oscilaciones de neutrinos (1998) se los suponía sin masa.

### 3.3 Cosmología — 6 parámetros

El modelo ΛCDM describe el universo entero —expansión, edad, composición, formación de estructura— con seis números:

| Parámetro | Qué es | Valor (Planck 2018) |
|---|---|---|
| Ω_b h² | Densidad de materia bariónica | ≈ 0,0224 |
| Ω_c h² | Densidad de materia oscura fría | ≈ 0,120 |
| 100 θ* | Escala angular del horizonte de sonido | ≈ 1,0411 |
| τ | Profundidad óptica de reionización | ≈ 0,054 |
| ln(10¹⁰ A_s) | Amplitud de las fluctuaciones primordiales | ≈ 3,04 |
| n_s | Índice espectral | ≈ 0,965 |

**Derivados de esos seis** (no son parámetros libres): H₀ ≈ 67,4 km/s/Mpc, edad del universo ≈ 13.800 millones de años, Ω_Λ ≈ 0,685, Ω_m ≈ 0,315.

### 3.4 Constantes dimensionales

c, ħ, G, k_B no son parámetros libres en el mismo sentido: fijan sistemas de unidades. En unidades de Planck valen 1. Lo que tiene contenido físico son las combinaciones adimensionales, como α.

### 3.5 Los 32 números, en una sola lista

La cuenta completa: 19 (Modelo Estándar) + 7 (neutrinos) + 6 (cosmología).

| # | Parámetro | Valor |
|---|---|---|
| 1 | Masa del electrón | 0,511 MeV |
| 2 | Masa del muón | 105,66 MeV |
| 3 | Masa del tau | 1776,9 MeV |
| 4 | Masa del quark up | ≈ 2,2 MeV |
| 5 | Masa del quark down | ≈ 4,7 MeV |
| 6 | Masa del quark strange | ≈ 93 MeV |
| 7 | Masa del quark charm | 1,27 GeV |
| 8 | Masa del quark bottom | 4,18 GeV |
| 9 | Masa del quark top | 172,7 GeV |
| 10 | Acoplamiento electromagnético (α) | 1/137,036 |
| 11 | Acoplamiento fuerte (α_s a M_Z) | 0,1180 |
| 12 | Acoplamiento débil (sin²θ_W) | 0,2312 |
| 13 | CKM — ángulo θ₁₂ | ≈ 13,0° |
| 14 | CKM — ángulo θ₂₃ | ≈ 2,4° |
| 15 | CKM — ángulo θ₁₃ | ≈ 0,20° |
| 16 | CKM — fase CP δ | ≈ 68° |
| 17 | Valor esperado del vacío (v) | 246,2 GeV |
| 18 | Masa del Higgs | 125,25 GeV |
| 19 | Ángulo theta de QCD | < 10⁻¹⁰ *(solo cota)* |
| 20 | Masa del neutrino 1 | *no medida* |
| 21 | Masa del neutrino 2 | *no medida* |
| 22 | Masa del neutrino 3 | *no medida* |
| 23 | PMNS — ángulo θ₁₂ | ≈ 33,4° |
| 24 | PMNS — ángulo θ₂₃ | ≈ 49° |
| 25 | PMNS — ángulo θ₁₃ | ≈ 8,6° |
| 26 | PMNS — fase CP δ | ≈ 195° *(mal determinada)* |
| 27 | Ω_b h² — densidad de bariones | 0,0224 |
| 28 | Ω_c h² — densidad de materia oscura | 0,120 |
| 29 | 100 θ* — horizonte de sonido | 1,0411 |
| 30 | τ — profundidad óptica de reionización | 0,054 |
| 31 | ln(10¹⁰ A_s) — amplitud primordial | 3,04 |
| 32 | n_s — índice espectral | 0,965 |

**Sobre las masas de los neutrinos (20–22):** individualmente son desconocidas. Solo se conocen las diferencias de sus cuadrados —Δm²₂₁ ≈ 7,5 × 10⁻⁵ eV², |Δm²₃₁| ≈ 2,5 × 10⁻³ eV²— y una cota a la suma, Σm < 0,12 eV. Ni siquiera está resuelto el orden (jerarquía normal o invertida).

#### Tres advertencias sobre esta lista

1. **El 32 no es sagrado.** Depende de la convención. Tegmark, Aguirre, Rees y Wilczek cuentan 31 en su censo de 2006 (*Phys. Rev. D* 73, 023505) porque normalizan todo a magnitudes adimensionales y eligen un conjunto cosmológico distinto. Si los neutrinos resultaran ser partículas de Majorana, se agregan dos fases y son 34. Lo que nadie discute es el orden de magnitud: son treinta y pico.

2. **Siete de los treinta y dos no están medidos.** Las tres masas de neutrinos, la fase CP del sector PMNS con precisión, y el ángulo theta de QCD, que solo tiene cota superior. No terminamos de leer el archivo.

3. **El que no aparece: Λ.** La constante cosmológica no figura como entrada independiente porque en ΛCDM se deriva de las otras (Ω_Λ ≈ 0,685). Pero es la que tiene el problema más grave: la teoría cuántica de campos la predice entre 60 y 120 órdenes de magnitud más grande que lo observado.

---

## 4. Dónde termina la compresión

Este es el punto de todo el documento.

**Las reglas se comprimen brutalmente. Los parámetros no se comprimen nada.** Con una precisión de alcance: donde aquí se dice que la compresión "termina", debe leerse que termina *la compresión conseguida por nuestras teorías actuales*. Si una teoría más profunda derivara los parámetros, pasarían a ser ley; si dependieran de una elección de vacío, pasarían a ser estado. La frontera describe el conocimiento de hoy, no una ontología demostrada.

1. **Ningún parámetro está explicado.** No sabemos por qué el electrón pesa lo que pesa. Son hechos brutos con valor decimal: la teoría anda perfectamente sin dar razón de ellos.

2. **El problema de la constante cosmológica.** El valor observado de Λ está entre 60 y 120 órdenes de magnitud por debajo de lo que la teoría cuántica de campos predice de forma ingenua. Se la ha llamado la peor predicción de la historia de la física. El modelo funciona igual.

3. **Las dos teorías no se hablan.** Relatividad general y mecánica cuántica son incompatibles donde ambas hacen falta a la vez: la singularidad de un agujero negro, el universo antes del tiempo de Planck (10⁻⁴³ s). Ahí la descripción se apaga.

4. **La flecha del tiempo no está en las leyes.** Las ecuaciones microscópicas son simétricas respecto del tiempo. La irreversibilidad que experimentamos no viene de la dinámica: viene de que el estado inicial del universo tenía una entropía absurdamente baja. Es una **condición de borde**, no una ley.

5. **95% del contenido es desconocido.** Materia oscura (~27%) y energía oscura (~68%) están parametrizadas, no entendidas. Todo el Modelo Estándar describe alrededor del 5% del contenido energético del universo.

6. **Tensión de Hubble.** El valor de H₀ derivado del fondo cósmico de microondas (≈67 km/s/Mpc) no coincide con el medido en el universo cercano (≈73). La discrepancia lleva años sin resolverse y podría indicar física nueva.

---

## 5. Lo que queda en pie

El universo conocido se deja escribir en dos ecuaciones y treinta y dos números. Eso no era obligatorio: un mundo detallado hasta el fondo, con reglas distintas en cada región, irreductible a resumen, es perfectamente concebible.

La pregunta que este documento deja abierta no es qué dicen las reglas. Es **por qué hay tan pocas** —y si esa escasez es una propiedad del mundo o del recorte que llamamos mundo.

---

### Fuentes de referencia

- *Review of Particle Physics*, Particle Data Group (edición vigente) — valores de partículas y acoplamientos.
- Planck Collaboration, *Planck 2018 results VI: Cosmological parameters* — sector cosmológico.
- Los valores citados son aproximados y se actualizan; para trabajo de precisión conviene ir a la fuente.

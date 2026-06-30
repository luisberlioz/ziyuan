# Logaritmos, Expresiones Logarítmicas y Ecuaciones

---

## 1. Logaritmos

### 1.1 Definición

El **logaritmo** de un número $N$ en una **base** $b$ es el **exponente** $x$ al cual hay que elevar la base para obtener dicho número.

$$
\log_b N = x \quad \Longleftrightarrow \quad b^x = N
$$

Donde se llaman:

- **$b$** → base del logaritmo (con $b > 0$ y $b \neq 1$)
- **$N$** → argumento o antilogaritmo (con $N > 0$)
- **$x$** → logaritmo

**Se lee:** *"logaritmo en base $b$ de $N$ es igual a $x$"*, o bien *"logaritmo base $b$ de $N$ vale $x$"*.

> **Restricciones fundamentales:**
> - La base debe ser positiva y distinta de 1: $b > 0$, $b \neq 1$.
> - El argumento debe ser estrictamente positivo: $N > 0$.
>
> Esto se deduce de la definición: $b^x$ con $b > 0$ nunca produce un resultado $\leq 0$, así que $N$ tiene que ser positivo.

---

### 1.2 Casos particulares importantes

| Nombre | Definición | Equivalencia exponencial |
|--------|------------|--------------------------|
| **Logaritmo común (decimal)** | $\log N = \log_{10} N$ | $10^x = N$ |
| **Logaritmo natural** | $\ln N = \log_e N$ | $e^x = N$,  con $e \approx 2.71828$ |
| **Logaritmo de la base** | $\log_b b$ | $b^1 = b$,  así que $= 1$ |
| **Logaritmo de 1** | $\log_b 1$ | $b^0 = 1$,  así que $= 0$ |

---

### 1.3 Conversión entre forma logarítmica y exponencial

Pasar de una forma a la otra es directo aplicando la definición.

#### De logarítmica a exponencial

Dada la igualdad $\log_b N = x$, se reescribe como $b^x = N$.

**Ejemplo 1:**

```
log₂ 32 = 5    ⟹    2⁵ = 32
```

**Ejemplo 2:**

```
log₅ 625 = 4   ⟹    5⁴ = 625
```

**Ejemplo 3:**

```
log₃ (1/9) = −2   ⟹    3⁻² = 1/9
```

#### De exponencial a logarítmica

Dada la igualdad $b^x = N$, se reescribe como $\log_b N = x$.

**Ejemplo 1:**

```
4³ = 64         ⟹    log₄ 64 = 3
```

**Ejemplo 2:**

```
10⁻² = 0.01     ⟹    log 0.01 = −2
```

**Ejemplo 3:**

```
eˣ = 7          ⟹    ln 7 = x
```

#### Relación fundamental

La conversión logaritmo ↔ exponencial es la base de todas las propiedades y operaciones siguientes. Toda propiedad logarítmica tiene su equivalente inmediato en notación exponencial.

---

### 1.4 Fórmula de cambio de base

Permite calcular un logaritmo en **cualquier base** si se dispone de logaritmos en otra base (típicamente base 10 o base $e$).

$$
\log_b N \ = \ \frac{\log_c N}{\log_c b}
$$

En particular, usando logaritmos decimales y naturales:

$$
\log_b N \ = \ \frac{\log N}{\log b} \ = \ \frac{\ln N}{\ln b}
$$

**Ejemplo 1 — calcular $\log_2 50$ usando decimales:**

```
log₂ 50  =  log 50 / log 2
         =  1.69897 / 0.30103
         ≈  5.6439
```

**Verificación:**  $2^{5.6439} \approx 50$ ✓

**Ejemplo 2 — calcular $\log_3 100$ usando naturales:**

```
log₃ 100  =  ln 100 / ln 3
          =  4.60517 / 1.09861
          ≈  4.1918
```

**Verificación:**  $3^{4.1918} \approx 100$ ✓

**Ejemplo 3 — cambio a la base del argumento:**

```
log_a b · log_b c · log_c a  =  1
```

Demostración: aplicando cambio de base, cada producto cancela el siguiente denominador, y el resultado es $1$. Esto es útil en identidades donde aparecen "cadenas" de logaritmos.

---

### 1.5 Propiedades de los logaritmos

Sean $b > 0$, $b \neq 1$, $M > 0$, $N > 0$, y $r \in \mathbb{R}$.

| # | Propiedad | Fórmula |
|---|-----------|---------|
| 1 | **Logaritmo de un producto** | $\log_b (M \cdot N) = \log_b M + \log_b N$ |
| 2 | **Logaritmo de un cociente** | $\log_b (M / N) = \log_b M - \log_b N$ |
| 3 | **Logaritmo de una potencia** | $\log_b (N^r) = r \cdot \log_b N$ |
| 4 | **Logaritmo de una raíz** | $\log_b \sqrt[r]{N} = \dfrac{1}{r}\log_b N$ |
| 5 | **Logaritmo de la base** | $\log_b b = 1$ |
| 6 | **Logaritmo de 1** | $\log_b 1 = 0$ |
| 7 | **Cambio de base** | $\log_b N = \dfrac{\log_c N}{\log_c b}$ |
| 8 | **Inversa** | $b^{\log_b N} = N$ |
| 9 | **Logaritmo de una potencia de la base** | $\log_b (b^r) = r$ |

**Demostración rápida de la propiedad 1 (producto):**

Sean $\log_b M = x$ y $\log_b N = y$. Entonces $M = b^x$ y $N = b^y$.

```
M · N  =  b^x · b^y  =  b^(x+y)

Por definición:
log_b (M · N)  =  x + y  =  log_b M + log_b N  ✓
```

Las propiedades 2, 3 y 4 se demuestran análogamente.

---

### 1.6 Ejemplos de aplicación directa

**Ejemplo 1:** Calcular $\log_2 8 \cdot \log_3 27$

```
log₂ 8 = 3       (porque 2³ = 8)
log₃ 27 = 3      (porque 3³ = 27)

Producto = 3 × 3 = 9
```

**Ejemplo 2:** Si $\log_b 2 = 0.43$ y $\log_b 3 = 0.68$, hallar $\log_b 6$.

```
log_b 6  =  log_b (2 · 3)
         =  log_b 2 + log_b 3
         =  0.43 + 0.68
         =  1.11
```

**Ejemplo 3:** Si $\log_b 5 = 0.83$, hallar $\log_b \sqrt{5}$.

```
log_b √5  =  log_b (5^(1/2))
          =  (1/2) · log_b 5
          =  (1/2) · 0.83
          =  0.415
```

**Ejemplo 4:** Calcular $\log 1000 - \log 10$.

```
log 1000  =  3       (porque 10³ = 1000)
log 10    =  1

Diferencia  =  3 − 1  =  2
```

Y verificamos por la propiedad de cociente: $\log(1000/10) = \log 100 = 2$. ✓

---

## 2. Expresiones Logarítmicas

Una **expresión logarítmica** es una combinación de varios logaritmos conectados por sumas, restas, productos y cocientes. Trabajamos con ellas en tres sentidos:

- **Simplificar** → convertir una expresión compleja en una más compacta.
- **Expandir** → descomponer un logaritmo en suma/resta de varios.
- **Reducir a un solo término** → dejar todo como un único $\log$ (o como un número).

---

### 2.1 Simplificación

Se trata de **comprimir** varios logaritmos en uno solo, usando las propiedades en sentido inverso al de la expansión.

**Ejemplo 1:**

```
log a + log b − log c  =  log (a · b / c)
```

**Ejemplo 2:**

```
2 log x − 3 log y + (1/2) log z  =  log (x² · z^(1/2) / y³)
                                    =  log (x² √z / y³)
```

**Ejemplo 3:** Simplificar $\log 6 + \log 5 - 2\log 3 - \log 2$.

```
=  log 6 + log 5 − log 3² − log 2
=  log (6 · 5) − log (9 · 2)
=  log 30 − log 18
=  log (30 / 18)
=  log (5 / 3)
```

**Ejemplo 4:** Simplificar $\ln(e^3) + \ln(\sqrt{e})$.

```
=  3 · ln e + (1/2) · ln e
=  3 · 1 + (1/2) · 1
=  7/2
```

---

### 2.2 Expansión

Se trata de **descomponer** un logaritmo de un producto/cociente/potencia en una suma/resta de varios logaritmos.

**Regla práctica:**
- Producto → suma de logaritmos.
- Cociente → resta de logaritmos.
- Exponente → coeficiente multiplicando al logaritmo.

**Ejemplo 1:** Expandir $\log(x^2 y / z)$.

```
=  log(x² y) − log z
=  log(x²) + log y − log z
=  2 log x + log y − log z
```

**Ejemplo 2:** Expandir $\ln\left(\dfrac{a^3 \sqrt{b}}{c^2}\right)$.

```
=  ln(a³ √b) − ln(c²)
=  ln(a³) + ln(√b) − 2 ln c
=  3 ln a + (1/2) ln b − 2 ln c
```

**Ejemplo 3:** Expandir $\log\left(\dfrac{(x+1)^2}{\sqrt{x^2+1}}\right)$.

```
=  2 log(x+1) − (1/2) log(x² + 1)
```

**Ejemplo 4:** Expandir $\log_b\left(\sqrt[3]{\dfrac{p^2 q}{r^5}}\right)$.

```
=  log_b(p²q) − log_b(r⁵), todo multiplicado por 1/3
=  (1/3) [ 2 log_b p + log_b q − 5 log_b r ]
```

---

### 2.3 Reducción a un solo término

El objetivo es dejar **toda la expresión como un único logaritmo** (o, si es posible, como un número puro).

**Ejemplo 1:** Reducir $\log 5 + \log 4$.

```
=  log(5 · 4)
=  log 20
```

**Ejemplo 2:** Reducir $2 \log x - \log y$.

```
=  log(x²) − log y
=  log(x² / y)
```

**Ejemplo 3:** Reducir $\frac{1}{2}\log a - 2\log b + 3\log c$.

```
=  log(√a) − log(b²) + log(c³)
=  log( c³ √a / b² )
```

**Ejemplo 4:** Reducir $3 \log_2(x-1) - \frac{1}{2}\log_2(x+1)$.

```
=  log₂[(x−1)³] − log₂[√(x+1)]
=  log₂[ (x−1)³ / √(x+1) ]
```

**Ejemplo 5 (hasta un número):** Reducir $\log 8 + \log 125 - 2\log 5$.

```
=  log(8 · 125) − log(5²)
=  log 1000 − log 25
=  log(1000 / 25)
=  log 40
```

**Ejemplo 6 (hasta un número):** Reducir $2 \log_5 3 - \log_5 9$.

```
=  log_5(3²) − log_5 9
=  log_5 9 − log_5 9
=  0
```

---

### 2.4 Consejos prácticos

1. **Trabaja con las propiedades en el orden correcto:** convierte cocientes a restas, productos a sumas, potencias en coeficientes.
2. **Factoriza cuando puedas.** Si ves números como 8, 27, 100, exprésalos como potencias (8 = 2³, 100 = 10²) para identificar cancelaciones.
3. **Mantén el dominio en mente.** Cualquier expresión intermedia debe tener argumento positivo.
4. **Cambio de base como último recurso** — solo si te piden el valor numérico o si la base no es uniforme.

---

## 3. Ecuaciones Exponenciales

Una **ecuación exponencial** es aquella en la que la incógnita aparece en el **exponente**. La idea central es **igualar bases** y luego igualar exponentes.

---

### 3.1 Método 1: Igualar bases

Si podemos expresar ambos lados como potencias de la **misma base**, entonces los exponentes deben ser iguales.

**Procedimiento:**
1. Reescribir ambos miembros con la misma base.
2. Igualar los exponentes.
3. Resolver la ecuación algebraica resultante.

**Ejemplo 1:** Resolver $2^x = 8$.

```
2^x  =  2³

Por igualdad de exponentes:
x  =  3
```

**Ejemplo 2:** Resolver $3^{x-1} = 81$.

```
3^(x−1)  =  3⁴

x − 1  =  4
x  =  5
```

**Ejemplo 3:** Resolver $4^x = 32$.

```
Reescribimos con base 2:
4^x  =  (2²)^x  =  2^(2x)
32   =  2⁵

2^(2x)  =  2⁵
2x  =  5
x  =  5/2
```

**Ejemplo 4:** Resolver $9^x \cdot 27^{x-1} = 3^{x+2}$.

```
9^x       =  (3²)^x  =  3^(2x)
27^(x−1)  =  3^(3(x−1))  =  3^(3x−3)

3^(2x) · 3^(3x−3)  =  3^(x+2)
3^(5x − 3)          =  3^(x+2)

5x − 3  =  x + 2
4x  =  5
x  =  5/4
```

**Ejemplo 5:** Resolver $\dfrac{8^{x+1}}{2^x} = 16$.

```
8^(x+1)  =  (2³)^(x+1)  =  2^(3x+3)
2^x      =  2^x

Cociente:
2^(3x+3) / 2^x  =  2^(2x+3)

2^(2x+3)  =  16  =  2⁴
2x + 3   =  4
2x       =  1
x        =  1/2
```

**Ejemplo 6:** Resolver $\left(\dfrac{2}{3}\right)^{x^2 - 5x + 6} = 1$.

Recordemos que $a^0 = 1$ para cualquier $a > 0$, $a \neq 1$. Por tanto el exponente debe ser cero:

```
x² − 5x + 6  =  0
(x − 2)(x − 3)  =  0
x = 2   o   x = 3
```

---

### 3.2 Método 2: Tomar logaritmo

Cuando **no es posible igualar las bases** directamente (típicamente cuando aparece un número "raro" como 7, 11, etc.), tomamos logaritmo a ambos lados.

**Procedimiento:**
1. Aplicar $\log$ (o $\ln$) a ambos miembros.
2. Usar la propiedad $\log(a^x) = x \log a$ para bajar la incógnita.
3. Resolver la ecuación algebraica.

**Ejemplo 1:** Resolver $5^x = 17$.

```
Aplicamos ln a ambos lados:
ln(5^x)  =  ln 17
x · ln 5  =  ln 17

x  =  ln 17 / ln 5
   ≈  2.8332 / 1.6094
   ≈  1.7604
```

**Ejemplo 2:** Resolver $3^{2x-1} = 50$.

```
ln(3^(2x−1))  =  ln 50
(2x − 1) · ln 3  =  ln 50

2x − 1  =  ln 50 / ln 3
2x      =  1 + (ln 50 / ln 3)
2x      =  1 + 3.5609
x       ≈  2.2805
```

**Ejemplo 3:** Resolver $7 \cdot 2^x = 3^{x+1}$.

```
Aplicamos ln:
ln 7 + x ln 2  =  (x + 1) ln 3
ln 7 + x ln 2  =  x ln 3 + ln 3

x ln 2 − x ln 3  =  ln 3 − ln 7
x (ln 2 − ln 3)  =  ln(3/7)

x  =  ln(3/7) / ln(2/3)
   ≈  −0.8473 / −0.4055
   ≈  2.0897
```

**Ejemplo 4:** Resolver $e^{2x} - 3e^x - 4 = 0$.

Aquí el cambio de variable $u = e^x$ convierte la ecuación en cuadrática:

```
u² − 3u − 4  =  0
(u − 4)(u + 1)  =  0
u = 4   o   u = −1

Pero e^x > 0 siempre, así que u = −1 no es válido.

e^x  =  4
x  =  ln 4  ≈  1.3863
```

---

### 3.3 Método 3: Cambio de variable

Cuando la ecuación es "cuadrática en exponenciales", sustituimos $u = a^x$ o $u = e^x$ para obtener un polinomio.

**Ejemplo:** Resolver $4^x - 5 \cdot 2^x + 4 = 0$.

```
Sea u = 2^x  (entonces 4^x = (2²)^x = u²)

u² − 5u + 4  =  0
(u − 1)(u − 4)  =  0

u = 1   →   2^x = 1  →  x = 0
u = 4   →   2^x = 4  →  x = 2

Soluciones: x = 0  o  x = 2
```

---

### 3.4 Resumen — cuándo usar cada método

| Situación | Método |
|-----------|--------|
| Ambos lados se reescriben con la misma base | **Igualar bases** (el más rápido) |
| Aparece un número "no potencia" (7, 13, etc.) | **Tomar logaritmo** |
| La ecuación es cuadrática en la exponencial | **Cambio de variable** |
| Coeficiente 1 con suma 0 en exponente | Recordar $a^0 = 1$ |

---

## 4. Ecuaciones Logarítmicas

Una **ecuación logarítmica** es aquella en la que la incógnita aparece dentro de un logaritmo. La estrategia general es **convertir a forma exponencial** y resolver.

---

### 4.1 Condiciones de existencia (dominio)

Antes de resolver, **siempre** hay que determinar el dominio:

- Cada logaritmo exige argumento positivo.
- Si la variable aparece como base, la base debe ser positiva y $\neq 1$.

**Ejemplo:** En $\log_2(x - 3)$, el dominio es $x > 3$.

---

### 4.2 Método 1: Convertir a forma exponencial

Si la ecuación tiene **un único logaritmo**, aplicamos directamente la definición.

**Procedimiento:**
1. Determinar el dominio.
2. Reescribir como ecuación exponencial.
3. Resolver y verificar que la solución cumple el dominio.

**Ejemplo 1:** Resolver $\log_2(x+3) = 4$.

```
Dominio: x + 3 > 0  →  x > −3

Convertimos a exponencial:
x + 3  =  2⁴  =  16

x  =  13

Verificación: 13 > −3  ✓
```

**Ejemplo 2:** Resolver $\log_3(2x - 1) = -2$.

```
Dominio: 2x − 1 > 0  →  x > 1/2

Convertimos:
2x − 1  =  3^(−2)  =  1/9

2x  =  1 + 1/9  =  10/9
x   =  5/9

Pero 5/9 < 1/2 ... ¡no cumple el dominio!

Conclusión: no hay solución. (Una ecuación logarítmica puede no tener solución si las restricciones lo impiden.)
```

**Ejemplo 3:** Resolver $\log(x-1) + \log(x+2) = 1$.

```
Dominio: x − 1 > 0 y x + 2 > 0  →  x > 1

Aplicamos propiedad de producto:
log[(x − 1)(x + 2)]  =  1

Convertimos a exponencial (base 10):
(x − 1)(x + 2)  =  10¹  =  10
x² + x − 2  =  10
x² + x − 12  =  0
(x + 4)(x − 3)  =  0

x = −4   o   x = 3

Solo x = 3 cumple x > 1.

Solución: x = 3
```

---

### 4.3 Método 2: Usar propiedades para reducir a un solo logaritmo

Cuando hay varios logaritmos, primero los reducimos a uno solo (con las propiedades de la sección 2), y luego convertimos a forma exponencial.

**Ejemplo 1:** Resolver $\log_2(x) + \log_2(x-2) = 3$.

```
Dominio: x > 0  y  x − 2 > 0  →  x > 2

Reducimos:
log_2[ x(x − 2) ]  =  3

Convertimos:
x(x − 2)  =  2³  =  8
x² − 2x − 8  =  0
(x − 4)(x + 2)  =  0

x = 4   o   x = −2

Solo x = 4 cumple x > 2.

Solución: x = 4
```

**Ejemplo 2:** Resolver $\log_3(x+1) - \log_3(x-1) = 2$.

```
Dominio: x > −1  y  x > 1  →  x > 1

Reducimos:
log_3[ (x+1)/(x−1) ]  =  2

Convertimos:
(x + 1)/(x − 1)  =  3²  =  9

x + 1  =  9(x − 1)
x + 1  =  9x − 9
10  =  8x
x  =  10/8  =  5/4

Verificación: 5/4 > 1  ✓

Solución: x = 5/4
```

**Ejemplo 3:** Resolver $2\log(x) - \log(x-3) = \log 4$.

```
Dominio: x > 0  y  x − 3 > 0  →  x > 3

Reducimos:
log(x²) − log(x − 3)  =  log 4
log[ x²/(x − 3) ]  =  log 4

Como log es inyectiva:
x²/(x − 3)  =  4
x²  =  4(x − 3)
x²  =  4x − 12
x² − 4x + 12  =  0

Discriminante: 16 − 48 = −32 < 0.

No hay soluciones reales.
```

**Ejemplo 4:** Resolver $\log_2(x+5) + \log_2(x-1) = \log_2(3x+5)$.

```
Dominio: x + 5 > 0, x − 1 > 0, 3x + 5 > 0  →  x > 1

Reducimos:
log_2[ (x+5)(x−1) ]  =  log_2(3x+5)

Como log_2 es inyectiva:
(x + 5)(x − 1)  =  3x + 5
x² + 4x − 5  =  3x + 5
x² + x − 10  =  0

x  =  [ −1 ± √(1 + 40) ] / 2
   =  [ −1 ± √41 ] / 2
   ≈  2.7016  o  −3.7016

Solo x ≈ 2.7016 cumple x > 1.

Solución: x = (−1 + √41)/2
```

---

### 4.4 Método 3: Cambio de variable

En algunas ecuaciones el logaritmo aparece de manera que conviene sustituir $u = \log_a x$.

**Ejemplo:** Resolver $(\log x)^2 - 3 \log x + 2 = 0$.

```
Sea u = log x.

u² − 3u + 2  =  0
(u − 1)(u − 2)  =  0
u = 1   o   u = 2

Volvemos a la variable original:
log x = 1   →   x = 10
log x = 2   →   x = 100

Soluciones: x = 10  y  x = 100
```

---

### 4.5 Ecuaciones con cambio de base obligatorio

Cuando aparece una base distinta en cada logaritmo, conviene unificarlas.

**Ejemplo:** Resolver $\log_2 x + \log_4 x = 6$.

```
Convertimos log₄ x a base 2:
log₄ x  =  log₂ x / log₂ 4  =  (1/2) log₂ x

Sustituimos:
log₂ x + (1/2) log₂ x  =  6
(3/2) log₂ x  =  6
log₂ x  =  4
x  =  16
```

---

### 4.6 Verificación de soluciones

Siempre se debe **verificar** cada candidata sustituyéndola en la ecuación original:

- Que cumpla las **condiciones de dominio**.
- Que la igualdad se satisfaga numéricamente (especialmente útil cuando hay logaritmos en bases mixtas).

**Por qué se hace esto:** Al aplicar propiedades como $\log A + \log B = \log(AB)$ o al convertir a exponencial, en principio estamos trabajando con expresiones equivalentes. Sin embargo, hay operaciones intermedias que podrían introducir raíces "falsas" si no se vigila el dominio.

---

## Resumen General de Fórmulas

### Definición

| Concepto | Fórmula |
|----------|---------|
| Logaritmo | $\log_b N = x \iff b^x = N$ |
| Cambio de base | $\log_b N = \dfrac{\log_c N}{\log_c b}$ |

### Propiedades

| Propiedad | Fórmula |
|-----------|---------|
| Producto | $\log_b(M \cdot N) = \log_b M + \log_b N$ |
| Cociente | $\log_b(M / N) = \log_b M - \log_b N$ |
| Potencia | $\log_b(N^r) = r \log_b N$ |
| Raíz | $\log_b\sqrt[r]{N} = \dfrac{1}{r} \log_b N$ |
| Base | $\log_b b = 1$ |
| Unidad | $\log_b 1 = 0$ |
| Inversa | $b^{\log_b N} = N$ |

### Ecuaciones

| Tipo | Estrategia principal |
|------|----------------------|
| Exponencial con bases iguales | Igualar exponentes |
| Exponencial con bases distintas | Tomar logaritmo |
| Exponencial cuadrática | Cambio de variable $u = a^x$ |
| Logarítmica con un solo log | Convertir a exponencial |
| Logarítmica con varios logs | Reducir a un solo log, luego exponencial |
| Logarítmica con $(\log x)^2$ | Cambio de variable $u = \log x$ |

### Dominios obligatorios

| Elemento | Restricción |
|----------|-------------|
| Base $b$ | $b > 0$, $b \neq 1$ |
| Argumento $N$ | $N > 0$ |

---

_Documento elaborado como guía de estudio. Para profundizar, se recomienda resolver una variedad amplia de ejercicios y verificar siempre el dominio antes de dar una solución como válida._
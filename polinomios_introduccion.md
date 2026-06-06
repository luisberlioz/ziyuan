# Introducción a los Polinomios

Una guía elemental sobre los polinomios: qué son, cómo se construyen, qué operaciones se pueden hacer con ellos y cómo se factorizan.

---

## 1. Términos algebraicos

Un **término algebraico** es el producto de un **coeficiente** (un número) y una o más **variables** elevadas a **exponentes** enteros no negativos.

**Partes de un término algebraico:**

- **Coeficiente:** el número que multiplica. Ejemplo: en $-3x^2$, el coeficiente es $-3$.
- **Parte literal (variables y exponentes):** las letras con sus exponentes. Ejemplo: en $5x^2y$, la parte literal es $x^2y$.
- **Exponente:** el número al que está elevada la variable. Ejemplo: en $x^4$, el exponente es $4$.
- **Grado del término:** la suma de los exponentes de todas sus variables. Ejemplo: $4x^2y^3$ tiene grado $2+3=5$.

**Términos semejantes** son aquellos que tienen exactamente la misma parte literal (iguales variables con iguales exponentes). Solo se pueden sumar o restar los términos semejantes. Por ejemplo, $3x^2$ y $-7x^2$ son semejantes, pero $3x^2$ y $3x^3$ no lo son.

---

## 2. Monomio

Un **monomio** es un término algebraico único, es decir, un producto de un coeficiente y variables elevadas a exponentes enteros no negativos.

**Ejemplos:**

- $5x$ (coeficiente $5$, parte literal $x$)
- $-3x^2y$ (coeficiente $-3$, parte literal $x^2y$)
- $\dfrac{2}{3}a^3b^2c$ (coeficiente $\frac{2}{3}$, parte literal $a^3b^2c$)
- $7$ (un número también es un monomio, sin parte literal)

### Grado de un monomio

Es la suma de los exponentes de todas las variables.

**Ejemplos:**

- $4x^3$ tiene grado $3$.
- $-2x^2y^4$ tiene grado $2+4=6$.
- $9$ (constante) tiene grado $0$.

### Coeficiente principal

Es el coeficiente del monomio (el número que multiplica la parte literal).

### ¿Cuándo una expresión es monomio?

Una expresión es monomio **si** cumple:

- Las variables están elevadas a exponentes enteros no negativos ($0, 1, 2, 3, \dots$).
- No hay sumas ni restas dentro de la expresión.
- No hay raíces de variables ni variables en el denominador.

**No son monomios:** $\sqrt{x}$, $\dfrac{1}{x}$, $x^{-2}$.

---

## 3. Polinomio

Un **polinomio** es una suma finita de monomios llamados **términos**. Cada monomio que conforma el polinomio es un término.

**Notación general:**

$$P(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0$$

**Partes de un polinomio:**

- **Términos:** cada uno de los monomios que lo forman. Por ejemplo, en $3x^2 - 5x + 7$ hay tres términos.
- **Coeficientes:** los números que multiplican las potencias de la variable. Por ejemplo, en $-x^3 + 2x^2 - x + 9$ los coeficientes son $-1, 2, -1, 9$.
- **Término independiente:** el término que no contiene variable (donde $x^0 = 1$). Por ejemplo, en $4x^3 - 2x + 11$ el término independiente es $11$.
- **Grado del polinomio:** el mayor exponente al que aparece elevada la variable.
- **Coeficiente principal:** el coeficiente del término de mayor grado.

### Ejemplo: completar la tabla de un polinomio

| Expresión | ¿Es polinomio? | Grado | Coeficiente principal | Término independiente |
|---|---|---|---|---|
| $3x^4 + 2x^2 - 5x^8$ | Sí | $8$ | $-5$ | $0$ |
| $-x^5 + 4x^2 - 7$ | Sí | $5$ | $-1$ | $-7$ |
| $-2x^3 + \sqrt{3}x^2 - 4$ | Sí | $3$ | $-2$ | $-4$ |
| $6x^{10} - 0{,}5x^4 + 3$ | Sí | $10$ | $6$ | $3$ |
| $-x^2 + 2x^{11} - 3x + 1$ | Sí | $11$ | $2$ | $1$ |
| $x^{14} - 2x^7 + 5$ | Sí | $14$ | $1$ | $5$ |
| $5x^3 - x + 8$ | Sí | $3$ | $5$ | $8$ |
| $2x^9 - 3x^5 + x - 10$ | Sí | $9$ | $2$ | $-10$ |
| $\dfrac{1}{3}x^{12} - \sqrt{5}x^6 + 4$ | Sí | $12$ | $\tfrac{1}{3}$ | $4$ |
| $7x^{15} - 2x^4 + 9x - 2$ | Sí | $15$ | $7$ | $-2$ |
| $x^3 - 2x^{1/2} - 3x + 5$ | **No** (exponente $1/2$) | — | — | — |
| $2x^{3/4} - x^2 + 6$ | **No** (exponente $3/4$) | — | — | — |
| $-x - 5 + 3x^4 - \dfrac{7x^2}{3} - 2x^{1/3} + 3$ | **No** (exponente $1/3$) | — | — | — |

> **Regla práctica:** una expresión es polinomio si los exponentes de las variables son **enteros no negativos** ($0, 1, 2, 3, \dots$).

### Nomenclatura según el número de términos

| Nombre | Número de términos | Ejemplo |
|---|---|---|
| Monomio | $1$ | $5x^3$ |
| Binomio | $2$ | $2x^2 - 3x$ |
| Trinomio | $3$ | $x^2 - 5x + 6$ |
| Polinomio | $4$ o más | $x^4 - x^3 + 2x^2 - x + 1$ |

### Nomenclatura según el grado

| Nombre | Grado | Forma general |
|---|---|---|
| Polinomio de grado $0$ (constante) | $0$ | $a_0$ |
| Lineal | $1$ | $a_1 x + a_0$ |
| Cuadrático | $2$ | $a_2 x^2 + a_1 x + a_0$ |
| Cúbico | $3$ | $a_3 x^3 + a_2 x^2 + a_1 x + a_0$ |
| Cuártico | $4$ | $a_4 x^4 + a_3 x^3 + a_2 x^2 + a_1 x + a_0$ |

### Polinomio ordenado y polinomio completo

- **Ordenado:** los términos están escritos de mayor a menor grado (o viceversa). Ejemplo: $2x^3 - x^2 + 5x - 1$ está ordenado en forma decreciente.
- **Completo:** aparecen todos los términos desde el grado mayor hasta el término independiente, sin saltos. Ejemplo: $x^3 + 0x^2 - 4x + 7$ es completo de grado $3$.

### Animación: construyendo un polinomio término a término

La siguiente animación parte de la constante y va agregando, uno por uno, los términos lineal, cuadrático, cúbico y cuártico. En la columna izquierda se acumula la expresión algebraica; en la derecha se dibuja la gráfica de la suma parcial correspondiente.

![Construcción de un polinomio término a término](./polinomios_construccion.mp4)

> **Nota sobre la reproducción en GitHub:** github.com no embebe videos en archivos Markdown (solo en comentarios / PRs). Para ver la animación incrustada en este documento, abre el archivo en el editor web de GitHub y arrastra `polinomios_construccion.mp4` dentro del área de edición — GitHub lo sube a su CDN y reemplaza la línea de arriba con un reproductor de video incrustado.

---

## 4. Operaciones con polinomios

Sean $P(x)$, $Q(x)$, $R(x)$, $S(x)$, $T(x)$ polinomios. Se definen las siguientes operaciones.

### 4.1 Suma de polinomios

$$P(x) + Q(x)$$

**Procedimiento:** se agrupan los términos **semejantes** y se suman sus coeficientes.

**Ejemplo.** Si $P(x) = 4x^2 - 3x + 5$ y $Q(x) = -2x^2 + 7x - 1$:

$$P(x) + Q(x) = (4x^2 - 2x^2) + (-3x + 7x) + (5 - 1) = 2x^2 + 4x + 4$$

**Propiedad:** el grado de la suma es, a lo sumo, el mayor grado de los sumandos (puede bajar si los términos de mayor grado se cancelan).

### Animación: suma de polinomios término a término

La siguiente animación muestra el procedimiento sobre dos polinomios $P(x)$ y $Q(x)$. Para cada grado (empezando por la constante, luego el término lineal, el cuadrático, etc.):

1. se enmarcan los dos términos **semejantes** en las filas de $P(x)$ y $Q(x)$,
2. se bajan a una mesa de trabajo donde se suman sus coeficientes,
3. el término resultante se agrega al lado derecho a la suma acumulada $P(x) + Q(x)$.

El ejemplo incluye un término de grado $4$ en $P(x)$ que no aparece en $Q(x)$, para ilustrar qué hacer cuando un polinomio no tiene un término: su coeficiente es $0$ y el término del otro polinomio se copia sin cambio.

![Suma de polinomios término a término](./polinomios_suma.mp4)

> **Nota sobre la reproducción en GitHub:** ver la nota equivalente en la sección 3 más arriba. Para incrustar el reproductor, arrastra el archivo `.mp4` correspondiente dentro del editor web de GitHub.

### 4.2 Diferencia (resta) de polinomios

$$P(x) - Q(x)$$

**Procedimiento:** se suma el opuesto: a $P(x)$ se le resta cada término de $Q(x)$ (o se le suma el opuesto de $Q(x)$).

**Ejemplo.** Con los mismos polinomios:

$$P(x) - Q(x) = (4x^2 - (-2x^2)) + (-3x - 7x) + (5 - (-1)) = 6x^2 - 10x + 6$$

### 4.3 Producto de polinomios

$$P(x) \cdot Q(x)$$

**Procedimiento:** se multiplica cada término del primer polinomio por cada término del segundo, y luego se agrupan los términos semejantes.

**Ejemplo.** Si $P(x) = 2x + 3$ y $Q(x) = x^2 - 4x + 5$:

$$
P(x)\cdot Q(x) = 2x(x^2 - 4x + 5) + 3(x^2 - 4x + 5)
$$

$$
= 2x^3 - 8x^2 + 10x + 3x^2 - 12x + 15
$$

$$
= 2x^3 - 5x^2 - 2x + 15
$$

### Animación: producto de polinomios término a término

La siguiente animación muestra el procedimiento sobre dos polinomios $P(x)$ y $Q(x)$. Para cada término del primer polinomio (empezando por el de menor grado) y cada término del segundo:

1. se enmarcan los dos términos que se van a multiplicar en las filas de $P(x)$ y $Q(x)$,
2. se muestra el producto parcial $a \cdot b = c$ como anotación al costado,
3. el producto parcial se agrega a la expansión acumulada $P(x) \cdot Q(x)$ que se construye en la parte inferior.

Al final, se agrupan los términos **semejantes** para obtener el polinomio simplificado.

![Multiplicación de polinomios término a término](./polinomios_multiplicacion.mp4)

> **Nota sobre la reproducción en GitHub:** github.com no embebe videos en archivos Markdown (solo en comentarios / PRs). Para ver la animación incrustada en este documento, abre el archivo en el editor web de GitHub y arrastra `polinomios_multiplicacion.mp4` dentro del área de edición — GitHub lo sube a su CDN y reemplaza la línea de arriba con un reproductor de video incrustado.

**Propiedad:** el grado del producto es la **suma** de los grados de los factores.

**Multiplicación de un polinomio por un escalar:**

$$k \cdot P(x)$$

Se multiplica cada coeficiente de $P(x)$ por $k$ (los grados no cambian).

---

## 5. Productos notables

Los **productos notables** son multiplicaciones entre polinomios que siguen un patrón fijo y cuyo resultado puede escribirse directamente, sin hacer todo el desarrollo término a término.

### 5.1 Cuadrado de un binomio

$$(a \pm b)^2 = a^2 \pm 2ab + b^2$$

**Regla mnemotécnica:** *el cuadrado del primero, más/menos el doble del primero por el segundo, más el cuadrado del segundo.*

**Ejemplos:**

- $(x + 3)^2 = x^2 + 6x + 9$
- $(2x - 5)^2 = 4x^2 - 20x + 25$
- $(x^3 - 2y)^2 = x^6 - 4x^3y + 4y^2$
- $(3a^2 - 4b^3)^2 = 9a^4 - 24a^2b^3 + 16b^6$
- $(\sqrt{3}x + 5y)^2 = 3x^2 + 10\sqrt{3}xy + 25y^2$

### 5.2 Cuadrado de un trinomio

$$(a + b + c)^2 = a^2 + b^2 + c^2 + 2ab + 2ac + 2bc$$

Es decir: *la suma de los cuadrados de los tres términos, más el doble de cada producto de dos términos distintos.*

**Ejemplos:**

- $(2x - 3y + 1)^2 = 4x^2 + 9y^2 + 1 - 12xy + 4x - 6y$
- $(2x^2 - 3xy + 4y^2)^2$ se desarrolla con la misma fórmula.

### 5.3 Cubo de un binomio

$$(a \pm b)^3 = a^3 \pm 3a^2b + 3ab^2 \pm b^3$$

**Ejemplo:**

- $(x - 2)^3 = x^3 - 6x^2 + 12x - 8$

### 5.4 Producto de binomios conjugados (diferencia de cuadrados)

$$(a + b)(a - b) = a^2 - b^2$$

**Ejemplos:**

- $(3x - 4y)(3x + 4y) = 9x^2 - 16y^2$
- $(\sqrt{x} - \sqrt{y})(\sqrt{x} + \sqrt{y}) = x - y$

### 5.5 Cubo de un binomio como diferencia o suma de cubos

De $(a+b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$ se deduce:

$$(a+b)(a^2 - ab + b^2) = a^3 + b^3 \quad \text{(suma de cubos)}$$

$$(a-b)(a^2 + ab + b^2) = a^3 - b^3 \quad \text{(diferencia de cubos)}$$

**Ejemplos:**

- $(x + 2)(x^2 - 2x + 4) = x^3 + 8$
- $(x - 1)(x^2 + x + 1) = x^3 - 1$

### 5.6 Producto de binomios con término común

$$(x + a)(x + b) = x^2 + (a+b)x + ab$$

**Ejemplo:** $(x + 3)(x + 5) = x^2 + 8x + 15$.

---

## 6. Factorización de polinomios

**Factorizar** un polinomio es escribirlo como el producto de dos o más factores. Es el proceso inverso a desarrollar un producto notable. Siempre conviene **factorizar completamente**: factorizar hasta que ningún factor admita una factorización adicional.

### 6.1 Factor común (monomio)

Se busca un factor que aparezca en **todos** los términos (un mismo monomio o un mismo número).

**Ejemplo:**

$$3x^2 + 6x - 9x^3 = 3x( x + 2 - 3x^2)$$

Se factoriza el MCD de los coeficientes ($3$) y la variable común de menor exponente ($x$).

### 6.2 Factor común (polinomio)

Si en cada término aparece un mismo **paréntesis**, ese paréntesis es el factor común.

**Ejemplo:**

$$a(b+3) + 5(b+3) = (b+3)(a+5)$$

### 6.3 Factorización por agrupación

Se agrupan los términos en bloques que tengan factor común, y luego se aplica el caso 6.2 entre los bloques.

**Ejemplo:**

$$
x^3 - 3x^2 + 4x - 12 = \underbrace{x^3 - 3x^2}_{\text{grupo 1}} + \underbrace{4x - 12}_{\text{grupo 2}}
$$

$$
= x^2(x - 3) + 4(x - 3) = (x - 3)(x^2 + 4)
$$

### 6.4 Diferencia de cuadrados

$$a^2 - b^2 = (a + b)(a - b)$$

**Ejemplos:**

- $x^2 - 9 = (x + 3)(x - 3)$
- $4a^2 - 25b^2 = (2a - 5b)(2a + 5b)$
- $x^4 - 16 = (x^2 - 4)(x^2 + 4) = (x-2)(x+2)(x^2+4)$
- $x^2 - 64x^4 = x^2(1 - 64x^2)$... aplicando diferencia de cuadrados: $= x^2(1-8x)(1+8x)$

### 6.5 Trinomio cuadrado perfecto

Un trinomio $a^2 \pm 2ab + b^2$ es un cuadrado perfecto porque proviene de $(a \pm b)^2$.

**Procedimiento:** verificar que el primer y tercer término son cuadrados perfectos, y que el segundo término es el doble producto de sus raíces.

**Ejemplos:**

- $x^2 - 6x + 9 = (x - 3)^2$
- $4x^2 - 20x + 25 = (2x - 5)^2$
- $9x^2 - 24xy + 16y^2 = (3x - 4y)^2$

### 6.6 Trinomio de la forma $x^2 + bx + c$

Se buscan dos números $m$ y $n$ tales que:

$$m + n = b \quad \text{y} \quad m \cdot n = c$$

Entonces:

$$x^2 + bx + c = (x + m)(x + n)$$

**Ejemplos:**

- $x^2 - 3x - 18$: buscamos $m+n=-3$ y $mn=-18$. Solución: $m=-6$, $n=3$. Entonces $x^2 - 3x - 18 = (x - 6)(x + 3)$.
- $x^2 - 15x + 56 = (x - 7)(x - 8)$ (porque $-7 + -8 = -15$ y $(-7)(-8) = 56$).
- $x^2 - 11x + 18 = (x - 9)(x - 2)$.

### 6.7 Trinomio de la forma $ax^2 + bx + c$ ($a \neq 1$)

**Método de ensayo y error:** se buscan cuatro números $a_1, a_2, b_1, b_2$ tales que:

$$ax^2 + bx + c = (a_1 x + b_1)(a_2 x + b_2)$$

con $a_1 \cdot a_2 = a$, $b_1 \cdot b_2 = c$ y $a_1 b_2 + a_2 b_1 = b$.

**Ejemplo.** Factorizar $6x^2 + 5x - 6$:

- $a_1 \cdot a_2 = 6$ → opciones: $(1,6), (2,3), (3,2), (6,1)$.
- $b_1 \cdot b_2 = -6$ → opciones: $(1,-6), (2,-3), (3,-2), (-1,6), (-2,3), (-3,2)$.
- Probando $(3x - 2)(2x + 3) = 6x^2 + 9x - 4x - 6 = 6x^2 + 5x - 6$. ✓

### 6.8 Suma y diferencia de cubos

$$a^3 + b^3 = (a + b)(a^2 - ab + b^2)$$

$$a^3 - b^3 = (a - b)(a^2 + ab + b^2)$$

**Ejemplos:**

- $x^3 - 27 = (x - 3)(x^2 + 3x + 9)$
- $8x^3 + 1 = (2x + 1)(4x^2 - 2x + 1)$

### 6.9 Estrategia general para factorizar

1. **Sacar factor común** (caso 6.1) si lo hay.
2. Reconocer si es **diferencia de cuadrados** (6.4) o **suma/diferencia de cubos** (6.8).
3. Si es un **trinomio**, ver si es cuadrado perfecto (6.5) o de la forma $x^2 + bx + c$ (6.6) o $ax^2 + bx + c$ (6.7).
4. Si tiene **cuatro o más términos**, intentar **agrupación** (6.3).
5. Repetir el proceso sobre cada factor hasta que ninguno admita una nueva factorización.

---

## 7. Ejercicios de práctica sugeridos

1. Determinar si cada expresión es polinomio. En caso afirmativo, indicar grado, coeficiente principal y término independiente:
   - $-3x^4 + 5x - 1$
   - $\sqrt{2}x^3 - x + 4$
   - $x^{-2} + x - 1$
   - $7x^5 - 2x^3 + \dfrac{x}{4}$

2. Dados $P(x) = 2x^3 - x^2 + 3x - 4$ y $Q(x) = -x^3 + 5x^2 - x + 2$, calcular:
   - $P(x) + Q(x)$
   - $P(x) - Q(x)$
   - $P(x) \cdot Q(x)$ (solo grado y término independiente del resultado)

3. Aplicar productos notables para desarrollar:
   - $(2x - 7)^2$
   - $(x^2 + 3y)^2$
   - $(x + 1)(x^2 - x + 1)$
   - $(x - 2)(x + 2)(x^2 + 4)$

4. Factorizar completamente:
   - $x^2 - 10x + 25$
   - $4x^2 - 49$
   - $27x^3 - 8$
   - $x^3 + 6x^2 + 11x + 6$
   - $2x^2 + 7x + 3$

---

> **Nota:** este documento es una introducción elemental. Para profundizar, se recomienda practicar primero con la guía de ejercicios de la Unidad II del curso Matemática I (MM-112).

# Unidad III: Ecuaciones

Una guía completa sobre ecuaciones, sus conceptos fundamentales y los métodos para resolverlas: desde la ecuación lineal hasta las ecuaciones polinómicas de grado superior. Cubre el contenido de la **Unidad III** del curso Matemática I (MM-112) impartido en la UNAH.

---

## 1. Conceptos fundamentales

### 1.1 Ecuación

Una **ecuación** es una igualdad entre dos expresiones algebraicas que se cumple únicamente para uno o varios valores específicos de la variable (llamados **incógnitas**).

**Ejemplo:** $3x - 2 = 10$ es una ecuación porque la igualdad entre $3x - 2$ y $10$ solo se cumple cuando $x = 4$.

Toda ecuación tiene dos partes llamadas **miembros**, separadas por el signo "=":

- **Primer miembro:** la expresión a la izquierda del signo igual.
- **Segundo miembro:** la expresión a la derecha del signo igual.

En el ejemplo anterior, el primer miembro es $3x - 2$ y el segundo miembro es $10$.

### 1.2 Raíz o solución

Una **raíz** o **solución** de una ecuación es el valor (o valores) de la variable que hace que la igualdad sea verdadera. Cuando se sustituye la raíz en la ecuación, ambos miembros dan el mismo resultado.

**Ejemplo:** en la ecuación $3x - 2 = 10$, el valor $x = 4$ es una solución, ya que al sustituir:

$$3(4) - 2 = 12 - 2 = 10 \checkmark$$

### 1.3 Conjunto solución

El **conjunto solución** es el conjunto de todos los valores que satisfacen la ecuación. Se denota generalmente como $C.S.$ o simplemente $S$.

**Ejemplo:** para la ecuación $x^2 - 4 = 0$, el conjunto solución es $C.S. = \{-2, 2\}$, ya que tanto $-2$ como $2$ satisfacen la ecuación.

### 1.4 Ecuaciones equivalentes

Dos ecuaciones son **equivalentes** si tienen exactamente el mismo conjunto solución. Es decir, toda solución de la primera es también solución de la segunda, y viceversa.

**Criterios de equivalencia:**

Dos ecuaciones son equivalentes si se cumple alguna de las siguientes operaciones:

1. Se suma o resta el mismo número (o expresión algebraica) a **ambos miembros** de la ecuación.
2. Se multiplican o dividen ambos miembros por el mismo número distinto de cero.

**Ejemplo:** las ecuaciones $3x = 9$ y $x = 3$ son equivalentes (se dividió entre 3). Ambas tienen $C.S. = \{3\}$.

---

## 2. Ecuación lineal

### 2.1 Definición

Una **ecuación lineal** (también llamada **ecuación de primer grado**) es una ecuación donde la variable aparece elevada al exponente 1, es decir, la mayor potencia de la variable es 1. Su forma general es:

$$ax + b = 0 \quad \text{o} \quad ax + b = cx + d$$

donde $a, b, c, d$ son números reales con $a \neq 0$.

**Ejemplos de ecuaciones lineales:**

- $2x - 5 = 7$
- $\dfrac{1}{2}x + \dfrac{3}{4} = 2$
- $3(2x + 1) - 4x = 10$

**No son ecuaciones lineales:** $x^2 = 4$ (exponente 2), $\sqrt{x} = 5$ (raíz).

### 2.2 Resolución

Para resolver una ecuación lineal, el objetivo es **aislar la variable** en uno de los miembros. Esto se logra aplicando las propiedades de equivalencia:

1. **Eliminar denominadores** (si los hay) multiplicando por el mínimo común múltiplo.
2. **Eliminar paréntesis** aplicando la propiedad distributiva.
3. **Agrupar términos con la variable** en un miembro y los términos independientes en el otro.
4. **Operar** hasta obtener la solución.

**Fórmula general:**

Si $ax + b = 0$ con $a \neq 0$, entonces:

$$x = -\frac{b}{a}$$

### 2.3 Tipos de soluciones

- **Solución única:** la mayoría de ecuaciones lineales. Por ejemplo, $2x = 10 \Rightarrow x = 5$.
- **Infinitas soluciones:** cuando la ecuación se reduce a una identidad como $0 = 0$. Por ejemplo, $2(x+1) = 2x + 2$.
- **Sin solución:** cuando la ecuación se reduce a algo imposible como $0 = 5$. Por ejemplo, $2x + 1 = 2x + 3$.

### 2.4 Ejemplos resueltos

**Ejemplo 1** (problema 1.a de la guía):
$$3x - 2x = 5$$
$$x = 5$$
$$C.S. = \{5\}$$

**Ejemplo 2** (problema 1.f de la guía):
$$\frac{1}{2}x + \frac{7}{4}x = 9$$

Multiplicamos por el mcm(2, 4) = 4:
$$2x + 7x = 36$$
$$9x = 36$$
$$x = 4$$
$$C.S. = \{4\}$$

**Ejemplo 3** (problema 1.m de la guía):
$$2(x + 2) - 7 = 5$$
$$2x + 4 - 7 = 5$$
$$2x - 3 = 5$$
$$2x = 8$$
$$x = 4$$
$$C.S. = \{4\}$$

**Ejemplo 4** (problema 1.o de la guía):
$$4(2 - x) + 3(x + 1) = 15$$
$$8 - 4x + 3x + 3 = 15$$
$$11 - x = 15$$
$$-x = 4$$
$$x = -4$$
$$C.S. = \{-4\}$$

---

## 3. Aplicaciones de la ecuación lineal

### 3.1 Método para plantear problemas de aplicación

Para resolver un problema mediante una ecuación lineal:

1. **Leer cuidadosamente** el problema e identificar la cantidad desconocida.
2. **Asignar una variable** a la cantidad desconocida (generalmente $x$).
3. **Expresar todas las cantidades** del problema en términos de la variable.
4. **Plantear la ecuación** traduciendo la relación descrita a lenguaje algebraico.
5. **Resolver** la ecuación.
6. **Verificar** que la solución tenga sentido en el contexto del problema.

### 3.2 Tipos comunes de problemas

#### a) Mezclas y concentraciones
Problemas donde se mezclan dos soluciones de distinta concentración para obtener una concentración final.

**Ejemplo** (problema 2.a de la guía):

> Un enfermero necesita preparar 200 ml de una solución glucosada al 5% usando dos soluciones existentes: una al 2% y otra al 10%. ¿Cuántos mililitros de cada solución debe mezclar?

**Planteamiento:** sea $x$ los ml de la solución al 2%. Entonces los ml de la solución al 10% son $200 - x$.

$$0.02x + 0.10(200 - x) = 0.05 \cdot 200$$
$$0.02x + 20 - 0.10x = 10$$
$$-0.08x = -10$$
$$x = 125$$

El enfermero debe mezclar **125 ml de la solución al 2%** y **75 ml de la solución al 10%**.

#### b) Problemas de números
Problemas donde se pide encontrar números que cumplen ciertas relaciones.

**Ejemplo** (problema 2.e de la guía):

> La suma de dos números es 48. El cuádruplo del menor es igual al doble del mayor. Encontrar los números.

**Planteamiento:** sea $x$ el número menor. Entonces el mayor es $48 - x$.

$$4x = 2(48 - x)$$
$$4x = 96 - 2x$$
$$6x = 96$$
$$x = 16$$

Los números son **16 y 32**.

#### c) Problemas de porcentajes
Problemas donde se aplican descuentos, ganancias o comisiones.

**Ejemplo** (problema 2.h de la guía):

> Una casa se vendió en L. 275,000. ¿Cuánto recibe el propietario si el abogado quien le realizó el trámite tiene una comisión del 8%?

**Planteamiento:** el propietario recibe el 92% del precio de venta.

$$C = 275{,}000 \cdot 0.92 = 253{,}000$$

El propietario recibe **L. 253,000**.

#### d) Problemas de movimiento (velocidad, distancia, tiempo)
Problemas donde se aplica la relación fundamental: $d = v \cdot t$ (distancia = velocidad × tiempo).

**Ejemplo** (problema 2.n de la guía):

> Dos automóviles que están a una distancia de 540 millas entre sí y cuyas velocidades difieren en 7 millas por hora se dirigen el uno hacia el otro. Se encontrarán dentro de cuatro horas. ¿Cuál es la velocidad de cada automóvil?

**Planteamiento:** sea $v$ la velocidad del más lento. La velocidad del más rápido es $v + 7$. Como van uno hacia el otro, las distancias se suman.

$$v \cdot 4 + (v + 7) \cdot 4 = 540$$
$$4v + 4v + 28 = 540$$
$$8v = 512$$
$$v = 64$$

Las velocidades son **64 y 71 millas por hora**.

#### e) Trabajo conjunto
Problemas donde varias personas o máquinas realizan un trabajo juntas.

**Ejemplo** (problema 2.q de la guía):

> María tarda en hacer un trabajo 30 minutos y Pedro tarda 20 minutos en hacer el mismo trabajo. ¿En cuánto tiempo harán el mismo trabajo si lo hacen juntos?

**Planteamiento:** María hace $\frac{1}{30}$ del trabajo por minuto, y Pedro hace $\frac{1}{20}$ por minuto. Sea $t$ el tiempo (en minutos) que tardan juntos.

$$\frac{1}{30}t + \frac{1}{20}t = 1$$

Multiplicamos por el mcm(30, 20) = 60:
$$2t + 3t = 60$$
$$5t = 60$$
$$t = 12$$

Juntos tardan **12 minutos**.

---

## 4. Ecuación cuadrática

### 4.1 Definición

Una **ecuación cuadrática** (o **ecuación de segundo grado**) es una ecuación donde la mayor potencia de la variable es 2. Su forma general es:

$$ax^2 + bx + c = 0$$

donde $a$, $b$ y $c$ son números reales y $a \neq 0$ (si $a = 0$, la ecuación deja de ser cuadrática y se convierte en lineal).

**Términos:**

- $a$ es el **coeficiente cuadrático** (acompaña a $x^2$).
- $b$ es el **coeficiente lineal** (acompaña a $x$).
- $c$ es el **término independiente** (no depende de $x$).

**Ejemplos:**

- $x^2 - 5x + 6 = 0$ → $a = 1$, $b = -5$, $c = 6$.
- $2x^2 + 3x = 0$ → $a = 2$, $b = 3$, $c = 0$.
- $-x^2 + 4 = 0$ → $a = -1$, $b = 0$, $c = 4$.

### 4.2 Número de soluciones

La cantidad de soluciones de una ecuación cuadrática depende de un valor llamado **discriminante**:

$$\Delta = b^2 - 4ac$$

- Si $\Delta > 0$: la ecuación tiene **dos soluciones reales distintas**.
- Si $\Delta = 0$: la ecuación tiene **una solución real** (doble).
- Si $\Delta < 0$: la ecuación **no tiene soluciones reales** (las soluciones son complejas).

### 4.3 Métodos de resolución

#### a) Fórmula general

Para cualquier ecuación $ax^2 + bx + c = 0$ con $a \neq 0$, las soluciones son:

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

Esta fórmula siempre funciona, sin importar el tipo de números involucrados.

**Ejemplo** (problema 3.b de la guía):
$$x^2 + 3x - 10 = 0$$

Aquí $a = 1$, $b = 3$, $c = -10$. Calculamos el discriminante:
$$\Delta = 3^2 - 4(1)(-10) = 9 + 40 = 49$$
$$\sqrt{49} = 7$$

Aplicamos la fórmula:
$$x = \frac{-3 \pm 7}{2}$$

Las dos soluciones son:
$$x_1 = \frac{-3 + 7}{2} = 2 \quad \text{y} \quad x_2 = \frac{-3 - 7}{2} = -5$$

$$C.S. = \{-5, 2\}$$

#### b) Factorización

Consiste en reescribir la ecuación cuadrática como el producto de dos factores lineales igualado a cero:

$$(x - p)(x - q) = 0$$

Por la **propiedad del producto cero**, si un producto es igual a cero, al menos uno de sus factores debe ser cero:

$$x - p = 0 \quad \text{o} \quad x - q = 0$$

Por lo tanto, $x = p$ o $x = q$.

**Para factorizar** una ecuación $x^2 + bx + c = 0$, se buscan dos números $p$ y $q$ tales que:

- $p + q = b$ (la suma es el coeficiente lineal)
- $p \cdot q = c$ (el producto es el término independiente)

**Ejemplo** (problema 3.a de la guía):
$$x^2 - 1 = 0$$

Aplicamos diferencia de cuadrados:
$$(x-1)(x+1) = 0$$

$$x - 1 = 0 \quad \text{o} \quad x + 1 = 0$$

$$x = 1 \quad \text{o} \quad x = -1$$

$$C.S. = \{-1, 1\}$$

**Ejemplo** (problema 3.f de la guía):
$$x^2 + 7x + 10 = 0$$

Buscamos dos números que sumen 7 y cuyo producto sea 10: son 5 y 2.
$$(x + 5)(x + 2) = 0$$

$$x = -5 \quad \text{o} \quad x = -2$$

$$C.S. = \{-5, -2\}$$

#### c) Completar el cuadrado

Es un método alternativo donde se reescribe la ecuación en la forma:

$$(x + h)^2 = k$$

y luego se aplica raíz cuadrada en ambos lados. Aunque es muy útil en contextos teóricos (por ejemplo, para deducir la fórmula general), en la práctica suele ser más rápido usar la fórmula general o la factorización.

### 4.4 Ejemplos resueltos

**Ejemplo 1** (problema 3.c de la guía):
$$x^2 - 3x - 4 = 0$$

Por factorización, buscamos dos números que sumen $-3$ y cuyo producto sea $-4$: son $-4$ y $1$.
$$(x - 4)(x + 1) = 0$$

$$x = 4 \quad \text{o} \quad x = -1$$

$$C.S. = \{-1, 4\}$$

**Ejemplo 2** (problema 3.s de la guía):
$$12x^2 + 17x + 6 = 0$$

Por fórmula general, con $a = 12$, $b = 17$, $c = 6$:
$$\Delta = 17^2 - 4(12)(6) = 289 - 288 = 1$$
$$x = \frac{-17 \pm 1}{24}$$

$$x_1 = \frac{-16}{24} = -\frac{2}{3} \quad \text{y} \quad x_2 = \frac{-18}{24} = -\frac{3}{4}$$

$$C.S. = \left\{-\frac{3}{4}, -\frac{2}{3}\right\}$$

---

## 5. División sintética

### 5.1 Definición

La **división sintética** (también llamada **regla de Ruffini**) es un método abreviado para dividir un polinomio entre un binomio de la forma $x - c$. Aunque solo funciona para este tipo de divisores, es mucho más rápido que la división larga tradicional.

### 5.2 Procedimiento

Para dividir $p(x)$ entre $x - c$:

1. Escribir los coeficientes de $p(x)$ en orden (de mayor a menor grado), incluyendo coeficientes de cero si faltan términos.
2. Escribir el valor de $c$ a la izquierda.
3. Bajar el primer coeficiente tal cual (será el primer coeficiente del cociente).
4. Multiplicar ese coeficiente por $c$ y escribir el resultado debajo del siguiente coeficiente.
5. Sumar la columna. El resultado es el siguiente coeficiente del cociente.
6. Repetir los pasos 4 y 5 hasta el último término.
7. El último número obtenido es el **residuo**; los demás números son los coeficientes del **cociente** (de un grado menor que el dividendo).

**Ejemplo** (problema 4.a de la guía):

Dividir $p(x) = x^3 + 2x^2 - x + 3$ entre $x - 1$.

Los coeficientes de $p(x)$ son: $1, 2, -1, 3$. El valor de $c$ es $1$ (porque $x - 1 = 0 \Rightarrow x = 1$).

```
1 |  1    2   -1    3
  |       1    3    2
  |________________________
     1    3    2    5
```

**Lectura del resultado:**

- **Cociente:** $x^2 + 3x + 2$
- **Residuo:** $5$

Por lo tanto:
$$x^3 + 2x^2 - x + 3 = (x - 1)(x^2 + 3x + 2) + 5$$

### 5.3 Ejemplo resuelto

**Ejemplo** (problema 4.b de la guía):

Dividir $p(x) = 2x^4 - 3x^3 + x^2 - 5x + 4$ entre $x + 2$ (es decir, $c = -2$).

```
-2 |  2   -3    1   -5    4
   |      -4   14  -30   70
   |______________________________
      2   -7   15  -35   74
```

**Lectura del resultado:**

- **Cociente:** $2x^3 - 7x^2 + 15x - 35$
- **Residuo:** $74$

Por lo tanto:
$$2x^4 - 3x^3 + x^2 - 5x + 4 = (x + 2)(2x^3 - 7x^2 + 15x - 35) + 74$$

---

## 6. Teoremas sobre polinomios

### 6.1 Teorema del Residuo

El **Teorema del Residuo** establece que:

> Cuando un polinomio $p(x)$ se divide entre un binomio $x - c$, el residuo de la división es igual al valor que toma el polinomio al evaluar $x = c$, es decir, $p(c)$.

En otras palabras, al hacer división sintética con $c$, el último número que aparece es precisamente $p(c)$.

**Aplicación:** para encontrar el residuo de dividir $p(x)$ entre $x - c$ sin hacer toda la división, simplemente se calcula $p(c)$.

**Ejemplo:**

Para el problema 4.a anterior, $p(x) = x^3 + 2x^2 - x + 3$ y $c = 1$:
$$p(1) = (1)^3 + 2(1)^2 - (1) + 3 = 1 + 2 - 1 + 3 = 5$$

Coincide con el residuo $5$ que obtuvimos. ✓

### 6.2 Teorema del Factor

El **Teorema del Factor** establece que:

> Un binomio $x - c$ es un **factor** de un polinomio $p(x)$ si y solo si $p(c) = 0$, es decir, si y solo si $c$ es una raíz (solución) de $p(x) = 0$.

En otras palabras, $x - c$ divide **exactamente** (sin residuo) a $p(x)$ si y solo si al sustituir $x = c$ en el polinomio el resultado es cero.

**Aplicación:** permite verificar si un número es raíz de un polinomio (y por tanto factor de él) sin hacer la división: simplemente se evalúa el polinomio en ese número.

**Ejemplo:**

Para $p(x) = x^3 - 2x^2 - 5x + 6$, evaluamos en $x = 3$:
$$p(3) = (3)^3 - 2(3)^2 - 5(3) + 6 = 27 - 18 - 15 + 6 = 0$$

Por lo tanto, $x = 3$ es una raíz y $(x - 3)$ es un factor de $p(x)$.

### 6.3 Teorema de las raíces racionales

El **Teorema de las raíces racionales** (o **Teorema de Gauss**) da una herramienta para encontrar las posibles raíces racionales de un polinomio con coeficientes enteros.

> Si un polinomio con coeficientes enteros tiene una raíz racional $\dfrac{p}{q}$ (en su mínima expresión), entonces:
> - $p$ (el numerador) divide al **término independiente** del polinomio.
> - $q$ (el denominador) divide al **coeficiente principal** del polinomio.

**Procedimiento para encontrar raíces racionales:**

1. Listar todos los divisores del término independiente (estos son los candidatos para $p$).
2. Listar todos los divisores del coeficiente principal (estos son los candidatos para $q$).
3. Formar todas las fracciones $\dfrac{p}{q}$ posibles.
4. Probar cada candidato sustituyéndolo en el polinomio (usando el Teorema del Residuo) hasta encontrar una raíz.
5. Una vez encontrada una raíz $c$, dividir el polinomio entre $x - c$ (usando división sintética) para obtener un polinomio de menor grado.
6. Repetir el proceso con el cociente hasta encontrar todas las raíces.

**Ejemplo:**

Para el polinomio $p(x) = x^3 - 3x^2 - 4x + 12$:

- Coeficiente principal: $1$. Sus divisores son $\pm 1$.
- Término independiente: $12$. Sus divisores son $\pm 1, \pm 2, \pm 3, \pm 4, \pm 6, \pm 12$.

Posibles raíces racionales: $\pm 1, \pm 2, \pm 3, \pm 4, \pm 6, \pm 12$.

Probamos:
- $p(2) = 8 - 12 - 8 + 12 = 0$ ✓

Por lo tanto, $x = 2$ es una raíz y $(x - 2)$ es un factor. Dividimos:

```
2 |  1   -3   -4   12
  |       2   -2  -12
  |________________________
     1   -1   -6    0
```

El cociente es $x^2 - x - 6 = (x-3)(x+2)$, cuyas raíces son $x = 3$ y $x = -2$.

Por lo tanto, $p(x) = (x-2)(x-3)(x+2)$ y el conjunto solución de $p(x) = 0$ es $C.S. = \{-2, 2, 3\}$.

---

## 7. Resolución de ecuaciones polinómicas de grado mayor que dos

### 7.1 Definición

Una **ecuación polinómica de grado mayor que dos** es una ecuación de la forma:

$$p(x) = a_nx^n + a_{n-1}x^{n-1} + \cdots + a_1x + a_0 = 0$$

donde $n \geq 3$ y $a_n \neq 0$.

**Ejemplos:**

- Cúbica ($n = 3$): $-2x^3 + 9x^2 - x - 12 = 0$
- Cuártica ($n = 4$): $2x^4 - 2x^3 - 14x^2 + 2x + 12 = 0$
- Quíntica ($n = 5$): $2x^5 - x^4 - 12x^3 + 7x^2 + 16x - 12 = 0$

### 7.2 Estrategia general

Para resolver ecuaciones polinómicas de grado mayor que dos:

1. **Buscar una raíz racional** usando el Teorema de las raíces racionales.
2. **Verificar** la raíz sustituyendo en el polinomio (Teorema del Residuo).
3. **Dividir el polinomio** entre $(x - c)$ usando división sintética.
4. **Resolver el cociente**, que es de un grado menor, repitiendo el proceso o usando la fórmula general si es cuadrático.
5. **Aplicar la propiedad del producto cero**: si $(x - c) \cdot q(x) = 0$, entonces $x = c$ o $q(x) = 0$.

### 7.3 Ejemplo resuelto

**Ejemplo** (problema 5.a de la guía):
$$-2x^3 + 9x^2 - x - 12 = 0$$

**Paso 1:** buscamos raíces racionales.

- Coeficiente principal: $-2$. Divisores: $\pm 1, \pm 2$.
- Término independiente: $-12$. Divisores: $\pm 1, \pm 2, \pm 3, \pm 4, \pm 6, \pm 12$.

Posibles raíces racionales: $\pm 1, \pm 2, \pm 3, \pm 4, \pm 6, \pm 12, \pm \dfrac{1}{2}, \pm \dfrac{3}{2}$.

**Paso 2:** probamos candidatos.

$p(3) = -2(27) + 9(9) - 3 - 12 = -54 + 81 - 3 - 12 = 12$ ✗

$p(4) = -2(64) + 9(16) - 4 - 12 = -128 + 144 - 4 - 12 = 0$ ✓

**Paso 3:** dividimos entre $x - 4$:

```
4 |  -2    9   -1   -12
  |       -8    4    12
  |________________________
     -2    1    3     0
```

El cociente es $-2x^2 + x + 3$.

**Paso 4:** resolvemos $-2x^2 + x + 3 = 0$, o equivalentemente $2x^2 - x - 3 = 0$.

Por factorización: buscamos dos números que sumen $-1$ y cuyo producto sea $-6$: son $-3$ y $2$.
$$(2x - 3)(x + 1) = 0$$

$$x = \frac{3}{2} \quad \text{o} \quad x = -1$$

**Paso 5:** unimos todas las raíces.

$$C.S. = \left\{-1, \frac{3}{2}, 4\right\}$$

### 7.4 Ejemplo con grado 4

**Ejemplo** (problema 5.f de la guía):
$$2x^4 - 2x^3 - 14x^2 + 2x + 12 = 0$$

**Paso 1:** primero, factorizamos el 2 común para simplificar: $2(x^4 - x^3 - 7x^2 + x + 6) = 0$, lo que nos da $x^4 - x^3 - 7x^2 + x + 6 = 0$.

**Paso 2:** buscamos raíces racionales. Coeficiente principal: $1$, término independiente: $6$. Candidatos: $\pm 1, \pm 2, \pm 3, \pm 6$.

$p(1) = 1 - 1 - 7 + 1 + 6 = 0$ ✓

**Paso 3:** dividimos entre $x - 1$:

```
1 |  1   -1   -7    1    6
  |       1    0   -7   -6
  |______________________________
     1    0   -7   -6    0
```

El cociente es $x^3 - 7x - 6$.

**Paso 4:** seguimos buscando raíces racionales de $x^3 - 7x - 6$. Candidatos: $\pm 1, \pm 2, \pm 3, \pm 6$.

$p(-1) = -1 + 7 - 6 = 0$ ✓

**Paso 5:** dividimos $x^3 - 7x - 6$ entre $x + 1$:

```
-1 |  1    0   -7   -6
   |      -1    1    6
   |________________________
      1   -1   -6    0
```

El cociente es $x^2 - x - 6 = (x-3)(x+2)$.

**Paso 6:** unión de todas las raíces.

$$C.S. = \{-2, -1, 1, 3\}$$

---

## 8. Resumen de la unidad

| Tema | Concepto clave | Métodos principales |
|------|----------------|---------------------|
| Conceptos básicos | Ecuación, raíz, conjunto solución, equivalencia | Propiedades de equivalencia |
| Ecuación lineal | $ax + b = 0$, grado 1 | Despeje directo, propiedades de equivalencia |
| Aplicaciones | Mezclas, números, porcentajes, movimiento, trabajo | Plantear y traducir a lenguaje algebraico |
| Ecuación cuadrática | $ax^2 + bx + c = 0$, grado 2 | Fórmula general, factorización |
| División sintética | División entre $x - c$ | Regla de Ruffini |
| Teorema del Residuo | Residuo = $p(c)$ | Evaluación directa |
| Teorema del Factor | $p(c) = 0 \Leftrightarrow (x-c)$ es factor | Verificación de raíces |
| Raíces racionales | Candidatos: $\frac{p}{q}$ con $p\mid c$, $q\mid a$ | Lista de candidatos + evaluación |
| Ecuaciones de grado ≥ 3 | Reducir grado hallando raíces | Factorización sucesiva + fórmula general |

---

## Ejercicios sugeridos de la guía

Para practicar esta unidad, se recomienda resolver los siguientes ejercicios de la guía de la Unidad III:

- **Ecuaciones lineales (básicas):** 1.a, 1.b, 1.c
- **Ecuaciones con fracciones:** 1.f, 1.g, 1.h, 1.j
- **Ecuaciones con paréntesis:** 1.m, 1.n, 1.o, 1.p
- **Aplicaciones:** 2.a, 2.c, 2.e, 2.h, 2.j, 2.n, 2.q, 2.x
- **Ecuaciones cuadráticas (factorización):** 3.a, 3.b, 3.c, 3.f, 3.j
- **Ecuaciones cuadráticas (fórmula general):** 3.k, 3.l, 3.s, 3.t
- **División sintética:** 4.a, 4.b, 4.c
- **Ecuaciones de grado mayor que 2:** 5.a, 5.b, 5.d, 5.f

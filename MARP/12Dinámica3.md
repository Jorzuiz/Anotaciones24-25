# Semana 12: Programación dinámica (III)

## Objetivos:

1. Saber resolver el problema de la multiplicación encadenada de matrices usando programación dinámica. Rellenado de la matriz por diagonales.

2. Saber resolver el problema de justificar un texto usando programación dinámica. Comparar distintas formas de resolver un mismo problema utilizando programación dinámica.

## 12.1 Multiplicación encadenada de matrices

El problema de la multiplicación encadenada de matrices consiste en establecer la forma de colocar los paréntesis en una secuencia de productos entre varias matrices de dimensiones compatibles de forma que se minimice el número de multiplicaciones entre números necesarias para obtener el resultado. Puesto que el producto de matrices es asociativo, el resultado de la multiplicación es el mismo independientemente de cómo se asocian las matrices. Sin embargo, la cantidad de multiplicaciones realizadas entre números al multiplicar dos matrices depende de las dimensiones de dichas matrices  por lo que distintas formas de asociarlas en la secuencia determinarán distintas cantidades de multiplicaciones.

El siguiente vídeo resuelve el problema de la multiplicación encadenada de matrices utilizando programación dinámica. Se trata del primer problema de programación dinámica en el que hay en general más de dos subproblemas con los que buscar la solución óptima, ya que si se desea multiplicar n
 matrices hay n−1
 formas posibles de dividir la secuencia en dos, que corresponden a las distintas formas de elegir la última multiplicación a realizar. También es el primer problema en el que la matriz utilizada para almacenar los resultados de los subproblemas se rellena por diagonales.

[Multiplicación encadenada de matrices URL (15:38)](https://www.youtube.com/watch?v=hKqLP5UzOu8)

En el `problema 52` Carpintero Ebanisto del juez automático has de ayudar al carpintero Ebanisto a decidir en qué orden realizar los cortes sobre un tablón de madera para minimizar el esfuerzo total realizado, teniendo en cuenta que cada vez que corta un trozo de madera en dos el esfuerzo que invierte es el doble de la longitud del trozo.

## 12.2 Justificación de un texto

El objetivo de este problema es repartir las palabras de un texto entre líneas de una determinada longitud sin partirlas. Para conseguir que todas las líneas tengan la misma longitud se introducen espacios adicionales a los que separan las palabras.  Estos espacios extra empeoran la estética del texto, por lo que a cada línea, excepto a la última, se le asocia una penalización por los que contiene, y el objetivo del problema es minimizar la suma de las penalizaciones de las líneas del texto. 
En el siguiente vídeo se explica cómo resolver el problema de justificar un texto utilizando programación dinámica. Se presentan dos soluciones distintas. En la primera se decide qué hacer con cada palabra, mantenerla en la línea si cabe o mandarla a una nueva línea. En la segunda se deciden de golpe todas las palabras a colocar en la siguiente línea y requiere conocer las sumas de longitudes de subsecuencias de palabras del texto.

[Justificación de un texto URL (17:24)](https://www.youtube.com/watch?v=nZRsGjH_SOg)

En el `problema 53`  Cine romántico a raudales del juez automático has de ayudar a Dynamique Cinema a planificar un maratón de cine romántico. Conocida la programación de cada una de las películas que se proyectan, el objetivo es maximizar el tiempo invertido en ver películas. ¿Crees que la estrategia de su hermana Deborah para el cine de terror le sirve?
>Observación: Para que el problema, o su solución, sea más interesante, no intentes sacar partido de que todo ocurre en el mismo día y el número de minutos de un día no es muy grande.

En el entorno de cuestionarios puedes encontrar el cuestionario de autoevaluación del material de esta semana.

### Material adicional

[Diapositivas - Multiplicación encadenada de matrices](./PDFs/31%20Multiplicación%20encadenada%20de%20matrices.pdf)

[Diapositivas - Justificación de un texto](./PDFs/32%20Justificación%20de%20un%20texto.pdf)

## Cuestionario

1. El problema de la multiplicación encadenada de $n$ matrices de forma óptima puede resolverse con una complejidad en tiempo en:
> La respuesta es $O(n^3)$. El algoritmo calcula para cada pareja de indices $i,j$ tales que $i\geq j$ el número mínimo de multiplicaciones básicas para multiplicar las matrices de la $i$ a la $j$ . El cáculo de cada valor es lineal en $n$ porque requiere considerer las distintas formas de colocar los paréntesis externos para realizar la ultima multiplicación. Puesto que la cantidad de parejas a calcular es del $O(n^2)$, el coste está en $O(n^3)$.

2. Al utilizar preogramación dinámica par resolver el problema de los productos encadenados de matrices es imprescindible rellenar la matriz para diagonales.
> Falso. También podría rellenarse de abajo ahcia arriba u de izquierda a derecha, ya que cada posición $(i,j)$ depende de las posucuones $(i,j)$ con $k\leq j -1$ que está en su isma fila a la izquierda, y $(k+1,j)$ con $i\leq k$ que está en la misma columna pero en filas inferiores.

3. En el algoritmo de programación dinámica que resuelve el problema del producto encadenado de matrices, podemos rellenar la matriz:
> Por diagonales comenzando en la diagonal encima de la principal.Puesto que que cada posición $(i,j)$ depende de las posiciones $(i,k)$ y $(k+1,j)$ tales que $(i\leq k \leq j-1)$, las cuales están respectivamente en su misma fila a la izquierda hasta la diagonal principal, y en la misma columna pero en filas inferiores hasta la diagonal principal, una posible forma de rellenar la matriz es por diagonales comenzando en la diagonal encima de la principal. El resto de opciones no garantiza que estén rellenas las posiciones necesarias. Sí podría rellenarse, sin embargo, de abajo arriba y de izquierda a derecha.

4. La solución por programaciçon dinámica al problema de la multiplcicación endadenada de matrices puede implementarse utilizadno el método recursivo descendente:
>Verdadero. La programación dinámica utiliza una tabla para almacenar los valores de subproblemas ya calculados evitando repetir dichos cálculos. El rellenado de esa tabla puede realizarse de manera recursiva descendente y en tal caso solo se almacenarán aquellos valores de subproblemas que sean necesarios para calcular el resultado del problema original.

5. En el algoritmo de programación dinámica que resuelve el problema del producto encadenado de matrices es más eficiente utilizar una matriz auxiliar donde se colocan los paréntesis $(P[i,j]=k)$ significa que se colocan los paréntesis de la siguiente manera: $(M_i\dots M_k)(M_{k+1}\dots M_j)$, aunque no es imprescindible.
> Verdadero. la matriz auxiliar que guarda dónde se colocal¡n los paréntesis permite reconstruir la soluciñon de manera mñas efieciente, con coste $O(n)$ en logar de $O(n^2)$ suendo $n$ el número de matrices.

6. En la solución al problema de la justificación de un texto que utiliza solamente un argumento, el número de casos básicos depende tanto de la longitud de la línea del párrafo como de las longitudes de las palabras.
>Verdadero. Si para cada $i$ calculamos la penalización mínima para formatear las palabras desde la $i$-ésima hasta la última comenzando con una línea en blanco, los casos base corresponden a aquellos $i$ que cumplen que todas las palabras desde la $i$ caben en la línea, es decir aquellas que cumplen:

>$(n-i)+\sum^n_{k=i}l_k\leq L$

>siendo $L$ la longitud de la línea, $\{ l_1,\dots,l_n\}$ las longitudes de las palabras y $(n-i)$ los blancos que deben aparecer entre cada dos palabras. Por tanto, la cantidad de índices $i$ que cumplen esta condición depende de $L$ y de las longitudes de las palabras.

7. En el probelma de la justificación de un texto, si queremos reconstruir la solución (decidir qué palabras van en cada línea) es necesario utilizar un espacuo adicional en $O(nL)$, siendo $n$ el nñumero de palabras del texto y $L$ la longitud de las líneas.
> Falso. Si para cada $i$ calculamos la penalización mínima para formatear las palabras desde la $i$-ésima hasta la última comenzando con una línea en blanco basta con un espacio adicional en $O(n)$ siendo $n$ el número de palabras del texto.

8. En la solución al problema de la justificación de un texto que utiliza solamente un argimento, las posiciones  de la tabla correspondientes a casas básicos son las primeras, las que tienen un índice menor.
> Falso. En la solución con un ñunico argumento calculamos para cada $i$ la penzalización mínima para formatear pabla¡baras desde la $i$-ésima hasta la última comenzando con una línea en blanco, Por tanto los casos base correponden a aquellos $i$ que cumplen que toddas las palabras desde la $i$ hata la última caben en la línea. Si no hay palabras que superen la longitud de una línea, serán casos base de las posiciones de la tabla correspondientes a $n, n-1,\dots$ hsta la menor posición $i$ que cumple que todas las palabras desde la $i$ hasta la última caben en la línea.

9. Para el problema de justificar las palabras de un párrafo a ambos márgenes, existe una estrategia voraz óptima que solamente salta de línea cuando la siguiente palabra no cabe en la línea actual.

> Falso. Un contraejemplo de que la estrategia voraz no conduce a la solución óptima es un caso en el que la longitud de línea es 8 y las palabras son “hola”, “soy”, “yo” y “Antonio”. La estrategia voraz las colocaría así:

hola soy

yo

Antonio

> La primera y última línea no tendrían penalización, por lo que la penalización sería la de la segunda línea, $6^3=216$. Sin embargo con la siguiente distribución:

hola

soy yo

Antonio

> La penalización sería $4^3$ de la primera línea y $2^3$ de la segunda, que da un total de $72$.
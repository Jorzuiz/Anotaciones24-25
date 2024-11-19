# Semana 9: Algoritmos voraces (II)

>Objetivos:
1. Aplicar el método algorítmico de los algoritmos voraces a problemas conocidos: minimizar tiempo medio en el sistema de un conjunto de tarea y maximizar el beneficio de un conjunto de tareas con plazo fijo.
2. Saber utilizar distintos métodos de demostración de las estrategias voraces aplicadas por estos algoritmos.

## 9.1 Minimizar el tiempo medio en el sistema

Disponemos de un conjunto de tareas que han de ser ejecutadas secuencialmente en un único procesador. Se desea minimizar el tiempo medio de estancia de las tareas en el sistema, el cual consta del tiempo que esperan a que les toca ejecutarse más el tiempo que tardan en ejecutarse. Puesto que todas las tareas deben ejecutarse, en este caso la estrategia voraz ha de decidir el orden en que se ejecutan ya que es dicha ordenación la que determina los tiempos que las tareas permanecen en el sistema.

El siguiente vídeo presenta una estrategia voraz que resuelve el problema de minimizar el tiempo medio en el sistema de un conjunto de tareas, y demuestra que la estrategia es óptima:

[Tiempo en el sistema mínimo URL (7:27)](https://www.youtube.com/watch?v=9Up9XQcCGq8)


Supongamos que en lugar de un único procesador disponemos de s
 procesadores idénticos que nos permiten ejecutar las tareas en paralelo. Investiga cuál sería en este caso la estrategia óptima que resuelve el problema. ¿Cuántas tareas le asignarías a cada procesador y cómo?

## 9.2 Tareas con plazo fijo y beneficio

El problema de las tareas con plazo fijo y beneficio puede surgir en contextos muy diferentes y resulta útil identificarlo para poder aplicar el algoritmo voraz eficiente que lo resuelve. Por ejemplo, una empresa de reformas que recibe una gran cantidad de solicitudes y que solo recibirá beneficios en caso de terminar cada obra en su correspondiente plazo, deberá decidir qué obras realizar para maximizar sus beneficios.

En general, se dispone de un conjunto de tareas, todas requiriendo el mismo tiempo de ejecución, pero cada una de ellas con un plazo límite pi
 y un beneficio bi
, que solamente se obtiene si la tarea i
 se realiza antes de su plazo. Partiendo de la situación en que no se pueden realizar todas antes de su plazo, el objetivo es planificar qué tareas seleccionar para maximizar el beneficio obtenido. En este problema no solamente es importante establecer la estrategia voraz sino que el test de factibilidad que determina si la tarea elegida por la estrategia es compatible con las tareas ya seleccionadas requiere de un estudio más minucioso con objeto de que sea eficiente.

El siguiente vídeo presenta una estrategia voraz que resuelve el problema de las tareas con plazo fijo y beneficio, demuestra que la estrategia es óptima y proporciona un test de factibilidad eficiente:

[Tareas con plazo fijo y beneficio URL (20:37)](https://www.youtube.com/watch?v=kepsOdZRp60) 


Con las siguientes tareas con plazo y beneficio dibuja la ejecución paso a paso del algoritmo voraz utilizando cada uno de los dos tests de factibilidad explicados en el vídeo.
|i|$p_i$|$b_i$|
|---|---|---|
|1|3|30|
|2|5|25|
|3|4|20|
|4|1|10|
|5|4|8|
|6|2|5|
|7|2|4|
|8|7|2|

En el problema que hemos visto de las tareas con plazo fijo y beneficio, todas las tareas tardan lo mismo, una unidad de tiempo. Estudia si la estrategia que se ha utilizado para resolver el problema es válida también en el caso de que la ejecución de cada tarea requiera un tiempo arbitrario, posiblemente diferente para cada una.

Aquí tienes otros problemas para practicar la estrategia voraz:


El problema 37  En primera línea de playa del juez automático nos pide averiguar cuál es el menor número de túneles subterráneos que habría que construir para poder conectar todos los hoteles de la costa con la primera línea de playa (ya se verá si la ley de costas lo permite). ¿Tú qué harías? Demuestra formalmente que tu estrategia voraz es óptima.


En el problema 38  El alienígena infiltrado del juez automático  has de ayudar a un alienígena para ocultar su planeta de las observaciones realizadas por un telescopio. Para ello se requiere cubrir un intervalo de tiempo con el menor número de tareas de observación teniendo en cuenta que se permite que se solapen. Demuestra formalmente que la estrategia que propones es óptima.

# Test y resultados

1. El algoritmo voraz que resuelve el problema de la planicifación de tareas de igual duración con plazo fijo maximizando beneficios considera las tareas:

>c. De mayor a menor beneficio. Se puede demostrar por el método de reducción de diferencias que la estrategia que selecciona las tareas de mayor a menor beneficio, comprobando su compatibilidad con las ya seleccionadas, conduce a la solución óptima.

2. ¿Cuál de las siguientes afirmaciones sobre el coste en tiempo de la estrategia voraz para resolver un problema en el que queremos maximizar el beneficio de `n` tareas de igual duración con plazo fijo, es correcta?

> a. $O(1)$ Incorrecta. No podemos asumir que las tareas están ordenadas de menor a mayor, por lo tanto el coste de ordenaras será $O(n log n)$. El resto de operaciones (incluyendo unir y buscar en conjuntos disjuntos) son, a efectos prácticos, constantes, de ahí que no añadan más coste en tiempo.

> b. $O(n)$ Incorrecta por la misma razón que la anterior.

> c. $O(n log n)$ Incorrecta. El mayor coste en tiempo viene de ordenar las tareas de menor a mayor por su beneficio, pero una ordenación eficiente es del orden de $O(n log n)$. El resto de operaciones (incluyendo unir y buscar en conjuntos disjuntos) son, a efectos prácticos, constantes de ahí que no añadan más coste en tiempo.

> d. La respuesta correcta es: $O(n log n)$

3. ¿Cuál de las siguientes afirmaciones sobre el coste en espacio adicional de la estrategia voraz para resolver un problema en el que queremos maximizar el beneficio de $n$ tareas de igual duración con plazo fijo, es correcta?

> $O(n*n)$ Incorrecta. Adicionalmente al vector de datos y solución, necesitamos tanto un vector con tamaño $n+1$ para saber el día más tardío en el que se puede hacer la tarea y conjuntos disjuntos para representar las clases de equivalencia, que hacen que el coste adicional en espacio sea únicamente proporcional a $n$.

> $O(1)$ Incorrecta. Adicionalmente al vector de datos y solución, necesitamos tanto un vector con tamaño $n+1$ para saber el día más tardío en el que se puede hacer la tarea y conjuntos disjuntos para representar las clases de equivalencia, que hacen que el coste adicional en espacio sea proporcional a $n$.

> $O(n)$ Cierto. Adicionalmente al vector de datos y solución, necesitamos tanto un vector con tamaño n+1 para saber el día más tardío en el que se puede hacer la tarea y conjuntos disjuntos para representar las clases de equivalencia, que hacen que el coste adicional en espacio sea proporcional a n.

4. Para demostrar que una estrategia voraz es correcta y obtiene una solución óptima sólo se puede aplicar el método de reducción de diferencias.

> Falso. El método de reducción de diferencias es una forma de demostrarlo. Otra forma de demostrar la optimalidad de la estrategia voraz es ver que cualquier otra solución que no siga la estrategia voraz se puede mejorar.

5. Las tareas indicadas en la tabla siguiente tienen una duración de una unidad de tiempo, se han de completar en el plazo indicado en la segunda columna y reportan el beneficio indicado en la tercera. No se pueden realizar dos tareas simultáneamente y no es necesario planificarlas todas.

|Tarea|plazo|Beneficio|
|---|---|---|
|1|3|12|
|2|2|5|
|3|1|11|
|4|1|11|

> El máximo beneficio posible es 28 (realizando las tareas 3, 2, 1).

6. Queremos planificar un conjunto de tareas para ejecutarlas en un único procesador de forma que se minimice su tiempo medio de estancia en el sistema (espera más ejecución). Si estas tareas son 6 y tienen tiempos de ejecución 24, 17, 10, 14, 28 y 26, ¿en qué orden ejecutarías esas tareas para minimizar el tiempo medio? Escribe los tiempos de las tareas en el orden en el que se ejecutarían.

> La planificación adecuada es la secuencia de tareas ordenada por tiempos de menor a mayor (es decir, 10, 14, 17, 24, 26 y por último 28). El tiempo medio es entonces 175/3.

7. Queremos planificar un conjunto de tareas para ejecutarlas en un único procesador de forma que se minimice su tiempo medio de estancia en el sistema (espera más ejecución). Si estas tareas son 3 y tienen tiempos de ejecución 19, 25 y 17, ¿cuál es el menor tiempo medio que podemos conseguir con una planificación adecuada?

> La solución es 38 (planificando las tareas de menor a mayor tiempo de ejecución). Se ejecuta la tarea 17, luego la 19 (17 + 19 = 36) y finalmente la 25 (36 + 25  = 61). El tiempo total 17 + 36 + 61 = 114, que da un tiempo medio de 38 por tarea.

8. En el taller Fernández se acumulan los coches a arreglar y, lo peor, es que la política de la empresa es que sólo se recibe el pago por la reparación si se entrega el coche antes de una fecha determinada (¡A quién se le ocurriría!). Esa fecha depende del cliente que ha llevado el coche, el beneficio que se obtiene por cada reparación depende del modelo del coche y, finalmente, el tiempo de reparación depende de la avería (no siempre este tiempo es el mismo, por lo tanto).
Para colmo de males, en el taller sólo trabaja su dueño: Alonso Fernández. Asumiendo que Fernández no es capaz de reparar y entregar en plazo todos los coches, ¿puedes ayudarle a decidir si existe una estrategia voraz (y en tal caso cuál) para maximizar su beneficio?

> Ordenamos los coches de mayor a menor según lo que se tarde en reparar y elegimos cada coche que sea compatible con las elecciones anterores Incorrecta. Supongamos 3 coches, los tres deben entregarse en 3 días. El primero reporta un beneficio de 50 y se tarda 3 días; los dos siguientes beneficios de 40 y se tarda 1 día. La solución óptima es reparar los dos últimos
> No existe una estrategia voraz correcta para este problema. Cierto. Existen siempre contraejemplos para cualquier estrategia voraz propuesta
> Ordenamos los coches de menor a mayor según lo que se tarde en reparar y elegimos cada coche que sea compatible con las elecciones anterores. Incorrecta. Supongamos 3 coches, los tres deben entregarse en 3 días. Los dos primeros reportan un beneficio de 10 y tardan 1 día en ser reparados; el tercero reporta un beneficios de 40 y se tarda 3 días. La solución óptima es reparar el último.

9. ¿Cuáles de estas características debe cumplir un algoritmo voraz?

> En cada paso, la elección debe ser la mejor posible. Cierto.

> La solución óptima debe ser única. Falso, el problema de la mochila real si hay varios objetos con el mismo cociente habría diferentes soluciones óptimas.

> En cada paso, la elección del siguiente elemento es única. Falso, por ejemplo, en Kruskal podemos tener varias aristas del mismo peso a elegir.

> En cada paso, cada decisión tomada es inamovible. Cierto.

> Su coste en tiempo no puede ser mayor que lineal. Falso. Por ejemplo, el problema de la mochila real necesita que ordenemos los elementes y esto supone un coste $O(n log n)$

10. Hemos intentado resolver un problema, P, con un algoritmo que aplica estrategia voraz, pero al intentar demostrar aplicando en método de diferencias que esa estrategia es correcta, llegamos a probar que la solución voraz puede ser peor que una solución óptima. ¿Qué podemos afirmar al respecto?

> Hemos elegido mal la solución óptima. `Falso`. La solución óptima no la hemos “elegido”, sólo hemos asumido que existe una solución óptima.
> No sabemos si el problema P se puede resolver con una estrategia voraz o no. `Cierto`. No podemos afirmar que se pueda (no hemos encontrado una estrategia voraz), pero tampoco sabemos si no se puede (puede existir una estrategia voraz correcta para resolverlo).
> El problema P no se puede resolver con una estrategia voraz. `Falso`. Puede ser que exista otra estrategia voraz que sí que funcione.
> Nuestra estrategia voraz es incorrecta. `Cierto`. Nuestra estrategia no produce una solución óptima.
> La estrategia voraz no se puede demostrar con el método de diferencias, habría que usar otra técnica de demostración. `Falso`. Si al tratar de aplicar el método de diferencias vemos que la solución voraz puede ser peor que otra solución válida, entonces es que la solución voraz no es óptima por definición y no se puede probar lo contrario.
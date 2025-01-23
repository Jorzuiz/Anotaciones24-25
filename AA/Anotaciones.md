# Anotaciones Aprendizaje Automático

> Objetivo: Poder volver a esto en un par de meses y no tener que volver a pelearme con toda la asignatura desde 0.
> Objetivo secundario: Ayudar a gente que quiera empezar a entender de tratamiento de datos y entrenamiento de IA abisquito

## Resumen Global

La IA se usa con el objetivo de poder tratar datos y predecir o "finjir" un uso inteligente de estos. Existen modelos de `Predicción` como los `MultiLayer Perceptron` o `Redes Neuronales` de diferentes configuraciones y modelos de `Clasificación` como los `K-Neares Neighbors` o `Random Forest`.
Ambos se entrenan con un gran volumen de datos que se tratan de una manera especifica en base al algoritmo, el primero permite predecir una variable, el tipo de giro que hace una IA de un coche o el valor del pan en base al estado del mercado y el segundo clasifica en base a un sistema, el tipo de enfermedad que desarrolle alguien según su historial o canciones recomendadas según tus gustos.

En el curso se explica e implementa un Multilayer Perceptron, una red neuronal con una serie de `neuronas` (Valores matemáticos) de entrada, una capa oculta con más neuronas y una capa de salida con neuronas también.
Estas neuronas realizan operaciones matemáticas que transforman, por ejemplo, los 400 pixeles de entrada de una imagen 20x20 en los 10 posibles valores que puede tener entre los numeros del 0-9.

## Tratamiento y limpieza de datos

Los datos suelen leerse de archivos .csv pero tambien pueden usarse imagenes. Los CSV estan estructurados en columnas con tipos de variables y filas con cada caso. En la ssignatura se han mostrado datos de pacientes y enfermedades de hospital y trazas de un juego de carreras.

> Datos de pacientes

|Age|Sex|ChestPainType|RestingBP|Cholesterol|FastingBS|RestingECG|MaxHR|ExerciseAngina|Oldpeak|ST_Slope|HeartDisease|
|---|---|-------------|---------|-----------|---------|----------|-----|--------------|-------|--------|------------|
|40 |M  |ATA          |140      |289        |0        |Normal    |172  |N             |0      |Up      |0           |
|49 |F  |NAP          |160      |180        |0        |Normal    |156  |N             |1      |Flat    |1           |
|37 |M  |ATA          |130      |283        |0        |ST        |98   |N             |0      |Up      |0           |
|48 |F  |ASY          |138      |214        |0        |Normal    |108  |Y             |1.5    |Flat    |1           |

> Trazas de un juego de carreras

|ray1|ray2|ray3|ray4|ray5|kartx|karty |kartz|time|action|
|----|----|----|----|----|-----|------|-----|----|------|
|-1.0|5.541817|5.515208|4.611081|4.58892|15.98893|0.2756145|3.10501|0.3733333|NONE  |
|-1.0|5.541757|5.515268|4.611082|4.588919|15.98893|0.2756903|3.10501|0.4123687|NONE  |
|19.29325|5.550231|5.506805|4.616851|4.583151|15.98312|0.2791599|32.94455|5.704584|ACCELERATE|
|17.83484|5.540693|5.515919|4.617383|4.582619|15.9826|0.2791599|34.38129|5.80104|ACCELERATE|
|16.33047|5.475322|5.613923|4.617956|4.582047|15.98202|0.27916|35.8917|5.90244|ACCELERATE|

Los datos que usamos para una red pueden no estar "limpios", vease, tener valores incorrectos o irrelevantes.
En el caso del juego de carreras, podemos observar que la posicion Y, la vertical, no cambia en toda la pista, asique es irrelevante para la IA que vamos a entrenar.
Ver esto no siempre es tan fácil, por eso a la hora de limpiar estos datso es MUY importante hacer una representación gráfica para poder analizarlos a ojo y ver que nos sirve o si hay valores anómalos.

Para cargar y limpiar estos datos usaremos la librería `Pandas`.

```python
import pandas as pd

df = pd.read_csv('data/heart.csv')
```

AL leer con el metodo `read_csv` se crea un `DataFrame`, es una tabla que tiene nombres en las columnas. Cada columna se denomina `Serie`, una lista de valores con un nombre, `Accion: IZQ,IZQ,DR,IZQ`.
Para poder usar estos datos tendremos que transofrmarlos de algún modo a un array.
Python de manera natural tiene un tipo de datos estructurado denominad `Lista`, pero que por algún motivo la gente puede llamar array pese a no serlo. Este tipo puede tener datos de diferentes tipos dentro, int, float, string y lo que sea al mismo tiempo.
>esto no nos sirve

Usaremos la libreria `numpy` para trabajar con sus arrays denominados `ndarray`.
Me niego a llamar array a algo que no sea esto y si lo ves en internet deberás asumir que es este tipo de array. Solo contendrán datos de un tipo.

```python 
import numpy as np 
```

Primero "limpiaremos" los datos y luego los "prepararemos".

Las filas pueden tener valores incorrectos cono NaN. La manera más sencilla de deshacerte de ellos es "tirarlos".

```python
df = df.dropna()
```
Esto elimina cualquier fila que tenga al menos un valor NaN.
Ahora bien, en este caso pasamos de 918 casos a 915, ¿Que ocurre si esto nos hubiese tirado la mitad de los datos?
>ESTAMOS JODIDOS
Es broma, podemos usar otro método para sustituir estos valores por sus valores medios en cada columna, esto nos asegura que si un paciente no tiene presión arterial porque no se le ha tomado, en vez de eliminar todos esos datos se le asigne una presión media respecto a todos los pacientes.
Lo ideal sería tener más casos para compensar pero el mundo no es perfecto y la data science esta aún menos.

Enter the `Imputer`

jeje

Sklearn nos proporciona una clase SimpleImputer que sustituye valores Nan con estrategias sencillas, esto es, media para números y más frecuente para categorías.

Podemos observar como se han importado los datos con el comando

```python
print(df.dtypes)
```

|Name          |type   |
|--------------|-------|
|Age           |int64  |
|Sex           |object |
|ChestPainType |object |
|RestingBP     |int64  |
|Cholesterol   |int64  |
|FastingBS     |int64  |
|RestingECG    |object |
|MaxHR         |float64|
|ExerciseAngina|object |
|Oldpeak       |float64|
|ST_Slope      |object |
|HeartDisease  |int64  |


Nuestro objetivo es que todos los datos sean tipo float y estén en una matriz que conmponga "casos" con columnas que se correspondan a los valores de estos datos.
Esta matriz no es más que un array de dimensiones NxM.

Los valores numéricos son fáciles de pasar a float.
Primero los separamos a mano en un dataframe y luego forzamos el cambio de tipo para asegurarnos que no haya ints doubles o queseyo.

```python
df_numeric = df.select_dtypes(include=np.number)
df_numeric = df_numeric.astype(np.float64)
```

|Name          |type   |
|--------------|-------|
|Age           |float64|
|RestingBP     |float64|
|Cholesterol   |float64|
|FastingBS     |float64|
|MaxHR         |float64|
|Oldpeak       |float64|
|HeartDisease  |float64|

|Age      |RestingBP|Cholesterol|FastingBS|MaxHR|Oldpeak|HeartDisease|
|---------|---------|-----------|---------|-----|-------|------------|
|40.0     |140.0    |289.0      |0.0      |172.0|0.0    |0.0         |
|49.0     |160.0    |180.0      |0.0      |156.0|1.0    |1.0         |
|37.0     |130.0    |283.0      |0.0      |98.0 |0.0    |0.0         |
|48.0     |138.0    |214.0      |0.0      |108.0|1.5    |1.0         |
|54.0     |150.0    |195.0      |0.0      |122.0|0.0    |0.0         |



Como habrás notado es dificil sacar operaciones matemáticas para valores como `hombre` o `Capitalista` asique tendremos que hacer algo con ellas.
Now presenting `One-Hot encoding`.
Se trata de un proceso por el cual primero se "averigua" de manera automática cuantos valores puede tener una de estas variables (Hombre, mujer, Non-binary) y luego se transforma en una máscara ([1,0,0] [0,1,0] [0,0,1]).
Esto es un término de programación, si no sabes lo que es a estas alturas, puedes buscarlo por tu cuenta o creer en mi palabra y seguir leyendo.

Podemos usar el método de Pandas o el de Sklearn. Importante mencionar que Sklearn nos permitirá deshacer esta codificación de manera sencilla si lo necesitamos luego, pero eso ya como veamos cada uno.

```python
df_categoric = df.select_dtypes(exclude=np.number)
df_categoric = pd.get_dummies(df, dtype=float)
```

|Sex_F         |Sex_M  |ChestPainType_ASY|ChestPainType_ATA|ChestPainType_NAP|ChestPainType_TA|RestingECG_LVH|RestingECG_Normal|RestingECG_ST|ExerciseAngina_N|ExerciseAngina_Y|ST_Slope_Down|ST_Slope_Flat|ST_Slope_Up|
|--------------|-------|-----------------|-----------------|-----------------|----------------|--------------|-----------------|-------------|----------------|----------------|-------------|-------------|-----------|
|0.0           |1.0    |0.0              |1.0              |0.0              |0.0             |0.0           |1.0              |0.0          |1.0             |0.0             |0.0          |0.0          |1.0        |
|1.0           |0.0    |0.0              |0.0              |1.0              |0.0             |0.0           |1.0              |0.0          |1.0             |0.0             |0.0          |1.0          |0.0        |
|0.0           |1.0    |0.0              |1.0              |0.0              |0.0             |0.0           |0.0              |1.0          |1.0             |0.0             |0.0          |0.0          |1.0        |
|1.0           |0.0    |1.0              |0.0              |0.0              |0.0             |0.0           |1.0              |0.0          |0.0             |1.0             |0.0          |1.0          |0.0        |
|0.0           |1.0    |0.0              |0.0              |1.0              |0.0             |0.0           |1.0              |0.0          |1.0             |0.0             |0.0          |0.0          |1.0        |


Esto hace que la columna Sex con valores M y F pase a llamarse como columnas Sex_M y Sex_F con valores 1.0 y 0.0.
Mencionar que lo hemos transformado a float directamente porque será el tipo de variable que usemos para todos los calculos de la red. En concreto `float64` que es el valor por defecto de python para float.

Ahora solo quedan dos cosas, juntar los datos para el entremaiento y separar los datos de salida.
Tradicionalmente se llaman `X` e `Y`.

Podemos juntar los datos con un concat. Al haber pasado por estos procesos existirán columnas de más con nombres nuevos y en un orden diferente al original. El orden no es relevante, las redes usan sistemas que seguran linealidad entre todos los datos y además siempre tenemos que entrenarlas de diferentes maneras para ir mejorando la tasa de aciertos asique tocará experimentar.
> Datos originales correspondientes a filas con valores NaN

|row|Age|Sex|ChestPainType|RestingBP|Cholesterol|FastingBS|RestingECG|MaxHR|ExerciseAngina|Oldpeak|ST_Slope|HeartDisease|
|---|---|---|-------------|---------|-----------|---------|----------|-----|--------------|-------|--------|------------|
|136|43 |F  |ATA          |120      |215        |0        |NaN       |175.0|N             |0.0    |Up      |0           |
|168|58 |M  |ASY          |135      |222        |0        |Normal    |NaN  |N             |0.0    |Up      |0           |
|186|58 |NaN|ATA          |130      |251        |0        |Normal    |110.0|N             |0.0    |Up      |0           |


```python
df_imputed = pd.concat([df_imputed_numeric, df_imputed_categoric], axis=1)
display(df_imputed.loc[[136]],df_imputed.loc[[168]],df_imputed.loc[[186]])
```

> Valores posteriores una vez Imputados y vueltos a unirse

|row|Age|RestingBP|Cholesterol|FastingBS|MaxHR|Oldpeak|HeartDisease|Sex_F|Sex_M|ChestPainType_ASY|...|ChestPainType_NAP|ChestPainType_TA|RestingECG_LVH   |RestingECG_Normal|RestingECG_ST   |ExerciseAngina_N|ExerciseAngina_Y|ST_Slope_Down|ST_Slope_Flat|ST_Slope_Up|
|---|---|---------|-----------|---------|-----|-------|------------|-----|-----|-----------------|---|-----------------|----------------|-----------------|-----------------|----------------|----------------|----------------|-------------|-------------|-----------|
|136|43.0|120.0    |215.0      |0.0      |175.0|0.0    |0.0         |1.0  |0.0  |0.0              |...|0.0              |0.0             |0.0              |0.0              |0.0             |1.0             |0.0             |0.0          |0.0          |1.0        |
|168|58.0|135.0    |222.0      |0.0      |136.849509|0.0    |0.0         |0.0  |1.0  |1.0              |...|0.0              |0.0             |0.0              |1.0              |0.0             |1.0             |0.0             |0.0          |0.0          |1.0        |
|186|58.0|130.0    |251.0      |0.0      |110.0|0.0    |0.0         |0.0  |0.0  |0.0              |...|0.0              |0.0             |0.0              |1.0              |0.0             |1.0             |0.0             |0.0          |0.0          |1.0        |

Ahora solo seleccionamos lo que queremos para la entrada como X y salida como Y

```python
y = df_imputed['HeartDisease'].values
X = df_imputed.drop('HeartDisease', axis = 1).values
```

las dimensiones finales serán de (918,20) y (918,)
El comando values ha sacado la columna Y y la ha transformado en un vector en vez de una matriz debido a que no hemos transformado el DataFrame sino una Series, tendremos que convertirlo para evitar problemas.

Listo :3

## Preparación y entrenamiento del modelo
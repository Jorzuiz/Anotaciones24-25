# Resumen

Esto es lo que he entendido de la práctica y le he explicado al patito de goma de la ducha.

- He cambiado los sensores para que formen una W desde la posicion del Kart porque me ha parecido buena idea detectar las colisiones un poco antes de que ocurran.

1. Tenemos que generar unos datos jugando a un juego para entrenar una IA.
2. Los datos contienen informacion de unos sensores para medir distancias, posicion del coche, el tiempo en que se tomaron y el boton que ha pulsado el jugador.
3. La IA tendrá que aprender que boton pulsar en base a los datos que hemos generado.
4. Antes de usar cualquier modelo tendremos que limpiar esos datos, ej.: no tiene sentido la posición vertical del kart si la pista es plana. También habrá que juntar los datos en mismo archivo y aplicar standard scaler y demas cosas.
5. Hacemos esto porque puede haber datos irrelevantes, errores y cosas que la IA se comería y le sentaría mal al resultado que queremos. Los normalizamos porque queremos que todos los datos sean igual de importantes y noa fecten cosas como medir distancias en kilómetros y posiciones en milimetros.
6. Entrenaremos la IA en python y nos generará una matriz que se corresponde con los pesos entrenados. El archivo 3 exmat que estabamos usando hasta ahora.
7. Hareos esto con nuestro MLP, el KNN y demas cosas que piden.
8. Tocamos los hiperparametros hasta que los test de prediccion lleguen al 70, creo que ponia.
9. Esto significa que una parte de los datos se separa para comprobar luego (suelen ser 70-90% para entrenamiento) y cuando la red esté entrenada metemos esos datos y comprobamos que las etiquetas sean als correctas. Rollo si en los datos tenemos un obstaculo a la derecho y hemos pulsado izquierda, la red tendrá que leer en la capa de entrada los sensores, posicion, tiempo y tal y decir que tambien ha pulsado izquierda depues de aplicar a estos datos las matemagias que haya aprendido.
10. En nuestro caso son 10 partidas con unas 8500 lineas de CSV. Asi a lo grosso usaremos 7500 de esas etiquetas de manera aleatoria para generar el entrenamiento por refuerzo con el algoritmo de turno y cuando acabemos meteremos en lo generado las 1000 lineas restantes y comprobaremos que devuelva las etiquetas que tienen con un acierto de ese 70% de minimo.
11. Las utilidades que nos ha dado el profe nos permiten grabar una partida y aplicar la red entrenada si la hemos acabado.
12. Para poder aplicar la red entrenada tenemos que implementar en c# del script de unity el algoritmod e feedforward, este algoritmo es el que coge una linea de nuestro csv, aplica matemagia y devuelve una etiqueta de prediccion.
13. basicamente tendremos que entrenar las IAs en python y el parseador de JSON que nos dan se las dará en un formato que entienda a Unity para que el juego las use con el feedforward en vez de nuetros controles de teclado.
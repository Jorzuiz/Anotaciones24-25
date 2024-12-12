Zero:
Van aponerse quisquillosos con la cantidad de pixeles de CADA cuadro de ahi.
Aunque sean incrementales, suspender una no te ayuda en la segunda, en la segunda se entiende que las cosas de la primera esten arregladas.
Arquitectura compartida de aplicacion multiplataforma.
Compilacion diferente en multiplataforma.
Diferentes opciones de compilacion por plataforma (Diferentes "cmake" o lo que sea) Esto lo configuramos en el Visual Studio con las opciones de plataforma.
Para poder construir el ejecutable final necesitamos la logica y una libreria estática que se encuentra en lugares diferentes en las opciones del priyecto. Será un archivo de librería Engine con terminaciones diferentes (Engine = MotorPC.lib / Engine = MotorPS5.a)
O eliminamos el motor de win32 o lo ponemos en la solucion??
Los ejecutables tienen nombre distintos para plataforma y configuracion, BIN no puede tener subdirectorios



```c++
class Irenderer{
    virtual clear() =0;
}
class rendererPC : IRenderer{

}

class rendererPS5 : IRenderer{

}

int main(){

    IRenderer* renderer;
// NO se puede usr esto porque si la LOGICA gestiona el renderizado con ifdef ya no es multiplataforma
#ifdef __POSPERO__
    renderer = new RendererPS5();
#else
    renderer = new RendererPC();
}

renderer->clear(...);
renderer->drawRect(...);
renderer->present(...);
```

La palabra `virtual`. Cualquier cosa con virtual tiene sobrecarga.

Cuidado con incializacion y cierre
Nada de leaks
DETECTAR ERRORES y salir ordenadamente+
Como se hace un singleton??

Para evitar errores siempre  hay que devolver algo,
En PS5 por defecto las excepciones estan deshabilitadas. No se suelen usar. Colocar un new en un try catch de un constructor es algo RARO.

REGLA: Los constructores NO pueden fallar.
Forzar la inicializacion en 2 pasos
Un SIngleton que para crear la instancia necesite parametos (Enel renderer PC puedes pedirle una ventana de 1280x720 pasandolo coo parametro)

```c++
static bool Init(int w, int h){
    _instance =  new Renderer();
    return _instance.init(w,h); // Si esto falla destruyola instancia y devuelvo falso
}
static Renderer * Instance(){
    return _instance;
    }

static Renderer Instance = nullr;

if(Platform::Init(...){})
cout<<uyuyuyuyu/n;
return 1;

if(Renderer::Init(1280x720){}){
cout<<uyuyuyuyu/n;
Platform::release();
return 1;}
```

David Brey:
Practica 2:
Cuadros deben reaparecer por el otro lado de la pantalla si lo atraviesa (Ej: Si un cuadrado azul, pasa el lado derecho, reaparece en el lado izquierdo).

Practica donde hay que pintar 3 ventanas, cada una con 4 cuadrados. En las ventanas laterales, caen de manera diagonal y el la del centro cae en vertical. El juego no tiene input
En las practicas siguientes, el movimiento de los cuadrados sera diferente (Evitar cablear)
Arquitectura pensada para funcionar en multiplataforma (Windows, Linux, PS5)
Como compilar Ogre en Linux? --> Con CMake, para elegir que apartados se quiere compilar
No se va a usar CMake
Probablemente habra que hacer una arquitectura parecida a Moviles

DLLs con varios nombres para que convivan en el mismo directorio
Cuando se haga entrega y en el examen... no entregar ????
Nada de leaks y controlar los warnings y fallos
Constructor devuelve null para evitar errores. Constructores no pueden fallar
Usar inicializacion en 2 pasos y asi comprobar que no funcione
	Vease: Constructora no asigna nada y luego [static bool] Init() asigna todo lo que haga falta. Devuelve false si hay algo que de error

Uso singleton
Las excepciones es mejor evitarlas

Ejemplo Pedro Pablo:


```c++
// Muchos import

//-------------- renderer PS5 ----------
#include "RendererPS5.h"
using Renderer = RendererPS5;

#include "renderer.h"

static bool Init(int w, int h)
{
	_instance = new Renderer();
	return _instance.init(w,h); // Si esto falla, devuelve fallo y se destruye
	
}

static Renderer* Instance()
{return _instance;}

class IRenderer
{
	virtual clear() = 0
	
}

class RendererPC : IRenderer {
	...
}

class RendererPS5 : IRenderer {
	...
}

int main(){
if(Renderer::Init(1280,720))
{
	// Cos
}

// No se puede usar en la logica
// Queremos usar el polimorfismo, usando clases abstractas donde creamos las clases especializadas para cada plataforma
// Que es el virtual del clear del IRenderer? (Pregunta clasica de entrevista)[Sobrecarga]
#ifdef __Prospero__
    RendererPS5* rendererps5 =  new RendererPS5(...);
#else
    RendererPC* renderer = new RendererPC();

renderer->clear()
renderer->drawRect(...)
renderer->show()
}
```
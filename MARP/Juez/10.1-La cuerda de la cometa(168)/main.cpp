
/*@ <authors>
 *
 * Jorge Zurdo MARP46
 *
 *@ </authors> */

#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

//#include "../TADs/EnterosInf.h"

#ifndef ENTEROSINF_H_
#define ENTEROSINF_H_

#include <limits>
#include <iostream>

class EntInf {
    int num;
public:
    static const int _intInf = 1000000000;

    EntInf(int n = 0) : num(n) {}

    EntInf operator+(EntInf const& b) const {
        if (num == _intInf || b.num == _intInf || num >= (_intInf - b.num))
            return _intInf;
        else return num + b.num;
    }

    bool operator==(EntInf const& b) const {
        return num == b.num;
    }

    bool operator!=(EntInf const& b) const {
        return !(*this == b);
    }

    bool operator<(EntInf const& b) const {
        if (num == _intInf) return false;
        else if (b.num == _intInf) return true;
        else return num < b.num;
    }

    bool operator>(EntInf const& b) const {
        return b < *this;
    }

    void print(std::ostream& out = std::cout) const {
        if (num == _intInf) out << "+Inf";
        else out << num;
    }
};

const EntInf Infinito(EntInf::_intInf);

inline std::ostream& operator<<(std::ostream& out, EntInf const& e) {
    e.print(out);
    return out;
}

#endif

/*@ <answer>

N<int> cordeles de 1 a 1000, L Vector<int> longitudes de 1 a 1000 y C vector<int> coste de 1 a 1000
Longitud objetivo exacta LON a crear con las diferentes cuerdas
Calcular minimo numero de cordeles y su coste, y numero de combinaciones diferentes posibles
Contar cantidad de combinaciones posibles para cada LON

Programación dinámica (recursividad y casos base)
Usaremos ascendente para construir la solución de  los casos base hasta el resultado
Evitaremos descendente poque requeriria de construir tablas de hasta 1000 casos y la tabla podria consumir demasiada memoria

El coste final es del orden de O(N*L) donde N es el numero de cuerdas y L la longitud
El coste en espacio es de tres vectores de tamaño L+1 para las formas y minimos
Cabe mencionar que estos vectores se reducen el espacio pero se sigue operando multiples veces sobre ellos machacando datos antiguos

 @ </answer> */


 // ================================================================
 // Escribe el código completo de tu solución aquí debajo
 // ================================================================
 //@ <answer>

// Stucts por claridad de código
struct Resultado {
    EntInf maneras;
    EntInf minCuerdas;
    EntInf minCoste;
};

struct Cuerda {
    int Longitud;
    int Coste;
};

Resultado cuerdaCometa(int N, int L, const vector<Cuerda>& cuerdas) {

    // Podemos reducir el espacio de tablas a vectores haciendo recorridos inversos
    vector<EntInf> maneras(L + 1, 0);
    vector<EntInf> minCuerdas(L + 1, Infinito);
    vector<EntInf> minCoste(L + 1, Infinito);

    maneras[0] = 1;     // Se inicia a {1, 0, ...}
    minCuerdas[0] = 0;  // Se inicia a {0, Inf, ...}
    minCoste[0] = 0;    // Se inicia a {0, Inf, ...}

    // Recorreremos primero las cuerdas y luego las longitudes porque no vamos a repetir las cuerdas ams de una vez, asique vamos a generar
    // una tabla con espacio de soluciones N*L
    for (int i = 1; i <= N; ++i) {      // Recorrido de cuerdas
        // Tendremos que usar un recorrido en orden inverso porque al usar un vector en vez de tabla 
        // tenemos que asegurarnos de no machacar los valores a la izquierda que vayamos a necesitar
        for (int j = L; j >= 0; --j) {  // Recorrido de longitud en orden inverso

            // Decidimos si usar o no la cuerda actual para la longitud; esto iterará sobre cada posible cuerda en cada longitud
            // Ej: si la longitud actual es 4  y queremos llegar a la de destino 5 con las cuerdas {1,3,5}, en esta iteracion solo comprobaremos {1, 3}
            if (cuerdas[i - 1].Longitud <= j) {

                // maneras[i - 1][j - cuerdas[i - 1].Longitud] maneras de alcanzar la longitud RESTANTE con las cuerdas anteriores
                // Esto puede ser un valor superior en la tabla por mas de un valor j y es lo que hace que no se pueda reducir en espacio
                maneras[j] = (maneras[j] + maneras[j - cuerdas[i - 1].Longitud]);

                // Tenemos que comprobar  si un valor es posible de alcanzarse antes de actualizarlo
                // Esto puede dejar huecos en la tabla formas y vectores de valores si por ejemplo tenemos longitud 3 pero la cuerda minima es 4
                if (minCuerdas[j - cuerdas[i - 1].Longitud] != Infinito) {
                    minCuerdas[j] = min(minCuerdas[j], minCuerdas[j - cuerdas[i - 1].Longitud] + 1);    // Actualizacion de numero de cuerdas si procede
                }
                if (minCoste[j - cuerdas[i - 1].Longitud] != Infinito) {
                    minCoste[j] = min(minCoste[j], minCoste[j - cuerdas[i - 1].Longitud] + cuerdas[i - 1].Coste);   // Actualizacion de coste si procede
                }
            }
        }
    }

    if (maneras[L]>0)
        return { maneras[L], minCoste[L], minCuerdas[L] };

    // Si en la última posición no hay un resultado válido devolvemos un valor que lo indique
    return { 0, Infinito, Infinito};
}


bool resuelveCaso() {

    // leer los datos de la entrada
    int N, L;
    vector<Cuerda> cuerdas; // Int longitud, int coste
    
    cin >> N >> L;

    int lon, cost;

    for (int i = 0; i < N; i++)
    {
        cin >> lon >> cost;
        cuerdas.push_back({lon, cost});
    }
    
    if (!std::cin)  // fin de la entrada
        return false;

    // Resolver el caso posiblemente llamando a otras funciones
    Resultado resultado = cuerdaCometa(N, L, cuerdas);
    
    // Escribir la solución
    if (resultado.maneras != 0)
        cout << "SI " << resultado.maneras << " " << resultado.minCoste << " " << resultado.minCuerdas << "\n";
    else
        cout << "NO\n";

    return true;
}

//@ </answer>
//  Lo que se escriba dejado de esta línea ya no forma parte de la solución.

int main() {
    // ajustes para que cin extraiga directamente de un fichero
#ifndef DOMJUDGE
    std::ifstream in("casos.txt");
    auto cinbuf = std::cin.rdbuf(in.rdbuf());
#endif

    while (resuelveCaso());

    // para dejar todo como estaba al principio
#ifndef DOMJUDGE
    std::cin.rdbuf(cinbuf);
#endif
    return 0;
}

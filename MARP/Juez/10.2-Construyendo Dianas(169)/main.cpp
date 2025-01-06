
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

//
//  EnterosInf.h
//
//  Implementación de enteros con +infinito.
//
//  Facultad de Informática
//  Universidad Complutense de Madrid
//
//  Copyright (c) 2020  Alberto Verdejo
//

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

P = valor en puntos de 1 a 500, S = numero de sectores de la diana de 1 a 50
valor = numero de puntos de 1 a 500

Semejante a problema de monedas
Programación dinámica ascendente CON REPETICION
Generaremos espaciod e soluciones en una tabla buscando la menor cantidad de dardos necesarios para llegar a P
Al seguir un orden estricto de puntuaciones ascendente, las ultimas en sumarse a la tabla seran las mayores
Esto nos permite usar un vector en vez de la tabla porque no tenemos que reconstruir soluciones intermedias
Quedamos por lo tanto con el algoritmo de cambio de monedas con espacio reducido de coste O(P * S) y espacio de soluciones de P+1

 @ </answer> */


 // ================================================================
 // Escribe el código completo de tu solución aquí debajo
 // ================================================================
 //@ <answer>

vector<int> puntosDiana(int P, int S, vector<int> const& diana) {

    int n = diana.size();
    vector<EntInf> combinaciones(P + 1, Infinito);
    combinaciones[0] = 0;

    // Calcular la matriz sobre el propio vector
    // Como los valores de la "tabla" solo dependen de su valor a la izquierda y arriba
    // podemos hacer que j vaya avanzando en vase al valor de su celda y de su izquierda ahorrando espacio
    for (int i = 1; i <= n; ++i) {
        for (int j = diana[i - 1]; j <= P; ++j) {
            combinaciones[j] = min(combinaciones[j], combinaciones[j - diana[i - 1]] + 1);
        }
    }
    
    // Reconstruir solucion
    vector<int> sol;
    if (combinaciones[P] != Infinito) {
        int i = S, j = P;
        while (j > 0) { // Quedan puntos hasta llegar
            if (diana[i - 1] <= j && combinaciones[j] == combinaciones[j - diana[i - 1]] + 1) {
                // Cargamos de mayor a menor las puntuaciones en el vector
                sol.push_back(diana[i - 1]);
                j = j - diana[i - 1];
            }
            else // Avanzamos hacia una puntuacion menor
                --i;
        }
    }
    return sol;
}

bool resuelveCaso() {

    // leer los datos de la entrada
    int P, S;
    vector<int> diana;

    cin >> P >> S;

    // Lee y carga valores de los sectores de la diana
    int valor;
    for (int i = 0; i < S; i++)
    {
        cin >> valor;
        diana.push_back(valor);
    }

    if (!std::cin)  // fin de la entrada
        return false;

    // Resolver el caso posiblemente llamando a otras funciones
    vector<int> resultado = puntosDiana(P, S, diana);

    // Escribir la solución
    if (resultado.size() != 0) {
        cout << resultado.size()<< ": ";
        for (int i = 0; i < resultado.size(); i++)
        {
            cout << resultado[i] << " ";
        }
        cout << "\n";
    }
    else
        cout << "Imposible\n";

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

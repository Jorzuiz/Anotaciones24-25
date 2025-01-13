
/*@ <authors>
 *
 * Jorge Zurdo Izquierdo MARP46
 *
 *@ </authors> */

#include <iostream>
#include <fstream>
using namespace std;

#include "Matriz.h"  // propios o los de las estructuras de datos de clase

/*@ <answer>

Partimos del algoritmo de los patitos para palindromos pero en este caso la tabla contendrá la palabra inversa
lo que buscamos es la palabra palindroma generada y queremos "espejar" las letras que no coinciden
    RecONOR -> RONOceR
partiendo de esta cadena tendremos que construir el resultado añadiendo letras que no esten en ambos lados

 @ </answer> */


 // ================================================================
 // Escribe el código completo de tu solución aquí debajo
 // ================================================================
 //@ <answer>

// Calcula la longitud del mayor palíndromo en patitos[i..j]
int aibofobia(string const& letras, int i, int j, Matriz<int>& patin) {
    int& res = patin[i][j];

    if (res == -1) {
        if (i > j) res = 0;
        else if (i == j) res = 1;
        else if (letras[i] == letras[j])
            res = aibofobia(letras, i + 1, j - 1, patin) + 2;
        else
            res = max(aibofobia(letras, i + 1, j, patin),
                aibofobia(letras, i, j - 1, patin));
    }
    return res;
}

// Hay que modificar esto para que reconstruya de mas supongo
// añade al final de sol el palíndromo más largo en patitos[i..j]
void reconstruir(string const& patitos, Matriz<int> const& patin,
    int i, int j, string& sol) {
    if (i > j) return;
    if (i == j) sol.push_back(patitos[i]);
    else if (patitos[i] == patitos[j]) {
        sol.push_back(patitos[i]);
        reconstruir(patitos, patin, i + 1, j - 1, sol);
        sol.push_back(patitos[j]);
    }
    else if (patin[i][j] == patin[i + 1][j])
        reconstruir(patitos, patin, i + 1, j, sol);
    else
        reconstruir(patitos, patin, i, j - 1, sol);
}



bool resuelveCaso() {

    // leer los datos de la entrada

    if (!std::cin)  // fin de la entrada
        return false;

    // resolver el caso posiblemente llamando a otras funciones

    // escribir la solución

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

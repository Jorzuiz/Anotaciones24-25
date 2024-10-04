
/*@ <authors>
 *
 * MARP 46 Jorge Zurdo Izquierdo
 * MARP 35 Muxu Rubia Luque
 * 
 *@ </authors> */

#include <iostream>
#include <fstream>
#include "../Treeset_AVL.h"
using namespace std;

/*@ <answer>

 Escribe aquí un comentario general sobre la solución, explicando cómo
 se resuelve el problema y cuál es el coste de la solución, en función
 del tamaño del problema.

 @ </answer> */


 // ================================================================
 // Escribe el código completo de tu solución aquí debajo
 // ================================================================
 //@ <answer>

bool resuelveCaso() {

    int N;
    cin >> N;
    if (N == 0)
        return false;

    // Cargamos el arbol con los valores
    // La insercion del nuevo nodo busca menores y mayores para cargarlo en su posicion O(log N)
    // Llamadas sucesivas a inserta hacen reequilibrios cuando se inserta el árbol para mantener la altura con rotaciones
    Set<int> arbol;
    int val;
    for (int i = 0; i < N; ++i)
    {
        cin >> val;
        arbol.insert(val);
    }

    int M;
    cin >> M;

    // para cada consulta se utiliza el nuevo método kesimo
    for (int i = 0; i < M; ++i) {
        int k;
        cin >> k;

        try
        {
            cout << arbol.kesimo(k) << "\n";
        }
        catch (std::out_of_range& e)
        {
            cout << "??\n";
        }

    }

    cout << "---\n";

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

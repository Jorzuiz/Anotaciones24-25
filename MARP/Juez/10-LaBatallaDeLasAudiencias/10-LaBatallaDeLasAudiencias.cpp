
/*@ <authors>
 *
 * Muxu Rubia Luque -   MARP 35
 * Jorge Zurdo Izquierdo - MARP 46
 *
 *@ </authors> */

#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

#include "..\IndexPQ.h"

/*@ <answer>

 Canales ordenadoos de 0-10^6
 Vector de pares con indices, ordenar con un sort.
 vector <canal, minuto> personas
 cola prioridades variables, cada canal espectadores
 @ </answer> */


 // ================================================================
 // Escribe el código completo de tu solución aquí debajo
 // ================================================================
 //@ <answer>

bool operator>(pair<int, int> a, pair<int, int> b) {
    return a.second > b.second || !(a.second == b.second);
}

bool resuelveCaso() {

    // leer los datos de la entrada
    int rango, canales, actualizaciones;
    std::cin >> rango >> canales >> actualizaciones;

    IndexPQ<int, gv  b  reater<int>> cola(canales);
    vector<pair<int, int>> resultados;

    // Lectura inicial de audiencia de cada canal
    int buff, canal, audiencia;
    for (int j = 0; j < canales; j++) {
            cin >> audiencia;
            cola.push(j, audiencia);
            resultados[j] = { j, 0 };
    }

    int anterior = 0, minuto;
    //Aqui se hace update de los canales que ya existen
    for (int i = 0; i < actualizaciones; ++i) {
        
        cin >> minuto;      
        // Actualizacion de los minutos en el máximo
        resultados[cola.top().elem].second += (minuto - anterior);
        anterior = minuto;  // actualiza

        int canal, audiencia;
        cin >> canal;
        while (canal != -1) {
            cin >> audiencia;
            cola.update(canal, audiencia);
            cin >> canal;
        }
    }

    resultados[cola.top().elem].second += (rango - anterior);

    // Ordena los canales por minutos de mayor a menor
    std::sort(resultados.begin(), resultados.end(), [](auto& left, auto& right) {
        return left.second < right.second;
    });

    int i = 0;
    // Imprime los canales lideres de audiencia por cantidad de tiempo
    while (resultados[i].second != 0)
        std::cout << resultados[i].first << resultados[i].second << "\n";

    std::cout << "---";

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

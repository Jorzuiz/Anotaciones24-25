
 /*@ <answer>
  *
    MARP46 Jorge Zurdo Izquierdo
  *
  *@ </answer> */

#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>

using namespace std;

#include "bintree.h"

/*@ <answer>

Generamos un nuevo método que calcula la altura de cada nodo de manera recursiva
No es necesario almacenarla porque no estamos creando una clase nueva

 @ </answer> */

 // ================================================================
 // Escribe el código completo de tu solución aquí debajo (después de la marca)
 //@ <answer>

// Medidor de altura
// No tenemos que almacenarlo en la clase BinTree, pero tendremos que contar la altura para saber si es AVL
// Cada llamada recursiva se suma a la altura hacia arriba y se queda con el hijo mayor
// Coste de O(N) puesto que pasa por todos los nodos del arbol
template <typename T>
int altura(const BinTree<T>& a) {
    if (a.empty())
        return 0;
    else return 1 + max(altura(a.left()), altura(a.right()));
}

// Método que comprueba las alturas de los hijos de un arbol para saber si es AVl
// Sus hijos tambien deben ser AVL
template <typename T>
bool esAVL(const BinTree<T>& arbol) {

    if (arbol.empty())   return true;

    int alturaIz = altura(arbol.left());
    int alturaDer = altura(arbol.right());
    int comparador = abs(alturaIz - alturaDer);
    
    // Para que sea AVL ademas hay que comprobar que si existen los valores respeten orden
    bool AVL = true;
    if (!arbol.left().empty())
        AVL = (arbol.left().root() < arbol.root());
    if (!arbol.right().empty())
        AVL = (arbol.right().root() > arbol.root() && AVL);

    // Importante el valor absoluto, te ahorra quebraderos de cabeza
    // Para que sea AVL tiene que ser AVL y sus hijos tambien
    return (comparador <= 1) && AVL && esAVL(arbol.left()) && esAVL(arbol.right());
}


bool resuelveCaso() {

    char tipo;  // Tipo N para enteros, tipo P para palabras
    cin >> tipo;

    if (tipo == 'N') {        // tipo INT

        BinTree<int> arbol = read_tree<int>(cin);

        if (esAVL(arbol))   cout << ("SI\n");
        else                cout << ("NO\n");
    }
    else if (tipo == 'P') {   // tipo STRING

        BinTree<string> arbol = read_tree<string>(cin);

        if (esAVL(arbol))   cout << ("SI\n");
        else                cout << ("NO\n");
    }

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

#ifndef DOMJUDGE
    std::cin.rdbuf(cinbuf);
#endif
    return 0;
}

# Algoritmos

> Cheat Sheet de algoritmos recopilada en un archivo para toda la asignatura de MARP

## S11 - Programación DInámica 2

### Caminos mínimos

```c++
void Floyd(Matriz<EntInf> const& G, Matriz<EntInf> & C, Matriz<int> & A) {
    int V = G.numfils(); // número de vértices de G
    // inicialización
    C = G;
    A = Matriz<int>(V, V, -1);
    for (int i = 0; i < V; ++i) {
        for (int j = 0; j < V; ++j) {
            if (i != j && G[i][j] != Infinito)
                A[i][j] = i;
        }
    }

    // actualizaciones de las matrices
    for (int k = 0; k < V; ++k) {
        for (int i = 0; i < V; ++i) {
            for (int j = 0; j < V; ++j) {
                auto temp = C[i][k] + C[k][j];
                if (temp < C[i][j]) { // es mejor pasar por k
                    C[i][j] = temp;
                    A[i][j] = A[k][j];
                }
            }
        }
    }
}
```

```c++
Implementación
using Camino = std::deque<int>;
Camino ir_de(int i, int j, Matriz<int> const& A) {
    Camino cam;
    while (j != i) {
        cam.push_front(j);
        j = A[i][j];
    }
    
    cam.push_front(i);
    return cam;
}

```

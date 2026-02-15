// 2OLIDTS-WilliamSelvas-05IA.cpp : Programa de ejemplo para manejar un vector de nombres de aves.
// Contiene funciones para mostrar, agregar y eliminar aves usando std::vector.

#include <iostream>
#include <vector>
#include <string>

using namespace std;

// Muestra las aves que están en el vector
void arreglo_aves(const vector<string>& aves)
{
    if (aves.empty()) {
        cout << "No hay aves en el vector." << '\n';
        return;
    }

    cout << "Los valores del vector:" << '\n';
    for (size_t i = 0; i < aves.size(); ++i) {
        cout << aves[i] << " ";
    }
    cout << "\n";
}

// Agrega tres aves al final del vector usando push_back (modifica el vector por referencia)
void push_arreglo_aves(vector<string>& aves)
{
    aves.push_back("Mayna");
    aves.push_back("Periquitos");
    aves.push_back("Cacatua");

    cout << "Los valores del vector despues de insertar: \n";
    for (size_t i = 0; i < aves.size(); ++i) {
        cout << aves[i] << " ";
    }
    cout << "\n";
}

// Elimina la última ave del vector usando pop_back (modifica el vector por referencia)
void pop_arreglo_aves(vector<string>& aves)
{
    if (aves.empty()) {
        cout << "No hay aves para eliminar." << '\n';
        return;
    }
    aves.pop_back();
    cout << "Los valores del vector despues del pop:\n";
    for (size_t i = 0; i < aves.size(); ++i) {
        cout << aves[i] << " ";
    }
    cout << "\n";
}

int main()
{
    vector<string> aves = { "Loro gris", "Paloma de diamante", "Coctel" };

    arreglo_aves(aves);
    push_arreglo_aves(aves);
    pop_arreglo_aves(aves);

    return 0;
}

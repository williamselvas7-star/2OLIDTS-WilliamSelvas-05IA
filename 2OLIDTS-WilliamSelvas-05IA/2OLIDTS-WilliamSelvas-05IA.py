# aves.py - Programa que maneja una lista de nombres de aves.

def mostrar_aves(aves):
    if not aves:
        print("No hay aves en la lista.")
        return
    print("Los valores de la lista:")
    print(" ".join(aves))
    print()

def push_arreglo_aves(aves):
    # Agrega tres aves al final (equivalente a push_back)
    aves.append("Mayna")
    aves.append("Periquitos")
    aves.append("Cacatua")
    print("Los valores de la lista despues de insertar:")
    print(" ".join(aves))
    print()

def pop_arreglo_aves(aves):
    # Elimina la última ave (equivalente a pop_back)
    if not aves:
        print("No hay aves para eliminar.")
        return
    eliminado = aves.pop()
    print(f"Eliminando la última ave: {eliminado}")
    print("Los valores de la lista despues del pop:")
    print(" ".join(aves))
    print()


def main():
    aves = ["Loro gris", "Paloma de diamante", "Coctel"]

    mostrar_aves(aves)
    push_arreglo_aves(aves)
    pop_arreglo_aves(aves)


if __name__ == '__main__':
    main()

"""aves.py - Gestión sencilla y segura de una lista de nombres de aves.

Funciones con anotaciones de tipos y comportamiento claro (devuelven
valores en lugar de sólo imprimir) para facilitar pruebas y reutilización.
"""
from typing import List, Optional


def mostrar_aves(aves: List[str]) -> None:
    """Muestra las aves con índice y un contador.

    Args:
        aves: lista de nombres de aves.
    """
    if not aves:
        print("No hay aves en la lista.")
        return
    print(f"Aves ({len(aves)}):")
    for i, nombre in enumerate(aves, start=1):
        print(f"{i}. {nombre}")
    print()


def agregar_aves(aves: List[str], *nuevas: str) -> int:
    """Agrega una o varias aves al final de la lista.

    Args:
        aves: lista a modificar.
        *nuevas: nombres de aves a agregar.

    Returns:
        Número de aves agregadas.
    """
    aves.extend(nuevas)
    return len(nuevas)


def eliminar_ultima_ave(aves: List[str]) -> Optional[str]:
    """Elimina y devuelve la última ave. Devuelve None si la lista está vacía."""
    if not aves:
        return None
    return aves.pop()


def main() -> None:
    aves: List[str] = ["Loro gris", "Paloma de diamante", "Coctel"]

    mostrar_aves(aves)

    añadidas = agregar_aves(aves, "Mayna", "Periquitos", "Cacatua")
    print(f"Se agregaron {añadidas} aves.")
    mostrar_aves(aves)

    eliminado = eliminar_ultima_ave(aves)
    if eliminado is not None:
        print(f"Ave eliminada: {eliminado}\n")
    else:
        print("No se eliminó ninguna ave (lista vacía).\n")
    mostrar_aves(aves)


if __name__ == "__main__":
    main()

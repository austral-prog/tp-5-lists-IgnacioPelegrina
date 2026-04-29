# Ejercicio 4: Remover elementos en posiciones específicas

def remove_elements(lista):
    """
    Remueve el primer, quinto y sexto elemento de la lista.
    La función debe funcionar con listas de cualquier tamaño.

    Args:
        lista: Una lista de elementos

    Returns:
        La lista después de remover los elementos indicados
    """
    if lista == []:
        return []
    else:
        del lista[0]
        lista[3:5] = []
    return lista
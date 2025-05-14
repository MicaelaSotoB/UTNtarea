"""
Este módulo va a contener validaciones y retornos de listas, como el mayor elemento de una lista o el menor.

"""

def crear_arreglo(longitud: int, valor) -> list:
    lista = [valor] * longitud
    return lista


def mayor_lista_pos(lista: list) -> int:
    """
    Esta función recorre la lista y buscar el mayor valor, retorna la posición en lista de este mismo valor
    Retorna también si hay más de uno con el mismo valor
    """
    mayor = float('-inf')
    pos = 0
    for i in range(len(lista)):
        if mayor < lista[i]:
            mayor = lista[i]
            pos = i
    return pos


def mayores_lista_pos(lista: list) -> int:
    """
    Está función recorre una lista y puede devolver una lista con cada posición que contenga un valor igual al valor máximo 
    de la lista inicial
    """
    mayor = float('-inf')
    lista_mayores = crear_arreglo(None, len(lista))
    for i in range(len(lista)):
        if mayor < lista[i]:
            mayor = lista[i]

    contador = 0
    for i in range(len(lista)):
        if lista[i] == mayor:
            lista_mayores[contador] = i
            contador += 1

    return lista_mayores

def menor_lista_pos(lista: list) -> int:
    """
    Esta función recorre la lista y buscar el menor valor, retorna la posición en lista de este mismo valor
    """
    menor = float('+inf')
    pos = 0

    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            pos = i
    return pos


def menores_lista_pos(lista: list) -> int:
    """
    Esta función recorre la lista y buscar el menor valor, retorna una lista con las posiciones de la lista inicial
    que sean iguales al menor valor
    """
    menor = float('+inf')
    lista_menores = [None]*len(lista)

    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]

    contador = 0
    for i in range(len(lista)):
        if lista[i] == menor:
            lista_menores[contador] = i
            contador += 1
    return lista_menores

def promedio_lista(lista: list) -> float:
    """
    Esta función calcula retorna el promedio entre los elementos de la lista
    """
    sumatoria = 0
    for i in range(len(lista)):
        sumatoria += lista[i]
    promedio = sumatoria / len(lista)
    return promedio

def contiene_valor(lista: list, valor: any) -> bool:
    """
    Está función recibe una lista y un valor, busca el valor en la lista y retorna si se encuentra o no
    """
    contiene = False
    i = 0
    while i < len(lista) and not contiene:
        if lista[i] == valor:
            contiene = True
        i += 1
    return contiene

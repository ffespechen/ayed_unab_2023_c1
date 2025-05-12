class NodoLista:
    def __init__(self, info=None, siguiente=None):
        self.info = info
        self.siguiente = siguiente


class Lista:
    def __init__(self):
        self.inicio = None
        self.tamanio = 0


## Función para insertar elementos a la lista en forma ordenada
def insertar(lista, dato):
    nodo = NodoLista(dato)
    if (lista.inicio is None) or (lista.inicio.info > dato):
        nodo.siguiente = lista.inicio
        lista.inicio = nodo
    else:
        anterior = lista.inicio
        actual = lista.inicio.siguiente
        while (actual is not None) and (actual.info < dato):
            anterior = anterior.siguiente
            actual = actual.siguiente
        anterior.siguiente = nodo
        nodo.siguiente = actual
    lista.tamanio = lista.tamanio + 1

def eliminar(lista, valor):
    dato = None
    if (lista.inicio.info == valor):
        dato = lista.inicio.info
        lista.inicio = lista.inicio.siguiente
        lista.tamanio -= 1
    else: # Recorrer la lista
        anterior = lista.inicio
        actual = lista.inicio.siguiente
        while (actual is not None) and (actual.info != valor):
            anterior = anterior.siguiente
            actual = actual.siguiente
        if (actual is not None):
            dato = actual.info
            anterior.siguiente = actual.siguiente
            lista.tamanio -= 1
    return dato

def buscar(lista, valor):
    dato = None
    if (lista.inicio.info == valor):
        dato = lista.inicio.info
    else: # Recorrer la lista
        anterior = lista.inicio
        actual = lista.inicio.siguiente
        while (actual is not None) and (actual.info != valor):
            anterior = anterior.siguiente
            actual = actual.siguiente
        if (actual is not None):
            dato = actual.info
    return dato

def is_empty(lista) -> bool:
    return (lista.tamanio == 0)

def imprimir(lista):
    cantidad = 0
    actual = lista.inicio 
    while (cantidad < lista.tamanio):
        print(actual.info)
        actual = actual.siguiente
        cantidad += 1


lista1 = Lista()
insertar(lista1, 8)
insertar(lista1, 4)
insertar(lista1, 2)
insertar(lista1, 7)
insertar(lista1, 3)
insertar(lista1, 5)
imprimir(lista1)
print("-----------------------")

eliminar(lista1, 2)
eliminar(lista1, 7)
imprimir(lista1)

print(buscar(lista1, 5))
print(buscar(lista1, 11))


## Ejemplo

# nodo0 = NodoLista(0)
# nodo1 = NodoLista(1)
# nodo2 = NodoLista(2)

# nodo0.siguiente = nodo1
# nodo1.siguiente = nodo2

# print(F"El valor del nodo inicial es: {nodo0.info}")
# print(F"El valor del nodo siguiente es: {nodo0.siguiente.info}")
# print(F"El nodo del último tiene el valor: {nodo0.siguiente.siguiente.info}")

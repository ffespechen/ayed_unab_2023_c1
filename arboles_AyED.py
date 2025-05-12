class NodoArbol:
    def __init__(self, dato):
        '''Clase Nodo para implementación de árboles en Python'''
        self.informacion = dato
        self.izquierda = None
        self.derecha = None


def arbol_vacio(raiz) -> bool:
    return (raiz is None)

def insertar_nodo(raiz, dato):
    '''
    Función que inserta nodos en el árbol
    Si son menores al valor del nodo comparado, a la IZQUIERDA
    Si son mayores al valor del nodo comparado, a la DERECHA
    '''
    if arbol_vacio(raiz):
        raiz = NodoArbol(dato)
    elif (raiz.informacion <= dato):
        raiz.derecha = insertar_nodo(raiz.derecha, dato)
    else:
        raiz.izquierda = insertar_nodo(raiz.izquierda, dato)
    return raiz

def imprimir_arbol(raiz):
    if arbol_vacio(raiz):
        print(" - ")
    else:
        print(F"[ {raiz.informacion} ]")
        print(F"Rama IZQUIERDA del nodo {raiz.informacion}")
        imprimir_arbol(raiz.izquierda)
        print(F"Rama DERECHA del nodo {raiz.informacion}")
        imprimir_arbol(raiz.derecha)


arbol = insertar_nodo(None, 'M')
arbol = insertar_nodo(arbol, 'B')
arbol = insertar_nodo(arbol, 'J')
arbol = insertar_nodo(arbol, 'A')
imprimir_arbol(arbol)
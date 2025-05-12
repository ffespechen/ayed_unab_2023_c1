class NodoArbol:
    def __init__(self, info):
        self.izquierda = None
        self.derecha = None
        self.info = info


def arbol_vacio(raiz):
    return raiz == None

def insertar_nodo(raiz, dato):
    if arbol_vacio(raiz):
        raiz = NodoArbol(dato)
    elif (raiz.info <= dato):
        raiz.derecha = insertar_nodo(raiz.derecha, dato)
    else:
        raiz.izquierda = insertar_nodo(raiz.izquierda, dato)
    return raiz

def imprimir_arbol(raiz):
    if arbol_vacio(raiz):
        print("-")
    else:
        print(raiz.info)
        print("IZQUIERDA")
        imprimir_arbol(raiz.izquierda)
        print("DERECHA")
        imprimir_arbol(raiz.derecha)



arbol = insertar_nodo(None, 33)
arbol = insertar_nodo(arbol, 11)
arbol = insertar_nodo(arbol, 24)
arbol = insertar_nodo(arbol, 22)
imprimir_arbol(arbol)
class Nodo:
    '''Clase que representa un Nodo para construir una Pila'''
    def __init__(self, dato=None, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente


class Pila:
    '''Implementación de una Pila en Python'''
    def __init__(self):
        self.cima = None 
        self.tamanio = 0


def push(pila, dato_nuevo): # apilar
    '''Agrega un nuevo nodo a la cima de la Pila'''
    nodo_a_apilar = Nodo(dato_nuevo)
    nodo_a_apilar.siguiente = pila.cima
    pila.cima = nodo_a_apilar
    pila.tamanio += 1


def pop(pila): # desapila
    '''Devuelve el último nodo ingresado LIFO, y lo remueve de la Pila'''
    if pila.tamanio == 0:
        raise RuntimeError("No hay más elementos para remover")
    else:
        nodo_a_retornar = pila.cima
        pila.cima = nodo_a_retornar.siguiente
        pila.tamanio -= 1
        return nodo_a_retornar

def is_empty(pila):
    return (pila.tamanio == 0)

def top(pila):
    '''Muestra el valor del nodo en la cima de la Pila'''
    if pila.tamanio == 0:
        return None
    else:
        return pila.cima.dato

def print_pila(pila):
    if pila.tamanio == 0:
        print("PILA VACÍA!!")
    else:
        nodo = pila.cima
        print(pila.cima.dato)
        while (nodo.siguiente is not None):
            nodo = nodo.siguiente
            print(nodo.dato)


pila1 = Pila()
push(pila1, 'A')
push(pila1, 'B')
push(pila1, 'C')
print(F"El último elemento es: {top(pila1)}")
print(pila1.tamanio)
print(F"La pila está vacía? {is_empty(pila1)}")

print('---------')
print_pila(pila1)
print('---------')

resultado = pop(pila1)
print(resultado.dato)
resultado = pop(pila1)
print(resultado.dato)
resultado = pop(pila1)
print(resultado.dato)
print(F"La pila está vacía? {is_empty(pila1)}")
print(F"El último elemento es: {top(pila1)}")
print_pila(pila1)
resultado = pop(pila1)
print(resultado.dato)
print(pila1.cima.dato)
print(pila1.tamanio)

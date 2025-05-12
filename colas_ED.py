class NodoCola:
    def __init__(self, info=None, siguiente=None):
        self.info = info
        self.siguiente = siguiente


class Cola:
    def __init__(self):
        self.frente = None
        self.final = None
        self.tamanio = 0


def push(cola, dato):
    nodo = NodoCola(dato)
    if (cola.frente is None):
        cola.frente = nodo
    else:
        cola.final.siguiente = nodo
    cola.final = nodo
    cola.tamanio += 1

def pop(cola):
    dato = cola.frente.info
    cola.frente = cola.frente.siguiente
    if (cola.frente is None):
        cola.final = None
    cola.tamanio -= 1
    return dato 

def imprimir(cola):
    pass

cola = Cola()
push(cola, 'a')
push(cola, 'b')
push(cola, 'c')

print(F"En la cola, el elemento al frente es: {cola.frente.info}")
print(F"En la cola, al final nos quedó: {cola.final.info}")

print(F"Hago un POP {pop(cola)}")
print(F"Hago un POP {pop(cola)}")
print(F"Hago un POP {pop(cola)}")
print(F"Hago un POP {pop(cola)}")
print(F"En la cola, el elemento al frente es: {cola.frente.info}")
print(F"En la cola, al final nos quedó: {cola.final.info}")
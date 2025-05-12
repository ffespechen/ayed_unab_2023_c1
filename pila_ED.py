class NodoPila:
    def __init__(self, info=None, siguiente=None):
        self.info = info
        self.siguiente = siguiente


class Pila:
    def __init__(self):
        self.cima = None 
        self.tamanio = 0


def apilar(pila, dato):
    nodo = NodoPila(dato)
    nodo.siguiente = pila.cima
    pila.cima = nodo
    pila.tamanio += 1

def desapilar(pila):
    nodo = None
    if (pila.tamanio > 0):
        nodo = pila.cima
        pila.cima = nodo.siguiente
        pila.tamanio -= 1
    return nodo

def cima(pila):
    pass 

def imprimir(pila):
    pass 

pila = Pila()
apilar(pila, 'A')
apilar(pila, 'B')
apilar(pila, 'C')
apilar(pila, 'D')

print(f"En la cima está el valor {pila.cima.info}")

desapilar(pila)
desapilar(pila)
desapilar(pila)
desapilar(pila)
desapilar(pila)

# print(f"En la cima está el valor {pila.cima.info}")
print(f"La pila tiene {pila.tamanio} elementos")

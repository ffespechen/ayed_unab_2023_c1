class Nodo:
    '''Nodo que utilizaremos para construir Colas'''
    def __init__(self, dato=None, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente 


class Cola:
    '''Implementación de una Cola en Python '''
    def __init__(self):
        self.frente = None
        self.final = None 
        self.tamanio = 0


def enqueue(cola, dato): # Encolar / Push
    nodo = Nodo(dato)
    if cola.frente is None:
        cola.frente = nodo 
    else:
        cola.final.siguiente = nodo 
    cola.final = nodo
    cola.tamanio += 1

def dequeue(cola):
    if cola.tamanio == 0:
        raise RuntimeError("No se puede remover un elemento de la Cola vacía")
    else:
        nodo_a_devolver = cola.frente 
        cola.frente = nodo_a_devolver.siguiente
        if (cola.frente is None):
            cola.final = None
        cola.tamanio -= 1
        return nodo_a_devolver

def is_empty(cola):
    return (cola.tamanio == 0)

##-- Implementar función imprimir_cola
##-- Usando el atributo tamanio
def imprimir_cola(cola):
    if cola.tamanio == 0:
        print("COLA VACÍA")
    else:
        nodo = cola.frente
        contador = 0
        while (contador < cola.tamanio):
            print(nodo.dato)
            nodo = nodo.siguiente
            contador += 1

##-- Función primero()
def first(cola):
    return (None if cola.tamanio == 0 else cola.frente.dato)


#--- Pruebas de funcionamiento
cola1 = Cola()
print(f"--->   {first(cola1)}")

enqueue(cola1, 'A')
enqueue(cola1, 2)
enqueue(cola1, 'C')
enqueue(cola1, 'd')
print(f"Al frente de la cola está el: {cola1.frente.dato}")
print(f"Al final de la cola está el: {cola1.final.dato}")

print(f"--->   {first(cola1)}")
# print(f"Remuevo el primer elemento de la Cola: {dequeue(cola1).dato}")
# print(f"Remuevo el segundo elemento de la Cola: {dequeue(cola1).dato}")
# print(f"Remuevo el tercer elemento de la Cola: {dequeue(cola1).dato}")
# print(f"Remuevo el cuarto elemento de la Cola: {dequeue(cola1).dato}")
imprimir_cola(cola1)
print(f"El tamaño de la cola es: {cola1.tamanio}")
print(f"Remuevo otro elemento de la Cola: {dequeue(cola1).dato}")
class Cola:
    '''Implementación de una Cola en Python, usando listas'''
    def __init__(self):
        self.elementos = [] 

    def is_empty(self) -> bool:
        return (len(self.elementos) == 0)
    
    def len(self) -> int:
        return len(self.elementos)
    
    def enqueue(self, nuevo_elemento):
        '''push - encolar'''
        self.elementos.append(nuevo_elemento)

    def dequeue(self):
        '''pop - desencolar'''
        if len(self.elementos) == 0:
            return None
        else:
            return self.elementos.pop(0)
        
    def first(self):
        if len(self.elementos) == 0:
            return None
        else:
            return self.elementos[0]
        

cola1 = Cola()
print(F"La cantidad de elementos de cola1 es {cola1.len()}")
print(F"cola1 está vacío? {cola1.is_empty()}")
cola1.enqueue('A')
cola1.enqueue('B')
cola1.enqueue('C')
cola1.enqueue('D')
print(F"La cantidad de elementos de cola1 es {cola1.len()}")
print(F"cola1 está vacío? {cola1.is_empty()}")
print(F"El primer elemento es... {cola1.first()}")
print(F"Saco el primer elemento: {cola1.dequeue()}")
print(F"El primer elemento es... {cola1.first()}")
print(F"La cantidad de elementos de cola1 es {cola1.len()}")

## Escribir un programa que use nuestra Pila o Cola, y use los métodos implementados
## Tiene que recibir n cantidad de elementos
## Los agrega (push / enqueue) 
## Usando un while, los va sacando y mostrando
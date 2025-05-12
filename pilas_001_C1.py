class Pila:
    '''Estructura Pila implementada con una lista de Python'''
    def __init__(self):
        '''Inicializa una pila vacía'''
        self.elementos = []

    def len(self) -> int:
        '''Devuelve la cantida de elementos de la pila'''
        return len(self.elementos)
    
    def is_empty(self) -> bool:
        '''Devuelve True si la lista está vacía'''
        return (len(self.elementos) == 0)
    
    def push(self, nuevo_elemento):
        '''Agrega un elemento en el top de la pila'''
        self.elementos.append(nuevo_elemento)

    def pop(self):
        '''Remueve y devuelve el último elemento'''
        if (len(self.elementos) == 0):
            return None 
        else:
            return self.elementos.pop() 
    
    def top(self):
        '''Muestra el último elemento'''
        if (len(self.elementos) == 0):
            return None 
        else:
            return self.elementos[-1]
        
    def list_elements(self):
        return self.elementos[::-1]


pila1 = Pila()
print(F"La cantidad de elementos de la Pila es {pila1.len()}")
print(F"La Pila está vacía? {pila1.is_empty()}")
pila1.push('A')
pila1.push('B')
pila1.push('C')
print(F"La cantidad de elementos de la Pila es {pila1.len()}")
print(F"La Pila está vacía? {pila1.is_empty()}")
print(F"El último elemento ingresado en la Pila es {pila1.top()}")
print(F"Remuevo el último elemento de la Pila, y lo muestro {pila1.pop()}")
print(F"La cantidad de elementos de la Pila es {pila1.len()}")
print(pila1.list_elements())

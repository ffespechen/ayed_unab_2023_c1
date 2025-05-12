class Cola:
    '''Clase Cola implementada con lista en Python'''
    def __init__(self):
        self.elementos = []

    def tamanio(self) -> int:
        return len(self.elementos)
    
    def cola_vacia(self) -> bool:
        return (len(self.elementos) == 0)
    
    def en_frente(self):
        if len(self.elementos) == 0:
            return None
        return self.elementos[0]
    
    def push(self, nuevo_elemento):
        self.elementos.append(nuevo_elemento)

    def pop(self):
        if len(self.elementos) == 0:
            return None
        return self.elementos.pop(0)
    
    def mover_al_final(self):
        if not (len(self.elementos) == 0):
            elemento = self.pop()
            self.push(elemento)


cola1 = Cola()
print(cola1.en_frente())
print(cola1.tamanio())
cola1.push('A')
cola1.push('B')
cola1.push('C')
cola1.push('D')
print(cola1.en_frente())
print(cola1.tamanio())
cola1.mover_al_final()
print(cola1.en_frente())
print(cola1.pop())
print(cola1.tamanio())
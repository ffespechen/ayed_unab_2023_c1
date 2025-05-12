class Pila:
    '''Implementación de una pila usando listas en Python'''
    def __init__(self):
        self.elementos = []

    def tamanio(self) -> int:
        return len(self.elementos)
    
    def apilar(self, nuevo_elemento):
        self.elementos.append(nuevo_elemento)

    def desapilar(self):
        if len(self.elementos) == 0:
            return None
        return self.elementos.pop()
    
    def lista_vacia(self) -> bool:
        return (len(self.elementos) == 0)
    
    def cima(self):
        if len(self.elementos) == 0:
            return None
        else:
            elemento = self.elementos[-1]
            return elemento
        
    def mostrar_elementos(self):
        print("Cima -----")
        for i in range(len(self.elementos) - 1, -1, -1):
            print(self.elementos[i])
        print("Base -----")
        

pila1 = Pila()
print(pila1.lista_vacia())
print(pila1.mostrar_elementos())
pila1.apilar('A')
pila1.apilar('B')
pila1.apilar('C')
pila1.apilar('D')
print(pila1.cima())
print(pila1.mostrar_elementos())
print(pila1.tamanio())
print(pila1.desapilar())
print(pila1.desapilar())
pila1.apilar('C')
print(pila1.lista_vacia())

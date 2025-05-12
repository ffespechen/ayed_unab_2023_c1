class P:
    '''Clase de ejemplo - Modelo'''
    def __init__(self, nombre: str, valor: int =0):
        self.nombre = nombre
        self.valor = valor 

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str):
            self.__nombre = nuevo_nombre
        else:
            self.__nombre = 'nombre genérico'

    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, nuevo_valor):
        if isinstance(nuevo_valor, int) or isinstance(nuevo_valor, float):
            if nuevo_valor > 0:
                self.__valor = nuevo_valor
            else:
                self.__valor = abs(nuevo_valor)
        else:
            self.__valor = 0

    def metodo_generico(self):
        print(F"Soy un método de P, invocado desde {self.nombre}")

    def __str__(self):
        return F"Me llamo {self.nombre} y tengo un valor de {self.valor}"


# Instancias / Objetos del tipo P
p1 = P('objeto1', 10)
p2 = P('objeto2', 20)

print(type(p1))
print(p1)

p2.nombre = 1.05
p2.valor = -100

p1.metodo_generico()
p2.metodo_generico()
print(p2.valor)
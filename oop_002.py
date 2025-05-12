class Marciano:

    cantidad_marcianos = 0

    @classmethod
    def sumar_marciano(cls):
        cls.cantidad_marcianos += 1

    @classmethod
    def restar_marciano(cls):
        cls.cantidad_marcianos -= 1

    def __init__(self, nombre):
        self.nombre = nombre
        print(F"Nació el Marciano {self.nombre}")
        Marciano.sumar_marciano()

    def __del__(self):
        print(F"Se murío {self.nombre}")
        Marciano.restar_marciano()

print(F"Cantidad de marcianos al inicio {Marciano.cantidad_marcianos}")

m1 = Marciano('pepito')
m2 = Marciano('juancito')
m3 = Marciano('maría')

print(F"Cantidad Marcianos {Marciano.cantidad_marcianos}")

del m3

print(F"Cantidad Marcianos {Marciano.cantidad_marcianos}")
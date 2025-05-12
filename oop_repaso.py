class Automovil:
    def __init__(self, ruedas, color, cantidad_puertas):
        self.ruedas = ruedas
        self.color = color
        self.cantidad_puertas = cantidad_puertas

    @property
    def ruedas(self):
        return self.__ruedas
    
    @ruedas.setter
    def ruedas(self, cantidad_ruedas):
        if isinstance(cantidad_ruedas, int):
            if cantidad_ruedas > 2:
                self.__ruedas = cantidad_ruedas
            else:
                raise ValueError("No puede tener menos de 3 ruedas")
        else:
            raise TypeError("Las ruedas tienen que ser números enteros")
    
    @property
    def cantidad_puertas(self):
        return self.__puertas
    
    @cantidad_puertas.setter
    def cantidad_puertas(self, cantidad):
        if isinstance(cantidad, int):
            if cantidad > 0:
                self.__puertas = cantidad
            else:
                raise ValueError("No puede tener 0 o menos puertas!!!!!")
        else:
            raise TypeError("No puedo tener puertas que no sean un número entero")


    def __str__(self):
        return F"Color: {self.color} - Ruedas {self.ruedas} - Cant puertas {self.cantidad_puertas}"


fiat600 = Automovil(5, 'AMARILLO', 2)
print(fiat600)

auto_raro = Automovil(4, 1.25, -5)
auto_raro.ruedas = 0
print(auto_raro)
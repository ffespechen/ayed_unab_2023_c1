class TarjetaCredito:
    '''Clase que representa una Tarjeta de Crédito'''
    def __init__(self, nombre_titular, banco, limite):
        self.__titular = nombre_titular
        self.__banco = banco
        self.limite = limite 
        self.__historial = []

    @property
    def limite(self):
        return self.__limite 
    
    @limite.setter
    def limite(self, nuevo_limite):
        if isinstance(nuevo_limite, int) or isinstance(nuevo_limite, float):
            self.__limite = nuevo_limite
        else:
            self.__limite = 0.0

    @property
    def titular(self):
        return self.__titular 
    
    @property
    def historial(self):
        return self.__historial
    
    def comprar(self, precio):
        if precio < self.__limite:
            self.__historial.append(-precio)
            return True 
        else:
            return False 
        

    def depositar(self, monto):
        if monto <= 0:
            return False 
        else:
            self.__historial.append(monto)
            return True 



tarjeta_maximo = TarjetaCredito('MAXIMO', 'GALICIA', 1000000)
tarjeta_facundo = TarjetaCredito('FACUNDO', 'BBVA', 5000000)
tarjeta_priscilla = TarjetaCredito('PRISCILLA', 'NACIÓN', 10000000)

tarjeta_facundo.limite = 100
print(tarjeta_facundo.limite)
print(tarjeta_priscilla.titular)
print(tarjeta_facundo.comprar(50))
print(tarjeta_facundo.comprar(500))

#--- COMPRAS
tarjeta_priscilla.comprar(500)
tarjeta_priscilla.comprar(500)
tarjeta_priscilla.comprar(2500)
tarjeta_priscilla.comprar(8500)
#--- Cobró el sueldo
tarjeta_priscilla.depositar(1500000)

print(tarjeta_priscilla.historial)
print(F"Estado {sum(tarjeta_priscilla.historial)}")
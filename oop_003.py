class Persona:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni
        print("En el constructor de persona")

    def __str__(self):
        return f"Soy una persona, {self.nombre}"
    
# p1 = Persona('Candela', 55111000)
# p2 = Persona('Nazareno', 66333111)

class Empleado(Persona):
    def __init__(self, nombre, dni, sueldo, sucursal):
        super().__init__(nombre, dni)
        self.sueldo = sueldo
        self.sucursal = sucursal 
        print("En el constructor de Empleado")

    def __str__(self):
        return f"Soy un empleado {self.nombre}"
    
    def calcular_sueldo(self):
        return self.sueldo


class Vendedor(Empleado):
    def calcular_sueldo(self):
        pass

    def cantidad_de_ventas(self):
        pass


class Administrativo(Empleado):
    def calcular_sueldo(self):
        pass 

    def obtener_horas_extra(self):
        pass 


e1 = Empleado('Maylen', 66000111, 1700000, 'CASA CENTRAL')
e2 = Empleado('Lucas', 66222150, 1500000, 'SUC 1')

print(e1)
print(e1.calcular_sueldo())

print(e2)
print(e2.calcular_sueldo())


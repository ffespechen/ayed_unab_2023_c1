def sumar(valor1: float, valor2: float) -> float:
    return valor1 + valor2


def calcular_precio_total(precio: float, descuento: int, iva: float = 0.21, iibb: float = 0.02) -> float:
    return precio * (1 + iva) * ((100-descuento)/100)


print(sumar(1.5, 0.23))
print(sumar('A', 'B'))

print(calcular_precio_total(10000, 0))
print(calcular_precio_total(25000, 50))
print(calcular_precio_total(100000, 10))
print(calcular_precio_total(10000, 0, 0.105))
print(calcular_precio_total(1000, 20, iibb=0.05))
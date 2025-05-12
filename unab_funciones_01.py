def sumar(numero1: int, numero2: int) -> int:
    
    if (isinstance(numero1, int) or isinstance(numero1, float)) and (isinstance(numero2, int) or isinstance(numero2, float)):
        return numero1 + numero2
    else:
        raise TypeError("Debe ingresar dos números enteros")


def dividir(numero1, numero2, dividir_por=2):
    if dividir_por == 0:
        raise ZeroDivisionError('Fijate que me pasaste un cero!!!')
    return (numero1 + numero2) / dividir_por



resultado = sumar(11.5, 3)
print(resultado)

resultado1 = dividir(3, 2, 0)
resultado2 = dividir(5, 5, 10)

print(resultado1)
print(resultado2)
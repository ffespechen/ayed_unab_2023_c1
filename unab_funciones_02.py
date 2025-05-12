def sumar_numeros(*args):
    suma = 0
    for numero in args:
        suma = numero
    return suma


def funcionN(multiplica, *args):
    for i in range(0, len(args)):
        if i % 2 == 0:
            print(F"El número {args[i]} multiplicado por {multiplica} resulta {args[i]*multiplica}")
        else:
            print(F"El número {args[i]} dividido por {multiplica} resulta {args[i]/multiplica}")


resultado = sumar_numeros(2, 2, 3, 4, 5, 9)
resultado1 = sumar_numeros(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)

print(resultado)
print(resultado1)

funcionN(2, 1, 2, 3, 4, 5, 6, 7, 8, 9)
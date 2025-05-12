lista0 = [5, -3, 7, -11, 5, 9, -13, 0]

for i in range(0, len(lista0)):
    tipo = ''
    if lista0[i] % 2 == 0:
        tipo = 'PAR'
    else:
        tipo = 'IMPAR'
    print(F"En la posición {i} está el elemento {lista0[i]} y es {tipo}")

print(F"\n {'x' * 30} \n")

for j in lista0:
    print(j)

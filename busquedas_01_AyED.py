datos = ['A', 'C', 'L', 'D', 'X', '4', 'm', 'a', 'p', 'H', 'c', 'c', 'z', 'S', '9', '0']

encontrado = False
posicion = 0
comparaciones = 0

a_encontrar = input('Ingrese el valor a buscar -> ')

# Enfoque 1 - Recorre TODA LA LISTA aunque ya haya encontrado el elemento
# for dato in datos:
#     comparaciones += 1
#     if dato == a_encontrar:
#         encontrado = True
#         print(F"Encontrado en posición {posicion}")
#     posicion += 1

# Enfoque 2 - Recorre la LISTA y cuando encuentra el elemento, detiene la búsqueda
# for dato in datos:
#     comparaciones += 1
#     if dato == a_encontrar:
#         encontrado = True
#         print(F"Encontrado en posición {posicion}")
#         break 
#     posicion += 1

# Enfoque 3 - Búsqueda utilizando índices
for i in range(0, len(datos)):
    comparaciones += 1
    if datos[i] == a_encontrar:
        encontrado = True
        print(F"Encontrado en posición {i}")
        break 




if not encontrado:
    print("El dato buscado no se encontró")

print(F"Cantidad de comparaciones {comparaciones}")
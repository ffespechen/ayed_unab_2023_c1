lista1 = list()
lista2 = []
lista3 = [3, -1, 8, 6, 5, 1, 1, 3, 9]
lista4 = ['A', 1, 0.25, [1, 3, 5, 7]]

print(F"La lista2 tiene {len(lista2)} elementos al inicio")

# Agrega el elemento al final de la lista
lista2.append('A')
lista2.append('b')
lista2.append(3)
lista2.append(0.1)

lista2.insert(2, 'CCC')

print(F"La lista2 tiene {len(lista2)} elementos al final")
print(lista2)

lista1.insert(3, 'XXX')
print(lista1)

## Eliminar elementos
print(lista2.pop())
print(lista2.pop())

# PILAS
lista_pila = []
lista_pila.append('lunes')
lista_pila.append('martes')
lista_pila.append('miércoles')
print(lista_pila)
print("Comienzo a lavar...")
print(lista_pila.pop())
print(lista_pila.pop())
print(lista_pila.pop())
print(F"Terminé de laavar {len(lista_pila)}")


lista2.append('A')
lista2.append('A')
lista2.append('A')
print(lista2)
print('b' in lista2)
# print(lista2.remove('no existe'))
print(lista2)

print(F"Cuántas letras A hay en lista2? -> {lista2.count('A')}")
print(F"Cuántas letras X hay en lista2? -> {lista2.count('X')}")

# Ordena in place

# print(F"Lista desordenada {lista3}")
# lista3.sort()
# print(F"Lista ordenada {lista3}")
# lista3.reverse()
# print(F"Lista ordenada inversa {lista3}")

print(F"Lista desordenada {lista4}")
lista4.sort()
print(F"Lista ordenada {lista4}")
lista4.reverse()
print(F"Lista ordenada inversa {lista4}")
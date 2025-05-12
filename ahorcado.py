palabra_a_adivinar = 'CUALQUIERA'
CANTIDAD_DE_VIDAS = 20

for i in range(0, CANTIDAD_DE_VIDAS):
  letra_del_usuario = input("Ingrese una letra >> ")

  for letra in palabra_a_adivinar:
    if letra == letra_del_usuario:
      print(letra, end=' ')
    else:
      print(' - ', end=' ')
  
  print()

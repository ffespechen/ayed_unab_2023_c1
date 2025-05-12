def tratar_arbitrarios(param1: int, *args: int) -> None:
    print(type(args))
    for i in args:
        print(i)


def imprimir_por_pantalla(param1, **kwargs):
    print(type(kwargs))
    for k, v in kwargs.items():
        print(f"A la clave {k} le corresponde el valor {v}")


def mostrar_el_mayor(*args: int) -> int:
    # Código para localizar el mayor
    pass

def mostrar_el_menor(*args: int) -> int:
    # Código para localizar el menor
    pass



tratar_arbitrarios(1, 2, 5, 9, -1, -3, -7, 0, 5)
imprimir_por_pantalla(ancho=10, altura=60, color=17)
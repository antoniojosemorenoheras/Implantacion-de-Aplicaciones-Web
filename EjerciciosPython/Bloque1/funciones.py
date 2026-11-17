def pedir_texto(longitud_maxima, pide):
    texto = input(f'Introduce tu {pide} (Longitud Max ({longitud_maxima}): ')

    while len(texto) > longitud_maxima:
        texto = input("Texto demasiado grande. Introducelo de nuevo: ")
    return texto


def saluda():
    print("Hola Buenas")

saluda()
nombre = pedir_texto(10, "nombre")
apellidos = pedir_texto(60, "apellido")

print(f'Eres {nombre} {apellidos}')
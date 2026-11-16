def EscribirCentrado(texto):
    espacios = 40 - len(texto) // 2

    print(" " * espacios + texto)
    print(" " * espacios + "=" * len(texto))

EscribirCentrado(input("Introduce un texto: "))


# Otra versión, guardando el resultado dentro de una variable

def EscribirCentrado2(texto):
    espacios = 40 - len(texto) // 2

    texto_centrado = (" " * espacios + texto)
    subrayado = (" " * espacios + "=" * len(texto))

    return (texto_centrado +  "\n" + subrayado)


resultado = EscribirCentrado2(input("Introduce un texto: "))
print(resultado)
cadena = input("Introduce una cadena de caracteres separados por espacios: ")

contador_espacios = 0

for x in cadena:
    if x == " ":
        contador_espacios += 1

palabras = contador_espacios + 1

print(f'El número de palabras que tiene tu cadena es {palabras}')

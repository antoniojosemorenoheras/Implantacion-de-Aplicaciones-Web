cadena = input("Introduce una cadena de caracteres separados por espacios: ")

# Así lo he había hecho la primera vez
# for x in cadena:
#     if x == " ":
#         contador_espacios += 1

# palabras = contador_espacios + 1

# Con esta solucion es más corto y soporta varios espacios entre palabras

palabras = len(cadena.split())

print(f'El número de palabras que tiene tu cadena es {palabras}')

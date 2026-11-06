cadena = input("Introduce tu nombre completo con los apellidos: ")

iniciales = ""

for palabra in cadena.split():
    iniciales += palabra[0].upper()

print(f'Las iniciales de tu nombre son {iniciales}')
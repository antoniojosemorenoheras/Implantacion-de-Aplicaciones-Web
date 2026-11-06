cadena = input("Introduce una cadena de caracteres: ")
caracter = input("Introduce un caracter: ")

while len(caracter) != 1:
    print(f'Eso no es un caracter solo')
    caracter = input("Introduce de nuevo el caracter: ")

contador = 0

for x in cadena:
    if x == caracter:
        contador += 1

print(f'El número de veces que aparece el caracter en la cadena es {contador}')
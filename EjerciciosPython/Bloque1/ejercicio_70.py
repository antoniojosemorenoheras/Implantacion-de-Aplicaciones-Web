cadena = input("Introduce una cadena de caracteres: ")

apariciones = {}

for letra in cadena:
    if letra in apariciones:
        apariciones[letra] += 1
    else:
        apariciones[letra] = 1

# No distingue entre mayusculas y minisculas y las toma como diferentes

print(f'El diccionario con la cantidad de apariciones de cada caracter es {apariciones}')
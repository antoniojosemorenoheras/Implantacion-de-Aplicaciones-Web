numero = int(input("Introduce un número: "))

cuadrados = {}

for x in range(1, numero + 1):
    cuadrados[x] = x ** 2

print(f'El contenido del diccionario es {cuadrados}')
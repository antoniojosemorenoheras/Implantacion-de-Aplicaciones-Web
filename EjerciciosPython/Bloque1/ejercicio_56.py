numero = int(input("Introduce el número de un mes: "))

while numero > 12 or numero < 0:
    print("Ese número no es el número de un mes")
    numero = int(input("Introduce el número de nuevo: "))


numero = int(input("Introduce el número de un mes: "))

while numero > 12 or numero < 1:
    print("Ese número no es el número de un mes")
    numero = int(input("Introduce el número de nuevo: "))

meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
         "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

posicion = numero - 1

print(f'El mes introducido es {meses[posicion]} y los días que tiene ese mes son {dias[posicion]}')
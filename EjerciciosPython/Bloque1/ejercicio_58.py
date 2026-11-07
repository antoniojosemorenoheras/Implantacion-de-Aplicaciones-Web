nombre = input("Introduce el nombre del alumno: ")
nombres = []
edades = []

while nombre != "*":
    edad = int(input("Cual es la edad del alumno: "))
    nombres.append(nombre)
    edades.append(edad)
    nombre = input("Escribe el siguiente alumno: ")

if len(nombres) > 0:
    print("Estos son alumnos mayores de edad:")

    for x in range(len(nombres)):
        if edades[x] >= 18:
            print(f'El alumno {nombres[x]} es mayor de edad')

    edad_max = max(edades)

    print(f'Alumno o alumnos más mayores ({edad_max} años):')

    for y in range(len(nombres)):
        if edades[y] == edad_max:
            print(f'{nombres[y]}')
else:
    print("No se ha introducido ningún alumno")
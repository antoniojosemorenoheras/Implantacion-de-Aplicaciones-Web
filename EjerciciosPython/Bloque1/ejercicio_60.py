import random

tabla = []

for i in range(5): # 5 filas
    fila = [] # Creamos una lista que vaya a contener los digitos aleatorios
    for j in range(5): # 5 columnas por fila
        fila.append(random.randint(1, 9))
    tabla.append(fila)

# Mostrar la tabla
for fila in tabla:
    print(fila)
    
# Sumar las filas
for x in range(len(tabla)):
    print(f'La suma de la {x} fila es igual a {sum(tabla[x])}')

for j in range(5):                 # recorre las columnas
    total = 0                      # acumulador: se reinicia en cada columna
    for i in range(5):             # recorre las filas
        total += tabla[i][j]          # el número de la fila i, columna j
    print(f'Suma de la columna {j + 1}: {total}')
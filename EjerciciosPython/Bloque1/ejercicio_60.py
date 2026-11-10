# import random

# tabla = []

# for i in range(5): # 5 filas
#     fila = [] # Creamos una lista que vaya a contener los digitos aleatorios
#     for j in range(5): # 5 columnas por fila
#         fila.append(random.randint(1, 9))
#     tabla.append(fila)

# # Mostrar la tabla
# for fila in tabla:
#     print(fila)
    
# # Sumar las filas
# for x in range(len(tabla)):
#     print(f'La suma de la {x} fila es igual a {sum(tabla[x])}')

# for j in range(5):                 # recorre las columnas
#     total = 0                      # acumulador: se reinicia en cada columna
#     for i in range(5):             # recorre las filas
#         total += tabla[i][j]          # el número de la fila i, columna j
#     print(f'Suma de la columna {j + 1}: {total}')


# Parte hecha en clase

tabla = [
    [1 ,2 ,3 ,4 ,5 ],
    [6 ,7 ,8 ,9 ,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
]

# Sumar cada fila
suma = 0
for fila in tabla:
    suma = sum(fila)
    print(f'La suma de la fila {fila} es {suma}')

# Sumar cada columna hecho por mí
columna = 0
posicion = 0
for lista in tabla:
    columna = columna + lista[posicion]
    posicion += 1
    print(f'La suma de la columna {posicion} es igual a {columna}')

# Sumar columna
for indice_columna in range(5):
    suma_columnas = 0
    for indice_fila in range(5):
        suma = suma + tabla[indice_fila][indice_columna]
    print(f'La suma de la columna {indice_columna} es {suma_columnas}')
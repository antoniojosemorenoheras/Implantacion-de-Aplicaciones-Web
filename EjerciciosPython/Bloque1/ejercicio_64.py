# ---------- LECTURA DE DATOS ----------
precios = []
cantidades = []

for i in range(5):
    precio = float(input(f"Precio del artículo {i + 1}: "))
    precios.append(precio)

    fila = []
    for j in range(4):
        cantidad = int(input(f"  Cantidad del artículo {i + 1} en la sucursal {j + 1}: "))
        fila.append(cantidad)
    cantidades.append(fila)

# ---------- 1. CANTIDADES TOTALES DE CADA ARTÍCULO ----------
print("\n--- Cantidades totales por artículo ---")
for x in range(len(cantidades)):
    print(f'Total vendido del artículo {x + 1}: {sum(cantidades[x])}')

# ---------- 2. CANTIDAD DE ARTÍCULOS EN LA SUCURSAL 2 ----------
total_sucursal2 = 0
for i in range(len(cantidades)):
    total_sucursal2 += cantidades[i][1]
print(f'\nArtículos vendidos en la sucursal 2: {total_sucursal2}')

# ---------- 3. CANTIDAD DEL ARTÍCULO 3 EN LA SUCURSAL 1 ----------
print(f'Cantidad del artículo 3 en la sucursal 1: {cantidades[2][0]}')

# ---------- 4. RECAUDACIÓN TOTAL DE CADA SUCURSAL ----------
print("\n--- Recaudación por sucursal ---")
recaudaciones = []

for j in range(4):
    total = 0
    for i in range(5):
        total += cantidades[i][j] * precios[i]
    recaudaciones.append(total)
    print(f'Recaudación de la sucursal {j + 1}: {total:.2f} €')

# ---------- 5. RECAUDACIÓN TOTAL DE LA EMPRESA ----------
total_empresa = sum(recaudaciones)
print(f'\nRecaudación total de la empresa: {total_empresa:.2f} €')

# ---------- 6. SUCURSAL DE MAYOR RECAUDACIÓN ----------
maxima = max(recaudaciones)
sucursal_max = recaudaciones.index(maxima) + 1
print(f'La sucursal con mayor recaudación es la {sucursal_max} con {maxima:.2f} €')
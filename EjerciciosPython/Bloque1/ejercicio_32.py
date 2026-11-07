ahorro = 0

for mes in range(12):
    deposito = float(input(f'Introduce la cantidad del deposito del mes {mes + 1}: '))
    while deposito < 0:
        print("No puedes depositar cantidades negativas")
        deposito = float(input(f'Introduce la cantidad del deposito del mes {mes + 1}: '))
       
    ahorro = deposito + ahorro
    print(f'Hasta ahora llevas ahorrados {ahorro:.2f} euros')

print(f'Has ahorrado {ahorro} euros')
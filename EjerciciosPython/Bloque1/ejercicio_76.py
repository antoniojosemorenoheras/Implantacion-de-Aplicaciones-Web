def EsMultiplo (numero1, numero2):
    if numero1 % numero2 == 0:
        multiplo = True
    else:
        multiplo = False

    return multiplo

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

condicion1 = EsMultiplo(numero1, numero2)
condicion2 = EsMultiplo(numero2, numero1)

if condicion1 == True or condicion2 == True:
    print(f'Los números {numero1} y {numero2} uno es múltiplo del otro')
else: 
    print(f'Los números {numero1} y {numero2} no son múltiplos')

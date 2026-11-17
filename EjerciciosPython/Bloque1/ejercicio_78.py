def Segundos_HorasMinutos(segundos):
    horas = segundos // 3600
    resto = segundos % 3600
    minutos = resto // 60
    segundos = resto % 60

    return horas, minutos, segundos

def HorasMinutos_Segundos(horas, minutos, segundos):
    segundos_totales = (horas * 3600) + (minutos * 60) + segundos

    return segundos_totales


programa = -1
while programa != 0:
    print("Bienvenido al Programa")
    print("Pulsa 1 para convertir tus segundos a horas minutos y segundos")
    print("Pulsa 2 para convertir tu tiempo a segundos")
    print("Pulsa 0 para salir del Programa")

    programa = int(input("Introduce un número: "))

    if programa == 1:
        pido = int(input("Introduce los segundos: "))
        horas, minutos, segundos = Segundos_HorasMinutos(pido)
        print(f'Los {pido} segundos equivalen a {horas} horas, {minutos} minutos y {segundos} segundos')

    elif programa == 2:
        horas = int(input("Introduce las horas: "))
        minutos = int(input("Introduce los minutos: "))
        segundos = int(input("Introduce los segundos: "))

        cambio = HorasMinutos_Segundos(horas, minutos, segundos)
        print(f'Las {horas} horas, los {minutos} minutos y los {segundos} segundos equivalen a {cambio} segundos')

    elif programa == 0:
        print("Has cerrado el programa")

    else:
        print("El número que has pulsado no esta en el programa")
agenda = {}

menu = -1

while menu != 0:
    print("--- Para añadir o modificar introduce 1 ---")
    print("--- Para buscar usa el número 2 ---")
    print("--- Si quieres borrar algún registro introduce 3 ---")
    print("--- Mostrar todos los contactos de la agenda con el 4 ---")
    print("--- Salir del Menú con el 0 ---")

    menu = int(input("¿Que opción eliges? "))

    if menu == 1:
        nombre = input("Introduce un nombre: ")
        if nombre in agenda:
            print(f'El telefono de esa persona es: {agenda[nombre]}')
            pregunta = input("¿Es correcto el número? (s/n)")
            if pregunta == "n":
                numero = input("Introduce el número correcto: ")
                agenda[nombre] = numero
        else:
            print("El nombre no esta en la agenda")
            numero = input("Escribe el numero de la persona: ")
            agenda[nombre] = numero

    elif menu == 2:
        cadena = input("Introduce una cadena por la que pueda comenzar el contacto: ")
        existe = False
        for nombre, telefono in agenda.items():
            if nombre.startswith(cadena):
                print(f'{nombre} --> {telefono}')
                existe = True
        if existe == False:
            print(f'No existen contacto que empiezen por {cadena}')
            
    elif menu == 3:
        nombre = input("Escribe el nombre: ")
        if nombre in agenda:
            pregunta = input("¿Quieres borrarlo de la agenda? (s/n)")
            if pregunta == "s":
                del agenda[nombre]
                print("Contacto borrado")
            else:
                print("No se ha borrado")
        else:
            print("El nombre no esta en la agenda")

    elif menu == 4:
        if len(agenda) >= 1:
            print("Los contactos de la agenda son los siguientes:")
            for nombre, telefono in agenda.items():
                print(f'{nombre} --> {telefono}')
        else:
            print("No hay contactos en la lista")

    elif menu == 0:
        break

    else:
        print("Esa opción no esta en la lista")

print("Cerraste el menú")
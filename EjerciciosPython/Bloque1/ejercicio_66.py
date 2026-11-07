numeros = []
opcion = 0

while opcion != 9:
    print("")
    print("--- MENÚ ---")
    print("1. Añadir número a la lista")
    print("2. Añadir número en una posición")
    print("3. Longitud de la lista")
    print("4. Eliminar el último número")
    print("5. Eliminar un número")
    print("6. Contar números")
    print("7. Posiciones de un número")
    print("8. Mostrar números")
    print("9. Salir")
    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        numero = int(input("Escribe el número: "))
        numeros.append(numero)

    elif opcion == 2:
        numero = int(input("Introduce el número: "))
        posicion = int(input("Introduce la posición: "))
        if 1 <= posicion <= len(numeros):
            numeros.insert(posicion -1, numero)
            print(f'El número {numero} se ha introducido en la posición {posicion}')
        else:
            print("Esa posición no existe en la lista")


    elif opcion == 3:
        print(f'La lista tiene {len(numeros)} números dentro de ella')

    elif opcion == 4:
        if len(numeros) == 0:
            print("La lista no tiene números para eliminar")
        else:
            ultimo = numeros.pop()
            print(f'Has eliminado el número {ultimo}')

    elif opcion == 5:
        posicion = int(input("Escribe la posición que qieres eleiminar: "))
        if 1 <= posicion <= len(numeros):
            eliminado = numeros.pop(posicion - 1)
            print(f'Se ha borrado la posicion {posicion} que tenia el número {eliminado}')
        else:
            print("Esa posicion no esta en la lista")

    elif opcion == 6:
        contar = int(input("Introduce el número que quieres contar: "))
        if contar in numeros:
            print(f'El número {contar} aparece {numeros.count(contar)} veces')
        else:
            print("El número que quieres contar no esta en la lista")

    elif opcion == 7:
        buscar = int(input("Introduce el número que quieres buscar: "))
        if buscar in numeros:
            for i in range(len(numeros)):
                if numeros[i] == buscar:
                    print(f'El número introducido esta en la posición {i + 1}')
        else:
            print("El número no esta en la lista")

    elif opcion == 8:
        print(numeros)

    elif opcion == 9:
        print("Se ha acabado el programa")

    else:
        print("Ese número no esta en la lista de opciones")
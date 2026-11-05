cadena = input("Introduce una cadena de texto: ")
subcadena = input("Introduce tu subcadena: ")

if cadena[:len(subcadena)] == subcadena:
    print("La subcadena comienza como la cadena principal")
else:
    print("La subcadena no comienza como la cadena principal")
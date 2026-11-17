def Login (nombre, contraseña, intentos):
    if nombre == "usuario1" and contraseña == "asdasd":
        comprobacion = True
    else:
        comprobacion = False
        intentos += 1
    return comprobacion, intentos


intentos = 0
entrado = False


while intentos != 3 and entrado == False:
    usuario = input("Introduce el nombre de usuario: ")
    contraseña = input("Introduce la contraseña: ")
    entrado, intentos = Login(usuario, contraseña, intentos)
    if entrado == False and intentos < 3:
        print("El usuario o la contraseña no son correctos")
        print(f'Te quedan {3 - intentos} intentos')

if entrado == True:
    print("Bienvenido al programa")
else:
    print("Has agotado los 3 intentos")
notas = []

for x in range(1, 6):
    nota = float(input("Nota del examen: "))
    while nota > 10 or nota < 0:
        print("Eso no es una nota válida")
        nota = float(input("Vuelve a introducir la nota: "))
    notas.append(nota)

print(f'La lista de notas introducidas es {notas}')

media = sum(notas) / len(notas)
nota_maxima = max(notas)
nota_minima = min(notas)

print(f'La media de las notas introducidas es {media:.2f}, la máxima nota es {nota_maxima} y la nota más baja es {nota_minima}')

# Versión hecha en clase
notas = []

for iterador in range(0,5):
    nota = int(input("Introduce una nota: "))
    if nota >= 0 and nota <= 10:
        notas.append(nota)



# Versión V2 en clase
notas = []
numero_nota = 0

while numero_nota < 5: # while len(notas) < 5:
    nota = int(input("Introduce una nota: "))
    if nota >= 0 and nota <= 10:
        notas.append(nota)

print(f'Notas introducidas en notas = {notas}')

# Es hacer lo que hace sum():
# suma = 0
# for nota in notas:
#     suma = suma + nota

media = sum(notas) / len(notas)

print(f'Nota media {media}')

print(f'Nota mínima {min(notas)}')

maximo = -1
for nota in notas:
    if nota > maximo
        maximo = nota

print(f'Nota máxima {maximo}')
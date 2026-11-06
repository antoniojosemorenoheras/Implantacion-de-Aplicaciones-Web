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
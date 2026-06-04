notas = []
for i in range(10):
    nota = float(input("Digite a nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)

acima = 0
for nota in notas:
    if nota > media:
        acima += 1

print(notas)
print(str(media))
print(str(acima))
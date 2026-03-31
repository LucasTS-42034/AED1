qtd = int(input("Quantas notas você vai digitar? \n"))
nots = []

for i in range(qtd):
    n = float(input("Digite a nota: \n"))
    nots.append(n)

med = sum(nots) / len(nots)

print("A média é: " + str(med))

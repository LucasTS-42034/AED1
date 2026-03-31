qtd = int(input("Quantas notas você vai digitar? \n"))
nots = []
maior = int(0)

for i in range(qtd):
    n = int(input("Digite a nota: \n"))
    if n > maior:
        maior = n

print("A maior nota é " + str(maior))

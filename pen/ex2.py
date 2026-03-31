qtd = int(input("Quantas notas você vai digitar? \n"))
nots = []
apr = int(0)
rep = int(0)

for i in range(qtd):
    n = float(input("Digite a nota: \n"))
    if n >= 7:
        apr+= 1
    else:
        rep+= 1

print("A quantidade de aprovados é de " + str(apr))
print("A quantidade de reprovados é de: " + str(rep))
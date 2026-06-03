matriz = []
soma = 0

for i in range(4):
    linha = []
    for j in range(4):
        n = int(input("Digite um número: \n"))
        linha.append(n)
        if i == j:
            soma += n
    matriz.append(linha)

for linha in matriz:
    print(linha)

print(str(soma))
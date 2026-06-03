matriz = []
soma = 0
n = 0

for i in range(4):
    linha = []
    for j in range(4):
        n = int(input("Digite um número: \n"))
        linha.append(n)
    matriz.append(linha)

for linha in matriz:
    print(linha)

for i in range(4):
    soma = sum(matriz[i])
    print("Linha: " + str(soma))
def somad(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == j:
                soma += matriz[i][j]
    return soma

matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input("Digite um número: ")))
    matriz.append(linha)

for linha in matriz:
    print(linha)

print("Soma da diagonal principal: " + str(somad(matriz)))
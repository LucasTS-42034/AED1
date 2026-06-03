matriz = []
matriz_transposta = []

for i in range(3):
    linha = []
    for j in range(4):
        n = int(input("Digite um número: \n"))
        linha.append(n)
    matriz.append(linha)

for j in range(4):
    nova = []
    for i in range(3):
        nova.append(matriz[i][j])
    matriz_transposta.append(nova)

print("Matriz original: ")
for linha in matriz:
    print(linha)

print("Matriz transposta: ")
for linha in matriz_transposta:
    print(linha)
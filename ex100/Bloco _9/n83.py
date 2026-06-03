matriz1 = []
matriz2 = []
soma = []

for i in range(2):
    linha = []
    for j in range(2):
        n = int(input("Digite um número: \n"))
        linha.append(n)
    matriz1.append(linha)

for i in range(2):
    linha = []
    for j in range(2):
        n = int(input("Digite um número: \n"))
        linha.append(n)
    matriz2.append(linha)

for i in range(2):
    linha_soma = []
    for j in range(2):
        linha_soma.append(matriz1[i][j] + matriz2[i][j])
    soma.append(linha_soma)

for linha in soma:
    print(linha)
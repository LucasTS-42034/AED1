matriz = []
maior = 0
linh = 0
coluna = 0

for i in range(3):
    linha = []
    for j in range(3):
        n = int(input("Digite um número: \n"))
        linha.append(n)
        if maior is None or n > maior:
            maior = n
            linh = i
            coluna = j
    matriz.append(linha)

for linha in matriz:
    print(linha)

print("Maior valor: " + str(maior))
print("[" + str(linh) + "," + str(coluna) + "]")
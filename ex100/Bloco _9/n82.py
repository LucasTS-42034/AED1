matriz = []
conta = 0

for i in range(3):
    linha = []
    for j in range(3):
        n = int(input("Digite um número: \n"))
        linha.append(n)
        if n % 2 == 0:
            conta += 1
    matriz.append(linha)

for linha in matriz:
    print(linha)

print("Quantidade de números pares: " + str(conta))
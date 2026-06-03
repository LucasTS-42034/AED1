matriz = []
n = 0
soma = 0
for i in range(3):          
    linha = []
    for j in range(3):      
        n = int(input(f"Digite um  número: \n"))
        linha.append(n)
        soma += n
    matriz.append(linha)

for linha in matriz:
    print(linha)

print(str(soma))
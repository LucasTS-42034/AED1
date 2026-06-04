lista = []
for i in range(10):
    n = int(input("Digite um número: \n"))
    lista.append(n)

valor = int(input("Digite o valor que deseja procurar: \n"))
contagem = 0

for num in lista:
    if num == valor:
        contagem += 1

print("O valor " + str(valor) + " aparece " + str(contagem) + " vezes.")
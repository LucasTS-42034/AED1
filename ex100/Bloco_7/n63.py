lis = []
i = int(0)
maior = int(0)
for i in range(8):
    n = int(input("Digite um número: \n"))
    if maior < n:
        maior = n
    lis.append(n)
    i+=1

print("O maior número é: " + str(n) + " e sua posição é " + str(lis.index(maior)))

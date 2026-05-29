lis = []
i = 0
p = int(input("Digite o valor que deseja procurar\n"))
l = 0
for i in range(10):
    n = int(input("Digite um número: \n"))
    lis.append(n)
    if p == n:
        l += 1
    i+=1

print(f"O número {p} apareceu cerca de {l} vezes na lista.")

lis = []
i = 0
menor = 0
for i in range(5):
    n = int(input("Digite um número: \n"))
    lis.append(n)
    if n < menor:
        n = menor
    i+=1


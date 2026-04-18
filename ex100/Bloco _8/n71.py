lis = []
i = int(0)
for i in range(10):
    n = int(input("Digite um número: \n"))
    lis.append(n)
    i+=1

soma = sum(lis)
print("A soma é " + str(soma))
med = float(soma / 10)
print("A média é de: " + str(med))

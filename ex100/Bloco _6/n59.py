n = int(input("Digite um número: \n"))
soma = int(0)
if n > 0:
    for i in range(1, n):
        if n % i == 0:
            soma += i

if soma == n:
    print("O número " + str(n) + " é perfeito!")
else:
    print("O número " + str(n) + " não é perfeito.")

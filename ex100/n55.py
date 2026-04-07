n = int(input("Digite um número: \n"))
soma = int(0)
if n > 0:
    for i in range(2, 101):
        if n % i == 0:
            soma += i


print(soma)
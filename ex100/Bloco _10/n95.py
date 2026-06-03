def fatorial(n):
    if n < 0:
        print("Número inválido!")
        return 0
    elif n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)

num = int(input("Digite um número inteiro: "))

while True:
    if num < 0:
        print("Número inválido!")
    else:
        break

print("Fatorial: " + str(fatorial(num)))
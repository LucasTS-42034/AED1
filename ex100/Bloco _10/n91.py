def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

num = int(input("Digite um número inteiro para calcular o fatorial: "))
print(fatorial(num))
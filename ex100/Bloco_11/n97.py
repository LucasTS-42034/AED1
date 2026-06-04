def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

posicao = int(input("Digite a posição desejada: "))

while True:
    if posicao < 0:
        print("Número inválido!")
    else:
        break

resultado = fibonacci(posicao)
print("Valor na posição " + str(posicao) + ": " + str(resultado))
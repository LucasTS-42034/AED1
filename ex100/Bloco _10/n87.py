def maior(a, b):

    return a if a > b else b

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
print("O maior número é: " + str(maior(n1, n2)))
num = int(input("Digite um número inteiro: "))

if num == 0:
    print("0")
else:
    binario = ""
    n = num
    while n > 0:
        resto = n % 2
        binario = str(resto) + binario
        n = n // 2
    print(binario)
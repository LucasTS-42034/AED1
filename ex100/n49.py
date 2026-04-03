n = int(0)
soma = int(0)
while True:
    n = int(input("Digite um número: \n"))
    if n == 0:
        print("A soma é " + str(soma))
        break
    else:
        soma+= n
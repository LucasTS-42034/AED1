x1 = int(input("Digite o primeiro número: \n"))
x2 = int(input("Digite o segundo número: \n"))

if x1 == x2:
    print("Os números são iguais.")
else:
    print("Os números são diferentes.")
    if x1 > x2:
        print("O número " + str(x1) + " é maior que o número " + str(x2))
    elif x2 > x1:
        print("O número " + str(x2) + " é maior que o número " + str(x1))
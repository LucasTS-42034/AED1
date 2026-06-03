x1 = int(input("Digite o primeiro número: \n"))
x2 = int(input("Digite o segundo número: \n"))
x3 = int(input("Digite o terceiro número: \n"))

if x2 < x1 < x3:
    print("O primeiro número é maior que o segundo e menor que o terceiro")
elif x2 < x1 and x3 < x1:
    print("O primeiro número é maior que o segundo e o terceiro")
elif x3 < x1 < x2:
    print("O primeiro número é maior que o terceiro e menor que o segundo")
else:
    print("O primeiro número não é maior que o segundo e não é menor que o terceiro.")


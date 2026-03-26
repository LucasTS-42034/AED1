lad1 = int(input("Digite o primeiro lado: \n"))
lad2 = int(input("Digite o segundo lado: \n"))
lad3 = int(input("Digite o terceiro lado: \n"))


if lad1 < lad2 + lad3 and lad2 < lad1 + lad3 and lad3 < lad1 + lad2:
    if lad1 == lad2 == lad3:
        print("O triângulo é equilátero.")
elif lad1 == lad2 or lad1 == lad3 or lad2 == lad3:
        print("O triângulo é isósceles.")
    else:
        print("O triângulo é escaleno.")
else:
    print("Os lados não podem formar um triângulo.")


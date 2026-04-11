x = int(input("Digite o número: \n"))

if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto.")
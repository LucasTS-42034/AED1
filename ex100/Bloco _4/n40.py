nota1 = int(input("Insira a primeira nota: \n"))
nota2 = int(input("Insira a segunda nota: \n"))
freq = int(input("Insira a frequência: \n"))

media = (nota1 + nota2) / 2  # sem converter para int para preservar decimal

if freq < 70 and media < 60:
    print("Você foi reprovado por frequência e por nota.")
elif freq < 70:
    print("Você foi reprovado por frequência.")
elif media < 60:
    print("Você foi reprovado por nota.")
else:
    print("Parabéns, você foi aprovado!")
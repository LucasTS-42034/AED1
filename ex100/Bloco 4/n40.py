nota1 = int(input("Insira a primeira nota: \n"))
nota2 = int(input("Insira a segunda nota: \n"))
freq = int(input("Insira a frequência: \n"))

media = int((nota1 + nota2) / 2)

if freq < 70 and media < 40:
    print("Você foi reprovado por frequência e por nota.")
elif freq < 70:
    print("Você foi reprovado por frequência.")
elif 40 > media:
    print("Você está reprovado.")
elif media > 70:
    print("Parabens, foi aprovado!")







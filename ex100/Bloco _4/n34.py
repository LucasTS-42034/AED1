nota1 = int(input("Insira a primeira nota: \n"))
nota2 = int(input("Insira a segunda nota: \n"))
nota3 = int(input("Insira a terceira nota: \n"))

media = int((nota1 + nota2 + nota3) / 3)

if media > 70:
    print("Parabens, foi aprovado!")
if 70 > media > 40:
    print("Você está em exame.")
if 40 > media:
    print("Você está reprovado.")
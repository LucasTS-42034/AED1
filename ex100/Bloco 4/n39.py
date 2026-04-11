x = int(input("Digite sua idade: \n"))

if x < 14:
    print("Você é uma criança.")
elif 14 <= x < 18:
    print("Você é um adolescente.")
elif 18 <= x < 60:
    print("Você é um adulto.")
elif x >= 60:
    print("Você é um idoso.")
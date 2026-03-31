peso = int(input("Digite seu peso: \n"))
altura = float(input("Digite sua altura: \n"))

IMC = float(peso / (altura ** 2))

if IMC < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 > IMC < 24.9:
    print("Você está com peso normal.")
elif 25 > IMC < 29.9:
    print("Você está com sobrepeso.")
elif IMC > 30:
    print("Você é obeso.")


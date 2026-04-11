i = int(0)
soma = int(0)
while True:
    idade = int(input("Digite uma idade: \n"))
    media = 0
    if idade <= 0:
        print("Número negativo foi digitado.")
        media = float(soma / i)
        print("A media é de: " + str(media))
        break
    else:
        soma += idade
    i+=1
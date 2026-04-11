dias = int(input("Digite a quantidade de dias: \n"))
horas = int(input("Digite a quantidade de horas: \n"))
minutos = int(input("Digite a quantidade de minutos: \n"))

todia = int(dias * 24)

min = int((todia + horas) * 60)

min+= int(minutos)



print("A quantidade total de minutos é de: " + str(min))
quilo = int(input("Digite a quantidade de quilômetros rodados: \n"))
gas = int(input("Digite a quantidade de litros gastos: \n"))

val = float(quilo / gas)
print("O consumo médio do veículo é de: " + str(val))
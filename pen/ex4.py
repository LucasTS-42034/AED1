qtd = int(input("Quantos valores irá digitar? \n"))
nots = []
x = int(0)

for i in range(qtd):
    n = float(input("Digite o valor: \n"))
    x+= n


print("O total arrecadado é de: " + str(x))

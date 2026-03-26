salario = int(input("Digite o valor do salario: \n"))
desc = int(input("Digite o porcentual do aumento: \n"))

total = int(salario * (desc / 100))
val = int(salario + total)
print("O valor do produto com desconto é de: " + str(val))
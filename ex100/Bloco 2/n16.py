preco = int(input("Digite o preço do produto: \n"))
desc = int(input("Digite o o valor do desconto: \n"))

total = int(preco * (desc / 100))
val = int(preco - total)
print("O valor do produto com desconto é de: " + str(val))
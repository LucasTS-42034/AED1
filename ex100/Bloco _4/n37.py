x = int(input("Digite o valor do produto: \n"))
desc = int(input("Digite o o valor do desconto: \n"))

total = int(x * (desc / 100))
val = int(x - total)
par = int(x / 2)

valo = x * 1.10
pa3 = valo / 3

print("O valor do produto com desconto é de " + str(val))
print("Você poderá pagar em duas parcelas por " + str(par) + " reais.")
print("Você poderá pagar em três parcelas por " + str(pa3) + " reais.")

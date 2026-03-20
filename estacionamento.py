x = int(input("Digite a quantidade de horas: \n"))
preco = 0
esp = str(input("Possui deficiencia? \n"))



if x < 1:
    print("Gratis")

if 1 <= x <= 3:
    x = int(x - 1)
    if esp == "sim":
        preco = int((10 + (x * 5)) * 0.85)
        print("O preco é: " + str(preco) + " reais.")
    if esp == "nao":
        preco = int(10 + (x * 5))
        print("O preco é: " + str(preco) + " reais.")        

if x > 3:
   x = x - 3
   if esp == "sim":
        preco = int((20 + (x * 8)) * 0.85)
        print("O preco é: " + str(preco) + " reais.")
   if esp == "nao":
        preco = int(20 + (x * 8))
        print("O preco é: " + str(preco) + " reais.")
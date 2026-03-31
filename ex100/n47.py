n = int(input("Digite um número: \n"))
x = int(n)
fat = int(1)

while x != 0:
    fat = (fat * x)
    x -= 1

print(fat)

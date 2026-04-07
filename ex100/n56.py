n = int(input("Digite um valor: "))
inv = 0

while n > 0:
    dig = n % 10
    inv = (inv * 10) + dig
    n = int(n / 10)

print(inv)

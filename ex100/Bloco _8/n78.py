lista = []
for i in range(5):
    n = int(input("Digite um número: "))
    lista.append(n)

soma = []
acum = 0
for num in lista:
    acum += num
    soma.append(acum)

print(lista)
print(soma)
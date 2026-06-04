lista = []
pos = []
neg = []
for i in range(10):
    n = int(input("Digite um número: "))
    lista.append(n)
    if n < 0: 
        neg.append(n)
    else:
        pos.append(n)

print(lista)
print(neg)
print(pos)
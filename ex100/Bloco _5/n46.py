x = int(0)
soma = int(0)
pos = int(0)
neg = int(0)
zer = int(0)

while x < 10:
    n = int(input("Digite um número: \n"))
    if n > 0:
        pos += 1
    elif n < 0:
        neg +=1
    else:
        zer += 1
    x = x+1

print(pos)
print(neg)
print(zer)
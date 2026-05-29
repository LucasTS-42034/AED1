lis = []

for i in range(10):
    n = int(input("Digite o número: \n"))
    lis.append(n)

repet = []
for j in lis:
    if j not in repet:
        repet.append(j)

print(repet)
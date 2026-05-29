lis = []
i = int(0)
apr = 0
for i in range(10):
    n = int(input("Digite um número: \n"))
    lis.append(n)
    if n >= 70:
        apr+=1

print(lis)
print(apr)
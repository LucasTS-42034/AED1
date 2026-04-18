lis = []
i = 0
li = []
l = []
for i in range(5):
    n = int(input("Digite a primeira lista: \n"))
    lis.append(n)
    i+=1

for i in range(5):
    n = int(input("Digite a segunda lista: \n"))
    li.append(n)
    i+=1

for i in range(5):
    l.append(lis[i] + li[i])
    i+=1

print(l)

n = int(input("Digite um nymero \n"))
lis = range(1, n)
i = 0
soma = 0
while i != len(lis):
   print(lis[i])
   soma = int(lis[i] + soma)
   i = i + 1

print(soma)

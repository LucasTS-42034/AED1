n = int(input("Digite um numero \n"))
lis = range(2, n-1)
teste = int(0)
i = int(0)
tes = int(0)
while i != len(lis):
   if n % lis[i] == 0:
      teste += 1
   i = i + 1

if teste != 0:
   print("O número " + str(n) + " não é primo")
else:
   print("O número " + str(n) + " é primo")
i = int(0)
maior = int(0)
menor = int(0)
while i <= 10:
    n = int(input("Digite um numero: \n"))
    if maior < n:
        maior = n
    elif menor > n:
        menor = n
    i+=1

print("Este é o maior número: \n " + str(maior))
print("Este é o menor número: \n" + str(menor))
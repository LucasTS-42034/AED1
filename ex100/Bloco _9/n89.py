def media(lista):
    if len(lista) == 0:
        return 0 
    soma = 0
    for numero in lista:
        soma += numero
    return soma / len(lista)

n = int(input("Quantos números na lista? "))
lista = []
for i in range(n):
    lista.append(float(input(f"Digite um número: ")))
print("Média: " + str(media(lista)))
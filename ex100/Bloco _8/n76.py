lista1 = []
lista2 = []
for i in range(5):
    n = int(input("Digite um número para a primeira lista: "))
    lista1.append(n)
for i in range(5):
    n = int(input("Digite um número para a segunda lista: "))
    lista2.append(n)

nao = []
for elemento in lista1:
    if elemento not in lista2 and elemento not in nao:
        nao.append(elemento)
for elemento in lista2:
    if elemento not in lista1 and elemento not in nao:
        nao.append(elemento)

print(nao)
lista = []
for i in range(5):
    n = int(input("Digite um número: "))
    lista.append(n)

ordenada = True
for i in range(len(lista) - 1):
    if lista[i] > lista[i + 1]:
        ordenada = False
        break

if ordenada:
    print("A lista está em ordem crescente.")
else:
    print("A lista não está em ordem crescente.")
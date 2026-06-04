def busca_linear(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1

lista = []
for i in range(5):
    n = int(input("Digite um número: "))
    lista.append(n)

alvo = int(input("Digite o valor a ser buscado: "))
posicao = busca_linear(lista, alvo)

if posicao != -1:
    print("Valor encontrado:", posicao)
else:
    print("Valor não encontrado.")
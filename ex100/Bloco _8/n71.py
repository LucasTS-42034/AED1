lista = []
for i in range(5):
    n = int(input("Digite um número: \n"))
    lista.append(n)

rotacionada = [lista[-1]] + lista[:-1]

print("Lista original:", lista)
print("Lista após rotação para a direita:", rotacionada)
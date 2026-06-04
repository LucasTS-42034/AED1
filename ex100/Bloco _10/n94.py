def indice(lista):
    for i in range(len(lista)):
        print("Índice " + str(i) + ": " + lista[i])

dados = input("Digite números separados por um espaço: ").split()
indice(dados)
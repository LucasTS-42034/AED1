def indice(lista):
    for i in range(len(lista)):
        print("Índice " + str(i) + ": " + lista[i])

dados = input("Digite elementos separados por espaço: ").split()
indice(dados)
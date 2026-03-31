def maiornum(lista):
    maior = 0
    for i in lista:
        if maior < i:
            maior = i

    return(maior)

print(maiornum(9))
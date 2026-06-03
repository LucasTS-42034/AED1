def vogais(texto):
    vogais = "aeiouAEIOU"
    cont = 0
    for letra in texto:
        if letra in vogais:
            cont += 1
    return cont

frase = input("Digite uma frase: ")
print("Quantidade de vogais: " + str(vogais(frase)))
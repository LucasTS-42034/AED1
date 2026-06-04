lista = []
for i in range(5):
    n = int(input("Digite um número: "))
    lista.append(n)

frequencia = {}
for num in lista:
    if num in frequencia:
        frequencia[num] += 1
    else:
        frequencia[num] = 1

print("Frequência dos valores:")
for chave, valor in frequencia.items():
    print(str(chave) + " aparece " + str(valor) + " vezes")
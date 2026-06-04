lista = []
for i in range(5):
    n = int(input("Digite um número: "))
    lista.append(n)

distintos = list(set(lista))
distintos.sort(reverse=True)

if len(distintos) >= 2:
    print("Segundo maior:", distintos[1])
else:
    print("Não há segundo maior.")
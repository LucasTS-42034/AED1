def soma(n):
    if n == 0:
      return 0
    return n + soma(n - 1)

num = int(input("Digite um número inteiro: "))

while True:
    if num < 0:
        print("Número inválido!")
    else:
        break
    
print("Soma dos primeiros " + str(num))
print("Números naturais: " + str(soma(num)))
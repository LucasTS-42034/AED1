st = 0
soma = int(0)
i = int(0)
med = float(0)

while True:
    n = int(input("Digite um número: "))
    
    if n % 2 == 0:
        soma = soma + n
        i = i + 1
        
    st = input("Continuar? (S ou N) ")
    
    if st == "N":
        if i > 0:
            med = float(soma / i)
            print("A média é: " + str(med))
        else:
            print("Nenhum número par foi digitado.")
        break

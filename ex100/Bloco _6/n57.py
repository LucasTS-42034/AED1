i = 3
while i >= 1:
    n = input("Digite a senha: ")
    if n == "Chimichanga":
        print("Acesso liberado!")
        break
    else:
        i = i - 1
        print("Erro! " + str(i) + " tentativas restantes!")

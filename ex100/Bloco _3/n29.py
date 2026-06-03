user = input("Digite seu nome de usuário: \n")
senha = input("Digite sua senha: \n")

if user != "" and senha != "":
    print("Acesso permitido. Seja bem vindo!")
else:
    print("Erro! Pelo menos um dos campos está vazio!")

while True:
    opera = input("Digite a operacao (Digite X para sair): \n")
    if opera == "X":
        break
    resul = int(0)
    n1 = int(input("Digite o primeiro número: \n"))
    n2 = int(input("Digite o segundo número: \n"))
    
    if opera == "+":
        resul = n1 + n2
    elif opera == "*":
        resul = n1 * n2
    elif opera == "-":
        resul = n1 - n2
    elif opera == "/":
        resul = n1 / n2
    print("O resultado é " + str(resul))
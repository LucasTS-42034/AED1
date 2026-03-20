N1 = input("Digite um numero: \n")

N2 = input("Digite outro numero: \n")

print("Escolha: \n + para soma \n - para diminuicao \n * para multiplicacao \n / para divisao \n ** para exponencial \n // para divisao de piso \n % para modulo")

cha = input("Digite a multiplicação que quer escolher: \n")

if cha == "+":
    soma = int(N1) + int(N2)
    print("A soma dos numeros é: " + str(soma))
else:
    if cha == "-":
        dimi = int(N1) - int(N2)
        print("A diminuicao dos numeros é: " + str(dimi))
    else:
        if cha == "*":
            mult = int(N1) * int(N2)
            print("A multiplicacao dos numeros é: " + str(mult))
        else:
            if cha == "/":
                if N2 != "0" and N1 != "0":
                    div = int(N1) / int(N2)
                    print("A divisao dos numeros é: " + str(div))
                else:
                    if cha == "**":
                        expo = int(N1) ** int(N2)
                        print("O exponencial dos numeros é: " + str(expo))
                    else:
                        if cha == "//":
                            if N2 != "0" and N1 != "0":
                                floor = int(N1) // int(N2)
                                print("O piso dos numeros é: " + str(floor))
                            else:
                                if cha == "%":
                                    if N2 != "0" and N1 != "0":
                                        mod = int(N1) % int(N2)
                                        print("A modulo dos numeros é: " + str(mod))



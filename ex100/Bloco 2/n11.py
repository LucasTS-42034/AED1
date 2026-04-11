n1 = int(input("Digite o primeiro número: \n"))
n2 = int(input("Digite o segundo número: \n"))
opera = input("Digite uma operacao: ")
op = int()
if opera == "+":
    op = n1 + n2
    print(op)
    
if opera == "*":
    op = n1 * n2
    print(op)

if opera == "-":
    op = n1 - n2
    print(op)

if opera == "/":
    op = n1 / n2
    print(op)

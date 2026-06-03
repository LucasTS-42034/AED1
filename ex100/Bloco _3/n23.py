n1 = int(input("Digite 0 ou 1 novamente: "))
n2 = int(input("Digite 0 ou 1 novamente: "))

boo1 = bool(n1)
boo2 = bool(n2)

print(str(boo1) + " and " + str(boo2) + " = " + str(boo1 and boo2))
print(str(boo1) + " or " + str(boo2) + " = " + str(boo1 or boo2))
print("not " + str(boo1) + " = " + str(not boo1))
print("not " + str(boo2) + " = " + str(not boo2))
lada = float(input("Digite o primeiro lado: "))
ladb = float(input("Digite o segundo lado: "))
ladc = float(input("Digite o terceiro lado: "))

if (lada + ladb > ladc) and (lada + ladc > ladb) and (ladb + ladc > lada):
    print("Os lados formam um triângulo ")
    
    if lada == ladb == ladc:
        print("Equilátero.")
    elif lada != ladb and ladb != ladc and lada != ladc:
        print("Escaleno.")
    else:
        print("Isósceles.")
else:
    print("Os lados não formam um triângulo.")

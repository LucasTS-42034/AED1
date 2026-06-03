idade = int(input("Digite sua idade: \n"))

if idade < 0:
    print("Inválido!")
elif 0 <= idade < 18:
    print("Você é menor de idade.")
else:
    print("Você é maior de idade.")
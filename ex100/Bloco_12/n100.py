class ContaBancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficient, seu pobre ferrado.")

    def exibir_saldo(self):
        print("Saldo atual: R$ " + str(self.saldo))

saldo_inicial = float(input("Digite o saldo inicial: "))
conta = ContaBancaria(saldo_inicial)

while True:
    print("\n1 - Depositar")
    print("2 - Sacar")
    print("3 - Exibir saldo")
    print("0 - Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 0:
        print("Encerrando...")
        break
    elif opcao == 1:
        valor = float(input("Valor para depósito: "))
        conta.depositar(valor)
    elif opcao == 2:
        valor = float(input("Valor para saque: "))
        conta.sacar(valor)
    elif opcao == 3:
        conta.exibir_saldo()
    else:
        print("Opção inválida!")
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir(self):
        print("Nome: " + self.nome + " - Idade: " + str(self.idade))

nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
p = Pessoa(nome, idade)
p.exibir()
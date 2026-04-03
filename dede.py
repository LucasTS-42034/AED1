


def addLista(value: int = None, lista: list = []) -> list:
    if lista is None:
        lista = []
    
    lista.append(value)
    return lista


def cabecalho(nome: str = "Aluno") -> None:
    print("Meu nome é: ", nome)

# print(incremental(1.5, value))
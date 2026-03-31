nots = [
    [8.0, 7.0, 9.0],  
    [5.5, 6.0, 4.5],  
    [10.0, 9.5, 8.0]  
]

for linha in nots:
    med = sum(linha) / len(linha)
    print("Média do aluno: " + str(med))

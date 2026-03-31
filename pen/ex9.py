nots = [
    [8.0, 7.0, 9.0],  
    [5.5, 6.0, 4.5],  
    [10.0, 9.5, 8.0]  
]
rep = int(0)
apr = int(0)
for linha in nots:
    for nota in linha:
        if nota >= 7:
            apr+= 1
        else:
            rep+= 1


print("A quantidade de aprovados é de " + str(apr))
print("A quantidade de reprovados é de: " + str(rep))
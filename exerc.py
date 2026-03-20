lis = [3,7,10,15,22,30]
print(lis)

i = 0
while i != len(lis):
    if lis[i] > 10:
        print(lis[i])
    i = i + 1

valores = [5, 8, 12, 20]
print(valores)

print(sum(valores))


dados = [1,2,3,4,5,6,7]

j = 0
pares = int()
while j != len(dados):
    if dados[j] % 2 == 0:
        pares = pares + 1
    j = j + 1

print(pares)


dads = [1,2,2,3,3,3,4,5]
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
new = 0
newcont = 0
z = 0
while z != len(dads):
    if dads[z] == 1:
        cont1 += 1
    
    if dads[z] == 2:
        cont2 += 1
    
    if dads[z] == 3:
        cont3 += 1
    
    if dads[z] == 4:
        cont4 += 1
    
    if dads[z] != 1 & dads[z] != 2 & dads[z] != 3 & dads[z] != 4:
        new = dads[z]
        newcont += 1
    z += 1


thisdict = {
  1: cont1, 
  2: cont2, 
  3: cont3, 
  4: cont4,
  new: newcont
}


print(thisdict)



valore = [10,25,7,99,3]

c = 0
maior = 0
while c != len(valore):
    if valore[c] > maior:
        maior = valore[c]
    c = c + 1

print(maior)
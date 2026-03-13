list1 = [7.5, 8.0, 6.5, 9.0]

print(list1)
print(list1.append(5.0))
print(list1)
print(list1.pop(2))
print(list1)
print(list1.sort())
print(list1)
print(list1.reverse())
print(list1)

som = sum(list1)


media = int(som / 3)

print(media)

if media > 7:
    print("Parabens, foi aprovado!")
if 7 > media > 4:
    print("Você está em exame.")
if 4 > media:
    print("Você está reprovado.")

tup = tuple(list1)
t1 = (1, 2)
t2 = (3, 4)
tp = t1 + t2
print(tup)
print(tp)

list2 = (1,3,3,6,5)
set1 = set(list2)
set1.add(2)
set1.remove(6)
print(set1)
s1 = {1,2,3}
s2 = {3,4,5}
set3 = list(s1) + list(s2)
print(set(set3))

tup = (22, 25, 556664234, 21)

n = max(tup)

print("A temperatura mais quente é: " + str(n))

if n > 26:
    print("O clima esta quente, viu?")


set4 = {2,4,6,8}
x = input("Digite um numero: \n")

if(x )
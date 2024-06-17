import random
alunos = int(input('Quantos alunos são? '))
l = []
l1 = []

for x in range(1, alunos+1): l.append(x)

i1 = alunos // 2
i2 = alunos - i1

for i in range(0, i1):
    elem = random.choice(l)
    l1.append(elem)
    l.remove(elem)

l1.sort()
print(l1)

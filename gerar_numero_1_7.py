import random

e1 = 4
e2 = 5
i = 4
s1 = dict()
s2 = dict()

while True:
    x = random.randint(1, e1)
    y = random.randint(1, e2)
    s1[x] = x
    s2[y] = y
    if(len(s1) == e1 and len(s2) == e2):
        break

print(s1)
print(s2)






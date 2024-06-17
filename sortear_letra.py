import random

letras = []

for i in range(65, 91):
    letras.append(chr(i))

letra_sorteada = random.choice(letras)
print(letra_sorteada)


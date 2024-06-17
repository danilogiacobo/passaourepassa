import random

perguntas = []
num_perguntas = 40

for i in range(1, num_perguntas + 1):
    perguntas.append(i)

pergunta_sorteada = random.choice(perguntas)
print('Pergunta sorteada:', pergunta_sorteada)





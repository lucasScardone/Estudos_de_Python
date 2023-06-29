import random
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5, tente adivinhar...')
print('-=-' * 20)
random = random.randint(0, 5)
num = int(input('Em que número eu pensei? \n'))
if num == random:
    print(f'Parabéns, você acertou! O número realmente era {random}.')
else:
    print(f'Que pena, você errou... O numero era {random}. Você pelo menos chutou entre 0 e 5, certo?')

from random import randint
from time import sleep
print(f'''
_________________________________________________
              Jogo da Mega Sena
-------------------------------------------------
''')
times = int(input('Quantas vezes você quer jogar? '))
preset = []
for t in range(times):
    numbers = []
    for n in range(6):
        number = randint(1, 60)
        while number in numbers:
            number = randint(1, 60)
        numbers.append(number)
    preset.append(numbers)
    numbers.sort()
    sleep(1)
    print(f' {t+1}º jogo: {preset[t]}')
print(f'''
            Boa sorte!
   Dizem que a loteria é o imposto para quem 
      não entende de estatística...
''')

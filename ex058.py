from time import sleep
import random
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10...')
sleep(1)
print('Pronto! Tente adivinhar...')
print('-=-' * 20)
random = random.randint(0, 10)
num = int(input('Em que número eu pensei? \n'))
contador = 1
while num != random:
    contador += 1
    sleep(0.5)
    print(f'\nNão dessa vez... O número que eu pensei não foi {num}.')
    if num < random:
        print(' Dica: Você digitou um número menor.')
    elif num > random:
        print(' Dica: Você digitou um número maior.')
    num = int(input('Tente de novo: '))
if num == random:
    print(f'Meus parabéns! O número realmente era {random}. Você acertou na sua {contador}ª tentativa.')
else:
    print(f'Pudding')
if contador == 1:
    print('Nem teve graça, você acertou de primeira.')
elif 2 <= contador <= 4:
    print('Você teve um pouco de sorte, ou foi inteligente.')
elif 5 <= contador <= 11:
    print('Você teve um pouco de azar, ou só é burro mesmo. Vá estudar análise binária.')
elif contador > 11:
    print('Você é muito ruim ou tem problemas de memória. Como você demorou tanto?')

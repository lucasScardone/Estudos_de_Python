from random import randint
from time import sleep

print('Vamos jogar par ou impar!')
jogador = cpu = escolha = contador = resultado = 0

while True:
    cpu = randint(1, 10)
    escolha = str(input('Digite sua escolha, par ou impar? ')).strip().upper()[0]
    jogador = int(input('Jogue o seu número! '))
    resultado = cpu + jogador
    sleep(1)
    if (escolha == 'P' and resultado % 2 == 0) or (escolha == 'I' and resultado % 2 == 1):
        contador += 1
        print(f'Parabéns! Você venceu essa rodada! '
              f'O computador jogou {cpu} e você jogou {jogador}, o resultado é {resultado}, ou seja: ', end='')
        if escolha == 'P':
            print('par.')
        else:
            print('impar.')
    else:
        print(f'Você perdeu... O computador jogou {cpu} e você jogou {jogador}, o resultado é {resultado}, ou seja: ', end='')
        if escolha == 'P':
            print('impar.')
        else:
            print('par')
        break
if escolha not in 'PI':
    print('\nObs: escolha par ou ímpar direito, você perdeu automaticamente se não soube escolher.')
print(f'\nSua sequência de vitórias foi de {contador}.')

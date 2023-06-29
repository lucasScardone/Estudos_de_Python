import random
from time import sleep
print('''
Vamos jogar jankenpo!
[1] Pedra
[2] Papel
[3] Tesoura
''')

cpu = random.randint(1, 3)
arma = int(input('Escolha sua arma:'))
print('Jan...')
sleep(1)
print('ken...')
sleep(1)
print('po!')
sleep(1)

if cpu == 1:
    print('O computador jogou pedra!')
elif cpu == 2:
    print('O computador jogou papel!')
elif cpu == 3:
    print('O computador jogou tesoura!')
else:
    print('O computador ficou maluco! Fuja desse programa!')

if arma < 1 or arma > 3:
    print('Por favor escolha uma opção válida...')
else:
    if arma == cpu:  # Condição de empate
        print('Você empatou com o computador, tente de novo.')
    elif (arma == 1 and cpu == 3) or (arma == 2 and cpu == 1) or (arma == 3 and cpu == 2):  # Condição de vitória
        print('Meus parabéns! você ganhou do computador!')
    elif (arma == 1 and cpu == 2) or (arma == 2 and cpu == 3) or (arma == 3 and cpu == 1):  # Condição de derrota
        print('Lamento, você perdeu.')
    else:
        print('Muitíssimos parabéns, eu não sei como você chegou aqui.')

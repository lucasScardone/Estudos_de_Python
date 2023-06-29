from random import randint
from operator import itemgetter
from time import sleep
throws = dict(p1=randint(1, 20),
              p2=randint(1, 20),
              p3=randint(1, 20),
              p4=randint(1, 20))
for k, v in throws.items():
    sleep(1)
    print(f'O jogador {k} tirou {v} no dado.')
sleep(1)
print('-=' * 20)
sleep(1)
print('    =-= Ranking dos jogadores =-=    ')
sleep(1)
ranking = sorted(throws.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    sleep(1)
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')

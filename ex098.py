from time import sleep


def count(begin, end, pace):
    while ((begin - end) > 0 and pace >= 0) or ((begin - end) < 0 and pace <= 0):
        print('Sua progressão gera um loop infinito, insira os dados novamente.')
        begin = int(input('Qual será o termo inicial? '))
        end = int(input('E o final? '))
        pace = int(input('Qual será o ritmo da progressão?'))
    for c in range(begin, end+1, pace):
        sleep(0.5)
        print(f'{c}')
    print('Fim!')


print('Contando de 1 a 10 com funções...')
count(1, 10, 1)
print('Contando de 10 a 0 voltando de 2 em 2...')
count(10, -2, -2)
print('Personalize sua contagem!')
count(int(input('Qual será o termo inicial? ')),
      int(input('E o final? ')),
      int(input('Qual será o ritmo da progressão?')))

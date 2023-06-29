num_ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = 0
continuar = 'S'
while continuar == 'S':
    num = int(input('Digite um número inteiro entre 0 e 20: '))
    while num < 0 or num > 20:
        num = int(input('Por favor, digite um número inteiro entre 0 e 20: '))
    print(f'Você digitou o número {num_ext[num]}.')
    continuar = str(input('Deseja testar mais um número inteiro entre 0 e 20? [S/N]  ')).strip().upper()[0]
    if continuar == 'S':
        continue
    elif continuar == 'N':
        print('Adeus')
    else:
        print('Pudding.')

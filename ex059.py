from time import sleep
num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
mensagem = '''O que deseja fazer com esses números?
[1] Somar.
[2] Multiplicar.
[3] Descobrir o maior.
[4] Digitar outros números.
[5] Nada, só quero ir embora.
'''
operador = 0
while operador != 5:
    sleep(1)
    print(f'{mensagem}')
    operador = int(input(''))
    if operador == 1:
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operador == 2:
        print(f'{num1} x {num2} = {num1 * num2}')
    elif operador == 3:
        if num1 > num2:
            print(f'{num1} é maior que {num2}.')
        elif num2 > num1:
            print(f'{num2} é maior que {num1}')
        else:
            print(f'São o mesmo número!')
    elif operador == 4:
        num1 = int(input('Digite um número inteiro: '))
        num2 = int(input('Digite outro número inteiro: '))
    else:
        print('Adeus.')

num = int(input('Digite um número inteiro e positivo para calcularmos o fatorial: '))
fatorial = num
if num < 0:
    print('Não calculamos fatorial de número negativo.')
elif num == 0:
    print('0! = 1   (Não me pergunte por que).')
else:
    while num != 1:
        print(f'{num} x ', end='')
        fatorial *= num - 1
        num -= 1
    print(f'1 = {fatorial}')

num = int(input('Digite um número positivo para vermos se é primo: '))
if num < 0:
    print('Para com isso e digita direito')
elif num == 0 or num == 1:
    print('Os números 0 e 1 não são primos, não me pergunte por que...')
    exit()
else:
    s = 0
    for c in range(2, num):
        if num % c == 0:
            print(f'{c}', end='  ')
            s += 1
    if s != 0:
        print(f'\nO número não é primo, há {s} divisores para esse número (tirando 1 e ele mesmo).'
              f'\nVocê pode ver o número de divisores acima.')
    else:
        print(f'O número {num} é primo.')

print('\nVamos montar uma progressão aritmética!\n')
razao = int(input('Digite uma razão para a progressão: '))
inicial = int(input('Digite o valor inicial da progressão: '))

print('Os 10 primeiros termos são: ')
for c in range(0, 10):
    print(f'{inicial}', end='-> ')
    inicial += razao
print('...')

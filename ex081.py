numbers = []
while True:
    numbers.append(int(input('Adicione um valor à lista: ')))
    option = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if option == 'S':
        continue
    elif option == 'N':
        break
    else:
        option = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
if 5 in numbers:
    pos_num5 = numbers.index(5)
    print(f'O valor 5 está na lista e foi o {pos_num5+1}º valor digitado.')
else:
    print(f'O valor 5 não foi digitado.')
numbers.sort(), numbers.reverse()
print(f'Você digitou {len(numbers)} valores.')
print(f'Os valores em ordem decrescente são: {numbers}')

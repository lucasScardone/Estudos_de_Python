def comparator(*n):
    print(f'Os números digitados foram {n}.')
    numbers.sort()
    print(f'O menor número digitado foi {numbers[0]} e o maior número digitado foi {numbers[-1]}.')


numbers = [int(input('Digite um número inteiro para ser comparado: '))]
while True:
    numbers.append(int(input('Digite mais um número inteiro para ser comparado: ')))
    option = str(input('Mais algum número? [S/N] ')).strip().upper()[0]
    while option not in 'SN':
        option = str(input('Mais algum número? [S/N] ')).strip().upper()[0]
    if option == 'S':
        continue
    elif option == 'N':
        break
comparator(numbers)

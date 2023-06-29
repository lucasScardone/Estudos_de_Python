from random import randint
numbers = []


def random_numbers(*num):
    print('Sorteando 5 valores: ', end='')
    for value in range(*num):
        v = randint(0, 9)
        print(f'{v}', end=' ')
        numbers.append(v)


def sum_pairs(num):
    num = 0
    print('\nOs valores pares são: ', end='')
    for v in numbers:
        if v % 2 == 0:
            print(f'{v}', end=' ')
            num += v
    print(f'\nE a soma dos valores pares é: {num}')


random_numbers(int(input('Quantos números você quer gerar? ')))
sum_pairs(numbers)

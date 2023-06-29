matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sum_even = sum_column = sum_odd = 0
for line in range(3):
    for column in range(3):
        matrix[line][column] = int(input(f'Digite um valor para a posição [{line}], [{column}]: '))
for line in range(3):
    print('\n')
    for column in range(3):
        print(f'[{matrix[line][column]:^5}]', end=' ')
        if column == 2:
            sum_column += matrix[line][column]
        if matrix[line][column] % 2 == 0:
            sum_even += matrix[line][column]
        else:
            sum_odd += matrix[line][column]
print(f'\nA soma da terceira coluna é de {sum_column}.')
print(f'A soma dos valores pares é de {sum_even}.')
print(f'A soma dos valores ímpares é de {sum_odd}')

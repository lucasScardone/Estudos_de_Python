numbers = []
even_numbers = []
odd_numbers = []
while True:
    number = int(input('Adicione um valor à lista: '))
    numbers.append(number)
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)
    option = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while option not in 'NS':
        option = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if option == 'S':
        continue
    elif option == 'N':
        break
numbers.sort()
even_numbers.sort()
odd_numbers.sort()
print(f'A lista completa é: {numbers}')
print(f'A lista de pares é: {even_numbers}')
print(f'A lista de ímpares é: {odd_numbers}')

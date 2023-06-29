numbers = []
for c in range(6):
    number = int(input('Digite um número inteiro: '))
    if c == 0:
        numbers.append(number)
        print('Valor adicionado à lista.')
    if c > 0:
        if number < min(numbers):
            numbers.insert(0, number)
            print('Valor adicionado ao início da lista.')
        elif number > max(numbers):
            numbers.append(number)
            print('Valor adicionado ao final da lista.')
        else:
            pos = 0
            while pos < len(numbers):
                if number <= numbers[pos]:
                    numbers.insert(pos, number)
                    print(f'Valor adicionado na posição {pos} da lista.')
                    break
                pos += 1
print(f'Os valores digitados em ordem crescente são: {numbers}')

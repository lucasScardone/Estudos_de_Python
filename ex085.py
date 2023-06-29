values = [[], []]
for c in range(1, 8):
    value = int(input(f'Digite o {c}º número inteiro: '))
    if value % 2 == 0:
        values[0].append(value)
    else:
        values[1].append(value)
values[0].sort(), values[1].sort()
print(f'Os valores digitados foram: {values}')
print(f'Os valores pares em ordem crescente foram: {values[0]}')
print(f'Os valores ímpares em ordem crescente foram: {values[1]}')

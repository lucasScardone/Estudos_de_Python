matrix = [[], [], []]
for c in range(1, 10):
    if 1 <= c <= 3:
        value = int(input(f'Digite um valor inteiro na posição[{1}, {c}] para gerar a matriz: '))
        matrix[0].append(value)
    elif 4 <= c <= 6:
        value = int(input(f'Digite um valor inteiro na posição[{2}, {c-3}] para gerar a matriz: '))
        matrix[1].append(value)
    elif 7 <= c <= 9:
        value = int(input(f'Digite um valor inteiro na posição[{3}, {c-6}] para gerar a matriz: '))
        matrix[2].append(value)
    else:
        print('Pudding.')
print(f'''A matriz gerada é: 
{matrix[0]}
{matrix[1]}
{matrix[2]}
''')
#  A solução usa ifs desnecessários e usa números mágicos. É possível fazer mais limpo em 10 linhas.

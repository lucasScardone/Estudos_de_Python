from random import randint
valores_list = []
for c in range(5):
    valores_list.append(randint(0, 9))
valores = tuple(valores_list)
print(f'Os valores sorteados foram {valores}')
print(f'O maior valor sorteado foi {max(valores)}')
print(f'O menor valor sorteado foi {min(valores)}')

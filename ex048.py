print('Vamos fazer somatórias!')
s = 0
ini = int(input('Digite de onde vamos começar a contar: '))
lim = int(input('Digite até onde vamos contar: '))
mult = int(input('Digite os múltiplos que deseja somar: '))
for c in range(ini, lim + 1, mult):
    s += c
print(f'A soma dos {lim // mult} valores é igual a {s}.')

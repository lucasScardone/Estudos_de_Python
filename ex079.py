values = []
while True:
    value = int(input('Digite um número inteiro para adicionar à lista: '))
    if value in values:
        print(f'O valor {value} já foi adicionado à lista. Não aceitamos valores duplicados.')
    else:
        values.append(value)
        print(f'Valor adicionado com sucesso')
    option = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if option == 'S':
        continue
    elif option == 'N':
        break
    else:
        option = str(input('Deseja continuar? Digite S para "sim" ou N para "não" [S/N]'))
values.sort()
print(f'Os valores digitados foram {values}.')

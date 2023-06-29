print('''
---------------------------------------------
Banco Meh
---------------------------------------------
''')
total = contador = 0
while True:
    valor = int(input('\nQue valor você quer sacar? '))
    if valor <= 1:
        continue
    total += valor
    if valor > 1000:
        print(f'\nO valor de R${valor} excede o limite de R$1000 por saque.')
        total -= valor
        continue
    if total > 1500:
        print(f'\nO valor de R${total} ultrapassa o limite diário de saque de R$1500.')
        total -= valor
        continue
    notas_100 = valor // 100
    resto = valor % 100
    notas_50 = resto // 50
    resto %= 50
    notas_20 = resto // 20
    resto %= 20
    notas_10 = resto // 10
    resto %= 10
    notas_5 = resto // 5
    resto %= 5
    notas_2 = resto // 2
    resto %= 2
    print(f'''
O saque possui um total de:
{notas_100} cédulas de R$100.
{notas_50} cédulas de R$50.
{notas_20} cédulas de R$20.
{notas_10} cédulas de R$10.
{notas_5} cédulas de R$5.
{notas_2} cédulas de R$2.
''')
    contador += 1
    if total == 1500:
        break
    if contador == 3:
        print(f'Você atingiu o limite de 3 saques diários, sacando um total de R${total}.')
        break
    outro_saque = str(input('\nDeseja fazer mais um saque? [S/N]')).strip().upper()[0]
    if outro_saque not in 'SN':
        outro_saque = str(input('Deseja fazer mais um saque? [S/N]')).strip().upper()[0]
    elif outro_saque == 'S':
        print('\n')
    elif outro_saque == 'N':
        break
print('Obrigado por usar os serviços Meh.')

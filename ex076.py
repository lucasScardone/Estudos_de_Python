products = []
prices = []
option = ''

while option != 'N':
    product = str(input('\nAdicione o produto que o cliente comprou: '))
    products.append(product)
    price = float(input('Quanto custou esse produto?  R$'))
    price = round(price, 2)
    prices.append(price)
    option = str(input('Deseja adicionar mais um produto? [S/N]')).strip().upper()[0]
    while option not in 'SN':
        option = str(input('Deseja adicionar mais um produto? Digite uma opção válida. [S/N]')).strip().upper()[0]
    if option == 'N':
        break
    elif option == 'S':
        print('\n')
        continue

products_tuple = tuple(products)
prices_tuple = tuple(prices)
print('''
__________________________________________________
                Listagem de preços
--------------------------------------------------
''')
for c in range(len(products_tuple)):
    print(f'{products_tuple[c]:.<15} R${prices_tuple[c]:>10}')
print('--------------------------------------------------')

print('''
---------------------------------------------
Lojas Meh gazine Luisa
---------------------------------------------
''')
lista_nome = []
lista_preco = []
numero_produtos = total = caro = nome_produto_mais_caro = nome_produto_mais_barato = 0

while True:
    nome = str(input('Nome do produto: ')).strip()
    lista_nome.append(nome)
    preco = float(input('Preço do produto: R$'))
    lista_preco.append(round(preco, 2))
    total += preco
    if preco > 1000:
        caro += 1
    lista_preco.sort()
    if preco >= lista_preco[-1]:
        nome_produto_mais_caro = nome
    if preco <= lista_preco[0]:
        nome_produto_mais_barato = nome
    numero_produtos += 1
    opcao = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    elif opcao == 'S':
        print('\n')
    elif opcao == 'N':
        print('\n')
        break

mais_barato = lista_preco[0]
mais_caro = lista_preco[-1]

print(f'''
O total da compra foi de R${total:.2f}.
Temos {caro} produto(s) custando mais de R$1000.  
O produto mais barato foi {nome_produto_mais_barato}, que custou R${mais_barato:.2f}.
E o produto mais caro foi {nome_produto_mais_caro}, que custou R${mais_caro:.2f}.
''')

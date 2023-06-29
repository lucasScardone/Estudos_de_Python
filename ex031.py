dist = float(input('Qual é a distância da viagem?\n Km:'))
dif = dist - 200
preco = dist * 0.5
preco_dif = dif * 0.45
if 0 <= dist <= 200:
    print(f'\nO preço da viagem é de R${preco:.2f}.')
elif dist > 200:
    print(f'\nO preço da viagem é de R${(preco + preco_dif):.2f}')
else:
    print(f'Você colocou um número negativo né?')

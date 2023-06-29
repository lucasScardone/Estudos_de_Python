print('=' * 10, 'Lojas meh', '=' * 10)
valor = float(input('Qual o valor da compra?\n R$'))
print('''
Formas de pagamento:
[1] À vista no dinheiro ou cheque.
[2] À vista no cartão.
[3] 2x no cartão.
[4] 3x no cartão.
''')
forma = int(input('Escolha a forma de pagamento: '))

if forma == 1:
    print(f'O produto no valor de R${valor} pago à vista em dinheiro ou cheque terá 10% de desconto, '
          f'passando a custar R${valor * 0.9:.2f}.')
elif forma == 2:
    print(f'O produto no valor de R${valor} pago à vista no cartão terá 5% de desconto,'
          f' passando a custar R${valor * 0.95:.2f}.')
elif forma == 3:
    print(f'O produto parcelado em duas vezes no cartão não possui desconto nem juros, '
          f'custando R${valor:.2f} em 2 parcelas de R${valor / 2:.2f}.')
elif forma == 4:
    print(f'O produto parcelado em 3 vezes possui juros de 10%, '
          f'passando a custar R${valor * 1.1:.2f} em 3 parcelas de R${(valor * 1.1) / 3:.2f}')
else:
    print('Por favor digite uma forma válida de pagamento')

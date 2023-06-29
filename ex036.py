valor = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
financiamento = int(input('Quantos anos de financiamento? '))
entrada = float(input('Deseja dar uma entrada de qual valor? R$'))
valor_total = valor - entrada
prestacao = valor_total / (financiamento * 12)

if entrada >= valor:
    print('Sua entrada é muito alta, você pode pagar a vista.')
elif prestacao <= salario * 0.3:
    print(f'Seu financiamento foi aprovado! A prestação será de R${prestacao:.2f}.')
else:
    print('Me desculpe, seu financiamento foi negado.')

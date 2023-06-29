from datetime import date
ano = int(input('Que ano você quer analisar? Coloque 0 para analisar o ano atual: \n'))

if ano == 0:
    ano = date.today().year
if (ano % 400) == 0:
    print(f'O ano de {ano} é bissexto.')
elif (ano % 100) == 0:
    print(f'O ano de {ano} não é bissexto.')
elif (ano % 4) == 0:
    print(f'O ano de {ano} é bissexto.')
else:
    print(f'O ano de {ano} não é bissexto.')

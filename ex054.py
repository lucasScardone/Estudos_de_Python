from datetime import date
maior = 0
menor = 0
for c in range(1, 8):
    data = int(input(f'Digite o ano de nascimento da pessoa número {c}: '))
    atual = date.today().year
    idade = atual - data
    if idade >= 18:
        print(f'A pessoa número {c} é maior de idade.')
        maior += 1
    else:
        print(f'A pessoa número {c} é menor de idade.')
        menor += 1
print(f'\nHá {menor} pessoa(s) menor(es) de idade e {maior} pessoa(s) maiores de idade.')

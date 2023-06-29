from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano

if idade > 18:
    print(f'Já passou do seu tempo de se alistar! Sua data de alistamento era {ano + 18}.')
elif idade < 18:
    print(f'Ainda faltam {18 - idade} anos para você se alistar.')
else:
    print('Lamento meu jovem, sua hora chegou...')

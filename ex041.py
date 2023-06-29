from datetime import date
nascimento = int(input('Ano de nascimento do atleta: '))
atual = date.today().year
idade = atual - nascimento
print('A categoria do atleta é:')

if 0 <= idade < 9:
    print('Mirim')
    print(f'O atleta tem {idade} anos.')
elif 9 <= idade < 14:
    print('Infantil')
    print(f'O atleta tem {idade} anos.')
elif 14 <= idade < 19:
    print('Júnior')
    print(f'O atleta tem {idade} anos.')
elif 19 <= idade <= 25:
    print('Sênior')
    print(f'O atleta tem {idade} anos.')
elif idade > 25:
    print('Master')
    print(f'O atleta tem {idade} anos.')
else:
    print('Essa idade é inválida.')

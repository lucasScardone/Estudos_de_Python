def vote(birth):
    age = year - birth
    if age < 0 or age > 122:
        print('Este ano de nascimento é inválido.')
        exit()
    if age < 16:
        print(f'Sua idade é {age} anos. Você ainda não pode votar.')
    elif age == 16 or age == 17:
        print(f'Sua idade é {age} anos. O voto é opcional.')
    elif 18 <= age <= 65:
        print(f'Sua idade é {age} anos. O voto é obrigatório.')
    elif age > 65:
        print(f'Sua idade é {age} anos. O voto é opcional.')
    else:
        print('Pudding')


year = 2022
vote(int(input('Digite o seu ano de nascimento: ')))

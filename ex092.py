worker = dict(name='', year=0, ctps=0, hired=0, salary=0.0)
while True:
    worker['name'] = str(input('Nome: '))
    worker['year'] = int(input('Ano de nascimento: '))
    idade = 2022 - worker['year']
    if idade < 16:
        print('Somos contra o trabalho infantil.')
        continue
    elif 16 <= idade < 18:
        print('Infelizmente não trabalhamos com menores aprendizes.')
        continue
    elif idade > 100:
        print('Você é velho demais para trabalhar')
        continue
    worker['ctps'] = int(input('Nº da carteira de trabalho (11 dígitos) (0 se não tem): '))
    if worker['ctps'] == 0:
        print(f'{worker["name"]} tem {idade} anos e não possui carteira de trabalho.')
        continue
    while worker['ctps'] < 10000000000 or worker['ctps'] > 99999999999:
        print('Número inválido, por favor digite o número de 11 dígitos corretamente.')
        worker['ctps'] = int(input('Nº da carteira de trabalho (11 dígitos) (0 se não tem): '))
    if 10000000000 <= worker['ctps'] <= 99999999999:
        worker['hired'] = int(input('Ano de contratação: '))
        worked = 2022 - worker['hired']
        if (worked - idade) < 18:
            print('Somos contra o trabalho infantil.')
            continue
        retired = idade + (35 - worked)
        worker['salary'] = float(input('Salário: '))
        print(f'''
        {worker["name"]} tem {idade} anos.
        Possui a carteira de trabalho de número: {worker['ctps']}
        Seu salário é de {worker['salary']:.2f}.
        Se aposentará aos {retired} anos.
        ''')
    option = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while option not in 'SN':
        option = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if option == 'S':
        continue
    elif option == 'N':
        break

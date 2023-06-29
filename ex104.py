def check_int_input(n):
    if n.isnumeric():
        n = int(n)
    else:
        while not n.isnumeric():
            n = input('Por favor digite um número inteiro válido (eu sei que você testou pudding) ')
    print(f'Seu número {n} foi inserido com sucesso.')


check_int_input(input('Por favor, digite um número inteiro: '))

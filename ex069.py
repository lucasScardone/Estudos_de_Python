lista_idade = []
lista_sexo = []
contador_universal = contador_homens = contador_mulheres = escolha = maioridade = mulher_20 = 0

while True:
    contador_universal += 1
    idade = int(input(f'Digite a idade da {contador_universal}ª pessoa: '))
    lista_idade.append(idade)
    if idade >= 18:
        maioridade += 1
    sexo = str(input(f'Digite o sexo da pessoa: [M/F] ')).strip().upper()[0]
    if sexo not in 'MF':
        sexo = str(input(f'Por favor, digite o sexo da pessoa corretamente: [M/F] ')).strip().upper()[0]
    else:
        lista_sexo.append(sexo)
    if sexo == 'M':
        contador_homens += 1
    elif sexo == 'F':
        contador_mulheres += 1
    if idade > 20 and sexo == 'F':
        mulher_20 += 1
    escolha = input('''Para adicionar mais algum usuário, digite qualquer tecla.
    Para sair, digite [S]''').strip().upper()[0]
    if escolha == 'S':
        break

print(f'''
{maioridade} pessoas são maior de idade.
{contador_homens} homem(ns) e {contador_mulheres} mulher(es) foram cadastrados(as).
{mulher_20} mulher(es) têm mais de 20 anos.
A ordem de cadastro das idades foi {lista_idade}.
A ordem de cadastro dos sexos foi {lista_sexo}
''')

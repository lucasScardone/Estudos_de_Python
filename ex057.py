sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Entrada inválida. Informe seu sexo: [M/F] ')).strip().upper()[0]
if sexo == 'M':
    print('Sexo masculino registrado com sucesso.')
elif sexo == 'F':
    print('Sexo feminino registrado com sucesso.')
else:
    print('Não sei como você chegou aqui, talvez esse sexo seja pudding.')

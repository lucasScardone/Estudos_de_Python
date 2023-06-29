nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = round((nota1 + nota2) / 2, 2)

if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10:
    print('Você inseriu alguma nota inválida')
else:
    if 6 <= media <= 10:
        print(f'A média do aluno é {media}. Aprovado!')
    elif 4 <= media < 6:
        print(f'A média do aluno é {media}. Recuperação...')
    elif 0 <= media < 4:
        print(f'A média do aluno é {media}. Reprovado!')
    else:
        print('Eu não sei como você chegou até aqui.')

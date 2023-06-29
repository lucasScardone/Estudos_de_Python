import random
aluno1 = str(input('Digite o nome do primeiro aluno: \n'))
aluno2 = str(input('Digite o nome do segundo aluno: \n'))
aluno3 = str(input('Digite o nome do terceiro aluno: \n'))
aluno4 = str(input('Digite o nome do quarto aluno: \n'))
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print(f'A ordem de apresentação será: {lista}.')

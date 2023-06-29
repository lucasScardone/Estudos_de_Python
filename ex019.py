import random
nome1 = str(input('Digite o nome do primeiro aluno: \n'))
nome2 = str(input('Digite o nome do segundo aluno: \n'))
nome3 = str(input('Digite o nome do terceiro aluno: \n'))
nome4 = str(input('Digite o nome do quarto aluno: \n'))
lista = [nome1, nome2, nome3, nome4]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}.')

students = {'name': str(input("Nome: ")),
            'g1': float(input("Primeira nota: ")),
            'g2': float(input("Segunda nota: "))}
while students['g1'] < 0 or students['g1'] > 10:
    students['g1'] = float(input('A primeira nota foi inválida, insira novamente: '))
while students['g2'] < 0 or students['g2'] > 10:
    students['g2'] = float(input('A segunda nota foi inválida, insira novamente: '))
media = (students['g1']+students['g2']) / 2
print(f'O nome é {students["name"]}. \nA média é igual a {media:.1f}.')
if 0 <= media < 4:
    print('O aluno está reprovado.')
elif 4 <= media < 6:
    print('O aluno está de recuperação.')
elif 6 <= media <= 10:
    print('O aluno está aprovado!')
else:
    print('Pudding')

users = {'name': [], 'age': [], 'gender': []}
count = total_age = 0
women = []
old_people = []
while True:
    users['name'].append(str(input('Nome do usuário: ')))
    users['age'].append(int(input('Idade do usuário: ')))
    while users['age'][count] < 0 or users['age'][count] > 122:
        users['age'][count] = int(input('Idade do usuário: (Eu não acredito na última idade digitada) '))
    total_age += users['age'][count]
    users['gender'].append((str(input('Sexo do usuário [H/M]: ')).strip().upper()[0]))
    while users['gender'][count] not in 'HM':
        users['gender'][count] = str(input('Sexo do usuário [H/M]: ')).strip().upper()[0]
    if users['gender'][count] == 'M':
        women.append(users['name'][count])
    count += 1
    option = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while option not in 'SN':
        option = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if option == 'S':
        continue
    elif option == 'N':
        break
avg_age = total_age / count
for user in range(count):
    if users['age'][user] > avg_age:
        old_people.append(users['name'][user])
print(f'''
Um total de {count} pessoas foram cadastradas.
A média de idade dos usuários é de: {avg_age:.1f} anos.
As mulheres cadastradas foram: {women}.
A pessoas com idade acima da média são: {old_people}
''')

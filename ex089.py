report_card = []
while True:
    student = []
    name = str(input('Digite o nome do aluno: '))
    student.append(name)
    grade1 = float(input('Digite a primeira nota: '))
    while grade1 < 0 or grade1 > 10:
        grade1 = float(input('Nota inválida! Digite a primeira nota: '))
    student.append(grade1)
    grade2 = float(input('Digite a segunda nota: '))
    while grade2 < 0 or grade2 > 10:
        grade2 = float(input('Nota inválida! Digite a segunda nota: '))
    student.append(grade2)
    report_card.append(student)
    option = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if option == 'S':
        continue
    elif option == 'N':
        break
    else:
        option = str(input('Digite uma opção válida: [S/N] ')).strip().upper()[0]
        if option == 'N':
            break
print('''
_________________________________
Nº Name                Average''')
for s in range(len(report_card)):
    print(f'{s+1:<2} {report_card[s][0]:<20} {(report_card[s][1]+report_card[s][2])/2:.1f}')
while True:
    check = int(input('Quer ver as notas de algum aluno? Digite o número dele, ou 0 para sair: '))
    if check < 0 or check > len(report_card):
        check = int(input('Este aluno não exite, digite alguém dentro da lista ou 0 para sair:'))
    if check == 0:
        break
    print(f'{report_card[check-1][0]}: \nnota1: {report_card[check-1][1]} \nnota2: {report_card[check-1][2]}')
print('\nObrigado por verificar a nota do seu filho!')

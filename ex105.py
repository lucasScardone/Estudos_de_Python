def report(*n, show=False):
    r = dict()
    r['total'] = len(n)
    r['maximum'] = max(n)
    r['minimum'] = min(n)
    r['avg'] = sum(n)/len(n)
    if show:
        if r['avg'] >= 6:
            print('Aprovado.')
        elif 4 <= r['avg'] < 6:
            print('Recuperação.')
        else:
            print('Reprovado.')
    return r


#  Etaria
#  grades = []
#  while True:
#      grade = input('Digite uma nota: ')
#      try:
#          float(grade)
#      except ValueError:
#          grade = input('Digite a nota corretamente: ')
#      float(grade)
#      grades.append(grade)
#      option = str(input('Deseja adicionar outra nota? [S/N] ')).strip().upper()[0]
#      while option not in 'SN':
#          option = str(input('Deseja adicionar outra nota? [S/N] ')).strip().upper()[0]
#      if option == 'S':
#          continue
#      elif option == 'N':
#          break
report_card = report(4.9, 5.8, 2,1, 9.8, show=True)
print(report_card)

altura = float(input('Digite a altura da parede em metros:\n m:'))
largura = float(input('Digite a largura da parede em metros:\n m:'))
area = altura * largura
tinta = area / 2
print(f'A altura da parede é de {altura:.2f}m e a largura é de {largura:.2f}m. '
      f'\nCom uma área de {area:.2f}m², será necessário um total de {tinta:.2f} litro(s) de tinta para pintá-la.')

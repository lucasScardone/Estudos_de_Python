lista_peso = []
for c in range(1, 6):
    peso = float(input(f'Digite o peso da {c}ª pessoa: '))
    lista_peso.append(peso)
lista_peso.sort()
print(f'A pessoa mais leve pesa {lista_peso[0]:.1f}kg e a pessoa mais pesada pesa {lista_peso[4]:.1f}kg.')

cadastro_geral = []
count = fat_index = skinny_index = 0
while True:
    cadastro_individual = []
    nome = str(input('Nome: '))
    cadastro_individual.append(nome)
    peso = float(input('Peso: '))
    while peso <= 0:
        peso = float(input('Digite um peso válido: '))
    cadastro_individual.append(peso)
    cadastro_geral.append(cadastro_individual)
    if count == 0:
        fat_index = 0
        skinny_index = 0
    else:
        if peso < cadastro_geral[skinny_index][1]:
            skinny_index = count
        elif peso > cadastro_geral[fat_index][1]:
            fat_index = count
    count += 1
    option = str(input('Digite S para sair ou pressione qualquer tecla para continuar: ')).strip().upper()[0]
    if option == 'S':
        break
print(f'Ao todo você cadastrou {count} pessoas.')
print(f'O maior peso foi de {cadastro_geral[fat_index][1]}kg. O(A) gordo(a) é {cadastro_geral[fat_index][0]}.')
print(f'O menor peso foi de {cadastro_geral[skinny_index][1]}kg. O(A) magro(a) é {cadastro_geral[skinny_index][0]}.')

print('Vamos construir uma progressão aritmética!\n')
inicio = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = 0
mais_termos = 0
contador = 0
universal = 0
print('Os primeiros 10 termos da PA serão:')
while contador < 10:
    termo = inicio + (razao * (contador + mais_termos))
    print(f'{termo} ', end='-> ')
    contador += 1
    universal += 1
    if contador == 9:
        print('...')
        mais_termos = int(input('\nDeseja ver mais quantos termos? (Digite 0 para sair) '))
        contador -= mais_termos
print('...')
print(f'\nProgressão finalizada com {universal} termos mostrados.')

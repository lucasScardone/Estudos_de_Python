print('Vamos construir uma progressão aritmética!\n')
inicio = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = 0
contador = 0
print('Os primeiros 10 termos da PA serão:')
while contador < 10:
    termo = inicio + (razao * contador)
    print(f'{termo} ', end='-> ')
    contador += 1
print('...')

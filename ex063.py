n = int(input('Quantos termos da sequência de Fibonacci você quer ver? (Mínimo 1) '))
if n < 1:
    print('Pare com isso.')
    exit()
contador = 0
t1 = 0
t2 = 1
soma = 0
print(f'A sequência de Fibonacci gerada é:')
while n > contador:
    print(f'{soma} ', end='-> ')
    contador += 1
    t1 = t2
    t2 = soma
    soma = t1 + t2
print('...')

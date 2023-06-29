contador = 0
num = int(input('Quer ver a tabuada de qual valor? '))
while True:
    if num < 0:
        break
    contador += 1
    print('-=-' * 5)
    for m in range(1, 11, +1):
        print(f'{num} x {m} = {num * m}')
    print('-=-' * 5)
    num = int(input('Quer ver a tabuada de mais algum valor? (Número negativo para sair) '))
print('\nPudding.exit')

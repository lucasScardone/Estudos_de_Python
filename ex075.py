numbers = (int(input('Digite um número inteiro: ')), int(input('Digite outro número inteiro: ')),
           int(input('Digite mais um número inteiro: ')), int(input('Digite o último número inteiro: ')))
print(f'Você digitou os valores {numbers}')
print(f'O valor 9 apareceu {numbers.count(9)} vezes')
if 3 in numbers:
    print(f'O valor 3 apareceu na {numbers.index(3) + 1}ª posição.')
else:
    print(f'O número 3 não foi digitado')
print('Os valores pares digitados foram: ')
for n in numbers:
    if n % 2 == 0:
        print(n, end=' ')

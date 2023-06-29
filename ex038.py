num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite mais um número inteiro: '))

if num1 > num2:
    print('O primeiro valor é maior.')
elif num2 > num1:
    print('O segundo valor é maior.')
elif num2 == num1:
    print('Os valores_list são iguais.')
else:
    print('Eu não sei como você chegou até aqui, mas algo está muito errado.')

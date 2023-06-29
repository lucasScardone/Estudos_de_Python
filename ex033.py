num1 = int(input('Digite o primeiro valor: \n'))
num2 = int(input('Digite o segundo valor: \n'))
num3 = int(input('Digite o terceiro valor: \n'))
# Verificando o menor valor.
if num1 <= num2 and num1 <= num3:
    print(f'O número {num1} é o menor valor.')
elif num2 <= num1 and num2 <= num3:
    print(f'O número {num2} é o menor valor.')
else:
    print(f'O número {num3} é o menor valor.')
# Verificando o valor do meio.
if num2 >= num1 >= num3 or num3 >= num1 >= num2:
    print(f'O número {num1} é o número do meio.')
elif num1 >= num2 >= num3 or num3 >= num2 >= num1:
    print(f'O número {num2} é o número do meio')
else:
    print(f'O número {num3} é o número do meio.')
# Verificando o maior valor.
if num1 >= num2 and num1 >= num3:
    print(f'O número {num1} é o maior valor.')
elif num2 >= num1 and num2 >= num3:
    print(f'O número {num2} é o maior valor.')
else:
    print(f'O número {num3} é o maior valor.')

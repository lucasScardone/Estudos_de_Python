salario = float(input('Qual é o seu salário? \nR$'))

if 0 <= salario <= 1250.00:
    print(f'Seu salário reajustado será de R${(salario * 1.15):.2f}.')
elif salario > 1250.00:
    print(f'Seu salário reajustado será de R${(salario * 1.1):.2f}.')
else:
    print(f'Salário inválido')

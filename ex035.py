lado1 = float(input('Informe um comprimento de lado para o triângulo: '))
lado2 = float(input('Informe outro comprimento de lado para o triângulo: '))
lado3 = float(input('Informe o último comprimento de lado para o triângulo: '))

if lado1 >= lado2 + lado3 or lado2 >= lado1 + lado3 or lado3 >= lado1 + lado2:
    print('Este triângulo não é possível.')
else:
    print('Este triângulo é possível.')

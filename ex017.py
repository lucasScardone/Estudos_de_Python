import math
co = float(input('Qual a medida do cateto oposto? \n'))
ca = float(input('Qual a medida do cateto adjacente? \n'))
hipotenusa = math.sqrt(pow(co, 2) + pow(ca, 2))
hypot = math.hypot(co, ca)
print(f'A hipotenusa deste triângulo retângulo é igual a {hipotenusa:.2f}.')
print(f'A hipotenusa deste triângulo retângulo é igual a {hypot:.2f}.')

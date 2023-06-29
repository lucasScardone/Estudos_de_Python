c1 = float(input('Digite o primeiro lado do triângulo: '))
c2 = float(input('Digite o segundo lado do triângulo: '))
c3 = float(input('Digite o terceiro lado do triângulo: '))

if c1 >= c2 + c3 or c2 >= c1 + c3 or c3 >= c1 + c2:
    print('Esses lados não formam um triângulo')
else:
    if c1 == c2 and c2 == c3:
        print('Os segmentos formam um triângulo equilátero.')
    elif (c1 == c2 and c1 != c3) or (c2 == c3 and c2 != c1) or (c3 == c1 and c3 != c2):
        print('Os segmentos formam um triângulo isósceles.')
    elif c1 != c2 and c2 != c3:
        print('Os segmentos formam um triângulo escaleno.')
    else:
        print('Eu não sei como você chegou aqui...')

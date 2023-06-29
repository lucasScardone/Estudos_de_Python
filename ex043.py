peso = float(input('Qual é o seu peso em kg? (ex: 89) \n'))
altura = float(input('Qual é a sua altura em metros e cm? (ex: 1.72) \n'))
imc = round(peso / (altura ** 2), 2)

print(f'Seu IMC é de {imc}, seu estado é de:')

if 0 <= imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('peso ideal')
elif 25 <= imc < 30:
    print('Acima do peso')
elif 30 <= imc < 40:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade mórbida')
else:
    print('Você inseriu um valor negativo, né?')

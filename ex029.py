velocidade = float(input('Qual é a velocidade do seu carro? \n Km/h:'))
multa = (velocidade - 80) * 7
if velocidade <= 80:
    print(f'\nVocê está dirigindo a {velocidade:.2f} km/h. Tenha uma boa viagem!')
else:
    print(f'''\nVocê está dirigindo a {velocidade:.2f} km/h.
Você está acima do limite de 80 km/h! 
Sua multa será de {multa:.2f} reais.''')

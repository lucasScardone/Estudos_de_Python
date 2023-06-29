dias = int(input('O carro foi alugado por quantos dias? \n Nº de dias: '))
km = float(input('O carro percorreu quantos kilômetros? \n Km: '))
custo = (km * 0.15) + (dias * 60)
print(f'\nO total a pagar é de R${custo:.2f}.')

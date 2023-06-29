frase = str(input('Digite uma palavra ou frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if junto == inverso:
    print(f'{junto} é palíndromo de {inverso}.')
else:
    print(f'{junto} não é palíndromo de {inverso}')

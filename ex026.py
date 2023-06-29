frase = str(input('Digite uma frase: \n')).strip()
fraseU = frase.upper()
print(f'''
A letra A aparece {fraseU.count('A')} vezes.
A primeira letra A aparece na posição {fraseU.find('A') + 1}.
A última letra A aparece na posição {fraseU.rfind('A') + 1}.
''')

nome = str(input('Digite seu nome completo: \n')).strip()
minusculas = nome.lower()
print(f'Seu nome apenas em minúsculas é {minusculas}.')
maiusculas = nome.upper()
print(f'Seu nome apenas em maiúsculas é {maiusculas}.')
sem_espaco = len(nome) - nome.count(' ')
print(f'Seu nome completo tem {sem_espaco} letras.')
espaco = nome.find(' ')
print(f'Seu primeiro nome tem {espaco} letras')

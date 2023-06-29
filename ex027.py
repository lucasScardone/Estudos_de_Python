nome = str(input('Digite seu nome completo: \n')).strip()
nome_split = nome.split()
print(f'''
Muito prazer em te conhecer!
Seu primeiro nome é {nome_split[0]}
Seu último nome é {nome_split[len(nome_split) - 1]}
''')

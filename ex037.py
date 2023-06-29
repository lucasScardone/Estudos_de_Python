num = int(input('Digite um número inteiro: '))
print("""
[1] Converter para binário
[2] Converter para octal
[3] converter para hexadecimal
""")
base = int(input('Escolha uma das bases numéricas para conversão: '))
if base == 1:
    print(f'{num} convertido em binário é igual a {bin(num)[2:]}.')
elif base == 2:
    print(f'{num} convertido em octal é igual a {oct(num)[2:]}')
elif base == 3:
    print(f'{num} convertido em hexadecimal é igual a {hex(num)[2:]}')
else:
    print('\nPor favor digite uma base válida da próxima vez...')

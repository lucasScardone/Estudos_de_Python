total = contador = 0
num = int(input('Digite um número inteiro a ser somado: (Ou 999 para sair)\n'))
while True:
    if num == 999:
        break
    total += num
    contador += 1
    num = int(input('Digite um número inteiro a ser somado: (Ou 999 para sair)\n'))
print(f'O somatório dos seus {contador} números é {total}.')

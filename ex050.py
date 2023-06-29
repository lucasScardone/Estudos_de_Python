soma_par = 0
num_par = 0
soma_impar = 0
num_impar = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}º valor inteiro para talvez ser somado: '))
    if (num % 2) == 0:
        soma_par += num
        num_par += 1
    elif (num % 2) != 0:
        soma_impar += num
        num_impar += 1
print(f'\n A quantidade de números pares foi de {num_par} e a soma é de {soma_par}.')
print(f'\n A quantidade de números ímpares foi de {num_impar} e a soma é de {soma_impar}.')

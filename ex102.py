def factorial(num, show=False):
    """
    param num: O número a ser calculado.
    param show: Mostrar ou não o processo.
    return: O valor do fatorial de num.
    """
    f = 1
    if num == 0:
        print('0 fatorial é igual a 1, não me pergunte o porquê.')
    for n in range(num, 0, -1):
        if show:
            print(n, end='')
            if n > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= n
    return f


number = int(input('Digite um número inteiro positivo para calcularmos o fatorial: '))
while number < 0:
    number = int(input('Digite um número inteiro POSITIVO para calcularmos o fatorial: '))
option = str(input('Deseja ver o processo de fatorial? [S/N]')).strip().upper()[0]
while option not in 'SN':
    option = str(input('Deseja ver o processo de fatorial? Digite uma opção válida [S/N] ')).strip().upper()[0]
if option == 'S':
    print(factorial(number, show=True))
elif option == "N":
    print(factorial(number, show=False))

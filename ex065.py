opcao = cont = total = num = 0
lista_num = []
while opcao != 'N':
    num = float(input('Digite um número para termos uma média final: '))
    total += num
    cont += 1
    lista_num.append(num)
    opcao = str(input('Deseja continuar? '
                      'Digite "N" para sair ou qualquer tecla para continuar:  ')).strip().upper()[0]
lista_num.sort()
media = total / cont
print(f'\nA média dos {cont} números é de {media:.1f}.'
      f' O menor número foi {lista_num[0]} e o maior número foi {lista_num.pop()}')

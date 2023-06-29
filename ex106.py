from time import sleep


def pyhelp(msg):
    sleep(1)
    print(f'Acessando o manual de {msg}')
    sleep(1)
    help(msg)
    sleep(1)
    

while True:
    print('''
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-
       Sistema de ajuda pyhelp
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    ''')
    command = input('Deseja ver o manual de alguma função ou biblioteca? [Digite FIM para sair]: ')
    if command.strip().upper() == 'FIM':
        break
    pyhelp(command)
print('Adeus')

def player(n, g):
    if n == '':
        n = 'desconhecido'
    if g.isnumeric():
        g = int(g)
        print(f'O jogador {n} fez {g} gols no campeonato.')
    else:
        print(f'O jogador {n} fez 0 gols no campeonato.')


player(input('Nome do jogador: '), input('Número de gols: '))

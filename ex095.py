players = []
while True:
    player = {'name': str(input('Nome do jogador de futebol: ')),
              'matches': int(input('Quantas partidas ele jogou? ')),
              'score': [],
              'total': 0}
    for match in range(player['matches']):
        player['score'].append(int(input(f'Quantos gols ele fez na partida {match+1}? ')))
        while player['score'][match] < 0:
            player['score'][match] = int(input(f'Quantos gols ele fez na partida {match + 1}? (insira um dado válido)'))
        player['total'] += player['score'][match]
    players.append(player)
    option = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while option not in 'SN':
        option = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if option == 'S':
        continue
    elif option == 'N':
        break
print('-=' * 20)
print('Cod nome      gols           total')
print('-' * 40)
for p in range(len(players)):
    print(f'{p+1:<2} | {players[p]["name"]:<10} | {players[p]["score"]} | {players[p]["total"]:>2}')
print('-' * 40)
while True:
    option = str(input('Deseja ver os dados de mais algum jogador? [S/N]')).strip().upper()[0]
    while option not in 'SN':
        option = str(input('Deseja ver os dados detalhados de algum jogador? [S/N]')).strip().upper()[0]
    if option == 'S':
        chosen = int(input('Digite o código do jogador: '))
        while chosen <= 0 or chosen > len(players):
            chosen = int(input('Digite o código do jogador: '))
        print(f'''
        O jogador {players[chosen-1]['name']} jogou {players[chosen-1]['matches']} partidas.
        Durante os jogos, ele fez este exato número de gols: {players[chosen-1]['score']}.
        Marcando um total de {players[chosen-1]['total']} gols.
        Sua média de gols por partida é de {(players[chosen-1]['total'] / players[chosen-1]['matches']):.1f}.
        ''')
    elif option == 'N':
        break

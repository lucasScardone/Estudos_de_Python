player = {'name': str(input('Nome do jogador de futebol: ')),
          'matches': int(input('Quantas partidas ele jogou? ')),
          'score': [],
          'total': 0}
for match in range(player['matches']):
    player['score'].append(int(input(f'Quantos gols ele fez na partida {match+1}? ')))
    while player['score'][match] < 0:
        player['score'][match] = int(input(f'Quantos gols ele fez na partida {match + 1}? (insira um dado válido)'))
    player['total'] += player['score'][match]
print(f'''
O jogador {player['name']} jogou {player['matches']} partidas.
Durante os jogos, ele fez este exato número de gols: {player['score']}.
Marcando um total de {player['total']} gols.
Sua média de gols por partida é de {(player['total']/player['matches']):.1f}.
''')

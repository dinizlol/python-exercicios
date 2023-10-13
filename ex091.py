from random import randint
from time import sleep
jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}
for k, v in jogadores.items():
    print(f'O jogador {k} jogou {v}')
    sleep(1)
ranking = dict(sorted(jogadores.items(), key=lambda item: item[1], reverse=True))
for k, v in ranking:
    print(f'{k} {v}')

    #mudou algo desde o vídeo até o dia de hoje

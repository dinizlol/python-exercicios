jogador = dict()
listap = list()
def linha():
    print('=-' * 30)
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
for p in range(0, (partidas)):
    listap.append(int(input(f'Quantos gols o {jogador["nome"]} marcou na {p}ª partida? ')))
jogador['gols'] = listap[:]
jogador['total'] = sum(listap)
linha()
print(jogador)
linha()
for c, k in jogador.items():
    print(f'O campo {c} tem o valor {k}')
linha()
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} jogos')
for i, p in enumerate(jogador["gols"]):
    print(f'Na partida {i}, fez {p} gols')
print(f'Somando um total de {jogador["total"]} gols.')

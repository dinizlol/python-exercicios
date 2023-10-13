time = list()
jogador = dict()
partidas = list()
def linha():
    print('=-' * 30)


while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input('Quantas partidas o jogador jogou? '))
    for a in range(0, tot):
        partidas.append(int(input(f'Quantos gols ele marcou na {a}ª partida? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    partidas.clear()
    resposta = str(input('Deseja cadastrar outro jogador? [S/N] ')).upper()
    if resposta == 'N':
       break
print('Cod', end=' ')
for i in jogador.keys():
    print(i, end=' ')
print()
linha()
for i, v in enumerate(time):
    print(i, end=' ')
    for d in v.values():
        print(d, end=' ')
    print()
print()
linha()

while True:
    opçao = int(input('Qual jogador gostaria de saber detalhes? 999 para encerrar  '))
    if opçao == 999:
        print('Obrigado por usar este programa!')
        break
    print(f'Levantamento do jogador {time[opçao]["nome"]} ')
    for i, v in enumerate(time[opçao]['gols']):
        print(f' No jogo {i} {time[opçao]["nome"]} fez {v} gols.')
    linha()
linha()
print()

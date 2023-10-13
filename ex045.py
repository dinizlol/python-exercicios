from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(computador)
print('''Vamos jogar!
Escolha uma opção:
[0] Pedra
[1] Tesoura
[2] Papel''')

jogador = int(input('Qual a sua jogada? '))

if computador == 0:
    if jogador == 0:
        print('EMPATE! O computador também jogou Pedra!')
    elif jogador == 1:
        print('PERDEU! O computador jogou Pedra.')
    elif jogador == 2:
        print('Você venceu! O computador jogou Pedra.')
elif computador == 1:
    if jogador == 0:
        print('Venceu! O computador jogou Tesoura.')
    elif jogador == 1:
        print('EMPATE! O computador também jogou Tesoura!')
    elif jogador == 2:
        print('Perdeu! O computador jogou Tesoura.')
elif computador == 2:
    if jogador == 0:
        print('Perdeu! O computador jogou Papel')
    elif jogador == 1:
        print('Venceu! O computador jogou Papel')
    elif jogador == 2:
        print('EMPATE! O computador também jogou Papel. ')
else:
    print('JOGADA INVALIDA!')




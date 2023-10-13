from random import randint
tentativas = 1
computador = randint(0, 10)
acertou = False
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print('Menos...')
            tentativas += 1
        elif jogador < computador:
            print('Mais...')
            tentativas += 1
print('Acertou!')
print(f'Você precisou de {tentativas} tentativas.')
from random import randint
print('=-'*10)
print('Vamos jogar par ou impar!')
print('-='*10)
while True:
    jogador = int(input('Digite um valor: '))
    pi = input('Par ou ímpar? [P/I] ').upper().strip()[0]
    computador = randint(1, 10)
    print(f'Você jogou {jogador} e o computador jogou {computador}')
    if pi == 'P':
        if (jogador + computador) % 2 == 0:
            print('Você venceu!\nVamos jogar novamente. \n')
        else:
            print('Você perdeu!')
            break
    elif pi == 'I':
        if (jogador + computador) % 2 != 0:
            print('Você venceu!\nVamos jogar novamente. \n')
        else:
            print('Você perdeu!!')
            break
print('~'*10)
print('Game over!')
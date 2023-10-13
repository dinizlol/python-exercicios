#from random import randint
#from time import sleep
#pc = randint(0, 5)
#print('=-=' * 20)
#print('Estou pensando em um número entre 0 e 5, consegue adivinhar? ')
#print('-=-' * 20)
#print('Pensando...')
#sleep(3)
#jogador = int(input('Em que número eu pensei? '))
#if jogador == pc:

#    print('Parabéns, você acertou!')
#else: print(f'Errou! Eu pensei no número {pc} não no {jogador} ')

from random import randint
from time import sleep

print('Estou pensando em um número entre 0 e 5, consegue adivinhar?')

número = randint(0, 5)

print('Pensando...')
sleep(2)

jogador = int(input('Qual número eu pensei? '))

if jogador == número:
    print('Parabéns! você acertou!')
else:
    print(f'Errou! Eu pensei no número {número}, não no número {jogador}!')



'''from random import randint
print('=-' * 30)
print('JOGO DA MEGA SENA')
print('=-' * 30)


lista = list()
jogos = list()
quant = int(input('Quantos jogos você gostaria de jogar? '))
tot = 1
while tot < quant:
    cont = 0
    while True:
        num = randint(0, 60)
        if num not in jogos:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    jogos.sort()
    lista.append(jogos[:])
    jogos.clear()
    tot += 1'''

from random import randint
from time import sleep

principal = list()
temp = list()
quant = int(input('Quantas vezes vc quer que eu randomize? '))
tot = 0
while quant != tot:
    cont = 0
    while True:
        numero = randint(1, 60)
        if numero not in temp:
            temp.append(numero)
            cont += 1
            if cont == 6:
                break
    temp.sort()
    principal.append(temp[:])
    temp.clear()
    tot += 1

for c, l in enumerate(principal):
    print(f'{c+1}º Jogo: {l} ')
    sleep(1)























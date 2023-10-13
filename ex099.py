from time import sleep
from random import randint

def maior(* num):
    cont = maior = 0
    print('Analisando os valores passados: ', end='')
    for valor in num:
        print(valor, end=' ')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nO maior número foi {maior}')
    print(f'Houveram {cont} números digitados')

maior(0, 1, 3, 5, 7)
maior(randint(0, 50), randint(0, 50), randint(0, 50), randint(0, 50), randint(0, 50))

'''gesu = list()
for i in range(0, randint(0, 10)):
    gesu.append(randint(0, 10))

print(gesu)

maior(gesu)'''

from random import randint
from time import sleep
def sorteia(lista):
    print('Sorteando os valores da lista: ', end='')
    for i in range(0, 6):
        lista.append(randint(0, 10))
        sleep(0.2)
        print(lista[i], end=' ')
    print()

numeros = list()
sorteia(numeros)

def somapar(soma):
    soma = 0
    listapares = []
    for i, c in enumerate(numeros):
        if c % 2 == 0:
            soma += c
            listapares.append(c)
    print(f'A soma dos números pares é {soma}')
    return listapares
#somapar(numeros)
pares = somapar(numeros)
print(pares)















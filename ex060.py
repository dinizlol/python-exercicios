#numero = int(input('Digite um número para saber seu fatorial: '))
#calculo = numero
#f = 1
#print(f'{numero} x', end=' ')
#while numero != 0:
#    f = f * numero
#    numero -= 1
#    print(f'{numero}', end='')
#    print(' x' if numero > 0 else ' =', end=' ')

#print(f)

numero = int(input('Digite um número para saber seu fatorial: '))
calculo = numero
f = 1
print(f'{numero} x', end=' ')
for c in range(numero, 1, -1):
    f = f * calculo
    calculo -= 1
    print(f'{calculo}', end='')
    print(' x' if calculo > 0 else ' =', end=' ')
print(f)
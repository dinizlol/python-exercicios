'''lista = list()
par = list()
impar = list()

while True:
    n = int(input('Digie um valor: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    r = str(input('Deseja digitar outro número? [S/N]'))
    if r in 'Nn':
        break
print(f'A lista completa é: {lista}')
print(f'A lista de pares é: {par}')
print(f'A lista de ímpares é: {impar}')'''

numeros = list()
pares = list()
impares = list()

while True:
    numeros.append(int(input('Digite um número: ')))
    r = str(input('Deseja continuar? [S/N]'))
    if r in 'Nn':
        break

for i, v in enumerate(numeros):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print(f'A lista completa de números é: {numeros}')
print(f'A lista dos números pares é: {pares}')
print(f'A lista dos números ímpares é: {impares}')

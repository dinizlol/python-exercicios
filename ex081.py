lista = list()

while True:
    lista.append(int(input('Digite um valor: ')))
    r = str(input('Deseja continuar? [S/N]'))
    if r in 'Nn':
        break
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} números.')
print(f'Os números em ordem decrescente são: {lista}')
if 5 in lista:
    print(f'O número 5 está na lista.')
else:
    print('O número 5 não está na lista')
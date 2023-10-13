lista = list()

while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor já existente!')
    r = str(input('Deseja continuar? [S/N] '))
    if r in 'Nn':
        break


lista.sort()
print(f'Os valores digitados foram:{lista}')




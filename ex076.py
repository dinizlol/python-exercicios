'''listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 5.25, 'Transferidor', 4.20, 'Compasso',
           9.99, 'Mochila', 120.85, 'Canetas', 22.30, 'Livro', 25.35)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')'''

listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 5.25, 'Transferidor', 4.20, 'Compasso',
           9.99, 'Mochila', 120.85, 'Canetas', 22.30, 'Livro', 25.35)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(pos)
    else:
        print(f'R${listagem[pos]:>7.2f}')


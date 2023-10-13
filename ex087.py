matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = scol = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a matriz[{l}, {c}] '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()

print(f'A soma dos números pares é: {spar}')
for i in range(0, 3):
    scol += matriz[i][2]
print(f'A soma da terceira coluna é: {scol}')
for i in range(0, 3):
    if i == 0:
        maior = matriz[1][i]
    else:
        if matriz[1][i] > maior:
            maior = matriz[1][i]
print(f'O maior número da segunda linha é: {maior}')

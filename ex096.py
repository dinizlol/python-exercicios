def mult(a, b):
    d = a * b
    print(f'A área de um terreno {a}x{b} é de {d}')


print(' Controle de terrenos ')
print('=-' * 30)

larg = float(input('LARGURA(M): '))
compr = float(input('COMPRIMENTO(M): '))
mult(larg, compr)

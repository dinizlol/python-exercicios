
while True:
    n = int(input('Qual número você deseja saber a tabuada? '))
    if n < 0:
        break
    for a in range(1, 11, 1):
        print(f'{n} x {a} = {n*a}')

print('Número incorreto, programa encerrado.')
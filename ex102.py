def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        f = f * c
        if show:
            print(c, end='')
            if c > 1:
                print('x', end='')
            else:
                print('=', end='')

    return (f)



fat = int(input('Qual número você deseja saber seu fatorial? '))
fatorial(fat, show=False)

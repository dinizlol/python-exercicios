from time import sleep
def contagem(a, b, c):
    print('~-' * 30)
    print(f'Contagem de {a} até {b-1} de {c} em {c}')
    sleep(1)
    for u in range(a, b, c):
        print(u, end=' ')
        sleep(0.2)
    print('FIM!')
    print()
    print('~-' * 30)


contagem(0, 11, 1)
contagem(10, 0, -2)

print('Agora é sua vez de personalizar a contagem!')
i = int(input('Digite o ínicio: '))
f = int(input('Digite o fim: '))
q = int(input('Digite de quanto em quanto a contagem deve ser feita: '))
contagem(i, f, q)





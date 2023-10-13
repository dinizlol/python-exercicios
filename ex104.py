def leiaint(numero):
    while True:
        n = str(input(numero))
        if n.isnumeric():
            return n
        else:
            print('ERRO! digite um número inteiro')


n = leiaint('Digite um numero ')
print(f'O valor digitado foi {n}.')

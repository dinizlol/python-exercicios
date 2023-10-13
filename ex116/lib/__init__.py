def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print('Digite um número inteiro válido.')
        else:
            return n




def linha(lin=42):
    print('-' * lin)

def cabeçalho(msg):
    linha()
    print(msg.center(42))
    linha()

def menu(lista):
    for i, c in enumerate(lista, start=1):
        print(i, '-', c)
    linha()
    op = leiaint('Digite uma opção: ')
    return op



def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Digite um número inteiro valido.')
            continue
        except KeyboardInterrupt:
            print('\nO usuario prefiriu não terminar o programa. ')
            return 0
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (TypeError, ValueError):
            print('Por favor, digite um numero real.')
            continue
        except KeyboardInterrupt:
            print('\nO usuário prefiriu não inserir os dados.')
            return 0
        return n



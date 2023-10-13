def leiadinheiro(msg):
    while True:
        n = str(input(msg)).replace(',', '.').strip()
        if n.isalpha() or n == '':
            print('Erro! Digite um valor válido')
        else:
            return float(n)


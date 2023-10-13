def metade(valor=0):
    return valor / 2


def dobro(valor=0):
    return valor * 2


def porcento(valor, taxa=0):
    return valor + (valor * taxa / 100)

def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')

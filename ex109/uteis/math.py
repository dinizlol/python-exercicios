def metade(valor=0, formatado=False):
    res = valor / 2
    return res if not formatado else moeda(res)


def dobro(valor=0, formatado=False):
    res = valor * 2
    return res if not formatado else moeda(res)


def porcento(valor, taxa=0, formatado=False):
    res = valor+(valor * taxa/100)
    return res if formatado is False else moeda(res)

def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')

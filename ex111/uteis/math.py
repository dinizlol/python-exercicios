def metade(valor=0, formatado=False):
    res = valor / 2
    return res if not formatado else moeda(res)


def dobro(valor=0, formatado=False):
    res = valor * 2
    return res if not formatado else moeda(res)


def porcentoa(valor, taxa=0, formatado=False):
    res = valor+(valor * taxa/100)
    return res if formatado is False else moeda(res)

def porcentod(valor, taxa=0, formatado=False):
    res = valor-(valor * taxa/100)
    return res if formatado is False else moeda(res)

def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')

def resumo(preço=0, taxaa=0, taxad=0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Analisando o preço: \t{moeda(preço)}')
    print(f'Metade do preço: \t\t{metade(preço, True)}')
    print(f'Dobro do preço: \t\t{dobro(preço, True)}')
    print(f'{taxaa}% de aumento: \t\t{porcentoa(preço, taxaa, True)}')
    print(f'{taxad}% de desconto: \t\t{porcentod(preço, taxad, True)}')
    print('-' * 30)


#gold = int(input('How much gold do you have? '))
#reais = gold * 0.000265
#dolar = reais / 4.96
#euro = dolar * 1.07
#pesosar = dolar * 240.41
#sol = dolar * 3.68
#print('You can sell your gold for R${} '.format(reais))
#print('You can sell your gold for U${:.2f} '.format(dolar))
#print('You can sell your gold for £{:.2f}'.format(euro))
#print('You can sell your gold for AR${:.2f}'.format(pesosar))
#print('You can sell your gold for PER${:.2f}'.format(sol))


reais = float(input('Quantos reais você gostaria de gastar? R$'))
dolar = float(input('Qual a cotação do dolar hoje? '))

valfinal = reais/dolar

print(f'Com a quantia de R${reais} dá para comprar U${valfinal:.2f}')









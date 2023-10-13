print('================LOJA DO DENIS================')
valor = float(input('Digite o valor da compra: R$'))
print('''FORMA DE PAGAMENTO
[1] PAGAMENTO A VISTA
[2] PAGAMENTO A VISTA NO CARTÃO
[3] 2X NO CARTÃO
[4] 3X OU MAIS NO CARTÃO''')
opção = int(input('Digite uma opção(1-4): '))
if opção == 1:
    calculo = valor - (valor * 10 / 100)
elif opção == 2:
    calculo = valor - (valor * 5 / 100)
elif opção == 4:
    parcela = int(input('Quantas parcelas? '))
    calculo = valor + (valor * 20 / 100)
    total = calculo / parcela
    print(f'Sua compra será feita em {parcela} vezes de R${total:.2f}a')
elif opção == 3:
    total = valor / 2
    calculo = valor
    print(f'Sua compra será parcelada em 2x ao mês, sendo R${total:.2f} por mês.')
else:
    print('Opção errada. Digite de 1 a 4.')
print(f'Sua compra no valor de R${valor:.2f} será agora de R${calculo:.2f}')
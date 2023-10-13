print('<>'*20)
print('CAIXA ELETRÔNICO')
print('<>'*20)
valor = int(input('Quanto você desejaria sacar?'))
ced = 50
total = valor
totalced = 0
confirmação = False
while not confirmação:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Você receberá {totalced} notas de R${ced}.')
        if ced == 50:
            ced = 20
        elif ced == 20:
          ced = 10
        elif ced == 10:
           ced = 1
        elif total == 0:
            confirmação = True
        totalced = 0
print('Obrigado por usar o caixa eletronico')
#valor = int(input('Qual o valor deseja sacar? '))



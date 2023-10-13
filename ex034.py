#sal = float(input('Digite o salário do funcionário: R$'))
#if sal <= 1250.00:
#    aum = sal + (sal * 15 / 100)
#else: aum = sal + (sal * 10/100)
#print(f'O novo salário é de R${aum:.2f}')


sal = float(input('Qual o salário do funcionário? R$'))
if sal <= 1250.00:
    aum = sal+(sal*15/100)
else:
    aum = sal+(sal*10/100)
print(f'O novo salário do funcionário é de: R${aum}')


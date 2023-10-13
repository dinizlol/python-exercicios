#sal = float(input('Qual o salário do funcionário? R$'))
#aum = float(input('Quanto é o aumento que você deseja dar ao funcionário? '))

#fin = sal + (sal * aum/100)


#print(f'O salário do funcionário foi de R${sal} para R${fin:.2f}.')
salário = float(input('Qual o salário do funcionário? R$'))
aumento = int(input(f'Qual o aumento que deseja dar a ele? '))


real = salário + (salário * aumento/100)

print(f'O salário do funcionário foi de R${salário:.2f} para R${real:.2f}')
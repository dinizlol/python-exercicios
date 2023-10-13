#produto = float(input('Qual o valor do produto? R$'))
#print(f'O produto que custava{produto}, com 5% de desconto custará R${produto*0.95:.2f}.')

prod = float(input('Qual o valor do produto? R$'))
desc = float(input('Quanto de desconto você gostaria? '))

porcentagem = prod - (prod*desc/100)

print(f'O produto que custava R${prod} custará R${porcentagem:.2f}')
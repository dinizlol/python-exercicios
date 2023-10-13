from uteis import math

num = int(input('Digite o preço: R$'))

print(f'A metade de R${num} é R${math.metade(num)}')
print(f'O dobro de R${num} é R${math.dobro(num)}')
taxa = int(input('Quantos % vc quer? '))
print(f'{taxa}% de R${num} é R${math.porcento(num, taxa)}')
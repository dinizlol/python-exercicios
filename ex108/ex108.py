from uteis import math

num = int(input('Digite o preço: R$'))

print(f'A metade de {math.moeda(num)} é {math.moeda(math.metade(num))}')
print(f'O dobro de {math.moeda(num)} é {math.moeda(math.dobro(num))}')
print(f'10% de {math.moeda(num)} é {math.moeda(math.porcento(num, 10))}')




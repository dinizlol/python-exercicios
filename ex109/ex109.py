from uteis import math

num = int(input('Digite o preço: R$'))

print(f'A metade de {math.moeda(num)} é {math.metade(num, True)}')
print(f'O dobro de {math.moeda(num)} é {math.dobro(num, True)}')
print(f'10% de {math.moeda(num)} é {math.porcento(num, 10, True)}')




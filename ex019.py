#from random import choice
#n1 = input('Primeira marca ')
#n2 = input('Segunda marca ')
#n3 = input('Terceira marca ')
#n4 = input('Quarta marca ')
#n5 = input('Quinta marca ')

#lista = [n1, n2, n3, n4, n5]

#sorteado = choice(lista)

#print(f'O sorteado foi: {sorteado}')

from random import choice

a1 = input('Qual o nome do primeiro aluno?' )
a2 = input('Qual o nome do segundo aluno? ')
a3 = input('Qual o nome do terceiro aluno? ')
a4 = input('Qual o nome do último aluno? ')
lista = [a1, a2, a3, a4]


sorteado = choice(lista)

print(f'O aluno sorteado foi: {sorteado}!')
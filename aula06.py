nome = input('Qual é o seu nome? ')
sobrenome = input('Qual é o seu sobrenome? ')
idade = input('Qual é a sua idade? ')
nascimento = input('Aonde você nasceu? ')
pet = input('Qual é o nome do seu cachorro? ')

print('Olá, {} {}. Sua idade é {}, você nasceu em {} '
      'e seu animal de estimação chama {}.'.format(nome, sobrenome,
    idade, nascimento, pet))

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1+n2

print('a soma de {} e {} é de:{} '.format(n1, n2, s))

a = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Está em maiúsculas? ', a.isupper())
print('Está em minúsculas? ', a.islower())
print('Está capitalizada? ', a.istitle())




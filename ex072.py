cont = 'Zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',\
    'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
resp = ' '
continuar = True
while continuar:
    num = int(input('Digite um número: '))
    if 0 <= num <= 20:
        print(f'O número {num}, escrito por extenso é: {cont[num]}.')
    else:
        print('Por favor, digite um número entre 0 e 20')
    while 0 <= num <= 20:
        resp = input('Deseja continuar? [S/N]').capitalize().strip()[0]
    while continuar not in 'SN':
            print('Por favor, digite "S" ou "N"')
    if continuar == 'N':
        continuar = False

print('Obrigado por usar esse programa')


'''cont = ['Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', \
        'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', \
        'Dezenove', 'Vinte']

continuar = True

while continuar:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'O número {num} se escreve {cont[num]}')
    resp = input('Você gostaria de digitar outro número? [S/N] ').capitalize().strip()[0]
    while resp not in 'SN':
        resp = input('Responda apenas com "S" ou "N": ').capitalize().strip()[0]
    if resp == 'N':
        continuar = False

print('Obrigado por usar esse programa!')'''

num = int(input('Digite um número inteiro: '))

print('''Escolha uma opção abaixo:
[1] converter para binário
[2] converter para octal
[3] converter para hexadecimal''')
n = int(input('Digite uma opção: '))

if n == 1:
    print(f'O número {num} convertido para para binário é: {bin(num)[2:]}')
elif n == 2:
    print(f'O número {num} convertido para decimal é: {oct(num)[2:]}')
elif n == 3:
    print(f'O número {num} convertido para hexadecimal é: {hex(num)[2:]}')
else:
    print('Opção errada! Digite 1, 2 ou 3.')
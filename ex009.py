#n = int(input('Digite um número para saber sua tabuada: '))

#print('-'*12)
#print('{} x {:2} = {}'.format(n, 1, n*1))
#print('{} x {:2} = {}'.format(n, 2, n*2))
#print('{} x {:2} = {}'.format(n, 3, n*3))
#print('{} x {:2} = {}'.format(n, 4, n*4))
#print('{} x {:2} = {}'.format(n, 5, n*5))
#print('{} x {:2} = {}'.format(n, 6, n*6))
#print('{} x {:2} = {}'.format(n, 7, n*7))
#print('{} x {:2} = {}'.format(n, 8, n*8))
#print('{} x {:2} = {}'.format(n, 9, n*9))
#print('{} x {:2} = {}'.format(n, 10, n*10))
#print('--'*6)


#n = int(input('Digite um número pra saber a tabuada dele: '))

#print('\033[7;34m=-=\033[m'*20)

#print(f'{n} x  1 = {n*1}')
#print(f'{n} x  2 = {n*2}')
#print(f'{n} x  3 = {n*3}')
#print(f'{n} x  4 = {n*4}')
#print(f'{n} x  5 = {n*5}')
#print(f'{n} x  6 = {n*6}')
#print(f'{n} x  7 = {n*7}')
#print(f'{n} x  8 = {n*8}')
#print(f'{n} x  9 = {n*9}')
#print(f'{n} x 10 = {n*10}')

#print('\033[7;33m=-=\033[m'*20)

n = int(input('Digite um número para saber sua tabuada: '))
b = 1
for a in range(0, 10, 1):
    print(f'{b} x {n} = {b*n}')
    b += 1


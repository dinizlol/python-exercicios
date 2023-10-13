num = int(input('Digite um número para saber se ele é primo: '))
tot = 0

for c in range(1, num+1):
    if num % c == 0:
        print(f'\033[34m', end=' ')
        tot += 1
    else:
        print(f'\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO número {num} foi divisível {tot} vezes.')
if tot == 2:
    print(f'E por isso ele é primo.')
else:
    print(f'E por isso ele não é primo.')

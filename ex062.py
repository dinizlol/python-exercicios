termo = int(input('Digite um termo: '))
razao = int(input('Digite a razão: '))
mais = 1
aramel = razao
print(f'{termo} ->', end='')
for c in range(10, 1, -1):
    termo += razao
    print(f' {termo} ->', end='')
print(' PAUSA',end='')
while razao != 0:
    razao = int(input('\nQuantos termos a mais você deseja saber? '))
    teste = razao
    while teste > 0:
            termo += aramel
            print(f' {termo} ->' if teste != 0 else ' PAUSA', end='')
            teste -= 1
    print(' PAUSA', end='')
print('\nObrigado por usar esse programa!')

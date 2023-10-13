'''from time import sleep
principal = list()
temp = list()

while True:
    temp.append(str(input('Digite o nome do aluno: ')))
    temp.append(float(input('Nota 1: ')))
    temp.append(float(input('Nota 2: ')))
    r = str(input('Deseja continuar? [S/N] '))
    principal.append(temp[:])
    temp.clear()
    if r in 'Nn':
        break
print('=-' * 30)
print('NºNOME         MÉDIA')
print('-' * 30)

for i, a in enumerate(principal):
    print(f'{i} {a[0]}        {(a[1]+a[2]) / 2}')

while True:
    perg = int(input('De qual aluno gostaria de saber as notas? [999 para interromper]  '))
    if perg == 999:
        print('-=' * 30)
        print('Obrigado por usar este programa!')
        break
    if perg <= len(principal) - 1:
        print(f'As notas de {principal[perg][0]} são: {principal[perg][1]}, {principal[perg][2]}.')
    else:
        print('Opção errada! Digite novamente.')
        sleep(2)'''
from time import sleep
ficha = list()

while True:
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))                  #outra maneira de adicionar a listas
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    r = str(input('Deseja continuar? [S/N] '))
    if r in 'Nn':
        break
print('=-' * 30)
print('Nº Nome        Média')
print('-=' * 30)
for i, a in enumerate(ficha):
    print(f'{i} {a[0]}   {a[2]:.2f}')

while True:
    perg = int(input('De qual aluno deseja saber as notas? [999 para interromper] '))
    if perg == 999:
        print('Obrigado por usar esse programa!')
        break
    if perg > len(ficha):
        print('Opção errada, digite novamente.')
        sleep(3)
    else:
        print(f'As notas de {ficha[perg][0]} são: {ficha[perg][1]}')




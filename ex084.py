lista = list()
temp = list()
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = temp[1]
    elif temp[1] > maior:
        maior = temp[1]
    elif temp[1] < menor:
        menor = temp[1]
    lista.append(temp[:])
    temp.clear()
    r = str(input('Deseja continuar? [S/N]'))
    if r in 'Nn':
        break

print(f'Ao todo, foram cadastrados {len(lista)} pessoas.')
print(f'O maior peso foi de {maior}KG.', end=' ')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print('Foram os mais pesados.')
print(f'O menor peso foi de {menor}KG.', end=' ')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')
print('Foram os mais leves.')


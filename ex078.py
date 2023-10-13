'''num = [1, 4, 6, 7]
#num[2] = 4
num.insert(3, 0)
#num.sort()
num.append(5)
num.pop(0)
print(num)

valores = list()
for cont in range(0, 6):
    valores.append(int(input('Digite um valor: ')))
valores.sort()

for c, v in enumerate(valores):
    print(f'Na posição {c+1} eu encontrei o valor {v}')'''

valores = list()
maior = menor = 0
for a in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {a}: ')))
    if a == 0:
        maior = menor = valores[a]
    else:
        if valores[a] > maior:
            maior = valores[a]
        if valores[a] < menor:
            menor = valores[a]
print(f'Você digitou os valores {valores}')
print(f'O menor valor foi {menor} na posição', end =' ')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')
print()
print(f'O maior valor digitado foi {maior} na posição', end=' ')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')

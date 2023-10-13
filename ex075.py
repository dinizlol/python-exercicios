numeros = tuple(int(input('Digite um número: '))for c in range(0, 4))
print(f'Você digitou os números: {numeros}')
print(f'O número 3 aparece na posição {numeros.index(3)+1}'if 3 in numeros else 'Não foi digitado o valor 3' )
print(f'O número 9 apareceu {numeros.count(9)} vezes.')

print(f'Os números pares são: ', end=' ')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
    else:
        print('Não houve nenhum número par')

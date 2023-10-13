frase = str(input('Digite uma frase para saber se é um palíndromo: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for num in range(len(junto)-1, -1, -1):
    inverso += junto[num]
print(f'O inverso de {junto} é {inverso}.')
if inverso == junto:
    print(f'Temos um palíndromo!')
else:
    print('A frase digitada não é um palindromo!')


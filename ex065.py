cont = soma = num = menor = maior = 0
resposta = 's'
while resposta != 'N':
    num = int(input('Digite um valor: '))
    resposta = input('Deseja continuar? [S/N]').upper()
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
media = soma / cont
print(cont)
print(media)
print(maior)
print(menor)

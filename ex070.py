print('-'*20)
print('LOJA SUPER BARATÃO')
print('-'*20)
soma = caro = conta = baratoo = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preço = int(input('Preço: R$'))
    soma += preço
    conta += 1
    if conta == 1 or preço < preço:
        baratoo = preço
        barato = produto
    if preço > 999:
        caro += 1
    resp = ' '
    while resp not in 'SN':
        resp = input('Deseja continuar? [S/N]').upper().strip()[0]
    if resp == 'N':
        break
print(f'O total da compra foi de: R${soma:.2f}')
print(f'Houveram {caro} produtos acima de R$1000.00')
print(f'O produto mais barato foi o {barato} que custou {baratoo:.2f}')



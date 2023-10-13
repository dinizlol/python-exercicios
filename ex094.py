cadastro = dict()
lista = list()
resposta = 's'
soma = media = 0
while resposta not in 'N':
    cadastro['nome'] = str(input('Digite o nome: '))
    while True:
        cadastro['genero'] = str(input('genero: [H/M]')).upper()
        if cadastro['genero'] not in 'HM':
            print('Por favor, digite apenas H ou M.')
        else:
            break
    cadastro['idade'] = int(input('Idade: '))
    soma += cadastro['idade']
    while True:
        resposta = str(input('Deseja cadastrar outra pessoa? [S/N] ')).upper()
        if resposta not in 'SN':
            print('Por favor, digite apenas S ou N.')
        else:
            break
    lista.append(cadastro.copy())
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
media = soma / len(lista)
print(f'B) A média de idade é de {media:5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in lista:
    if p['genero'] == 'M':
        print(f'{p["nome"]}', end=' ')
print()
print('D) Lista das pessoas com a idade acima da média: ', end='')
for p in lista:
    if p['idade'] >= media:
        print(f'{p["nome"]}', end=' ')


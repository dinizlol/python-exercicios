homem = adultos = nova = 0
while True:
    print('-'*20)
    print('Cadastre uma pessoa')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo: ')).upper().strip()[0]
    if idade > 17:
        adultos += 1
    if sexo == 'H':
        homem += 1
    if sexo == 'M':
        if idade < 18:
            nova += 1
    cont = ' '
    while cont not in 'SN':
        cont = input('Quer cadastrar outra pessoa? [S/N]').upper().strip()[0]
    if cont == 'N': break
print(f'Houveram {homem} Homens, {adultos} adultos e {nova} mulheres abaixo dos 18 anos. ')
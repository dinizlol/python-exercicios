media = 0
velho = 0
mulheres = 0
homemvelho = ''
for a in range(1, 5):
    print(f'------ {a}ª PESSOA ------')
    nome = str(input('nome: '))
    idade = int(input('Idade: '))
    genero = str(input('Sexo[M/F]: ')).upper()
    media = media + idade
    if genero in 'F' and idade < 18:
        mulheres += 1
    if genero == 'M':
        if idade > velho:
            velho = idade
            homemvelho = nome
print(f'A média de idade do grupo é de {media/4} anos.')
print(f'Existem {mulheres} mulheres menor de 18 anos')
print(f'O homem mais velho possui {velho} anos e se chama {homemvelho}.')
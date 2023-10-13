tupla = 'Caramelo', 'Mara', 'Mae', 'Irmao', 'Cachorro', 'Parede'

for a in tupla:
    print(f'\nNa palavra {a} temos as seguintes vogais: ',end='')
    for letra in a:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')


#teste = 'cachorro'

#for letra in teste:
#    print(letra, end='')
#    print(teste)
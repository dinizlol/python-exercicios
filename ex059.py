from time import sleep
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite mais um valor: '))

opção = 0
while opção != 5:
    print('''    [ 1 ] SOMAR
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção = int(input('Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('Calculando...')
        sleep(2)
        print(f'A soma dos dois números é: {soma}')
    elif opção == 2:
        mult = n1 * n2
        print('Calculando...')
        sleep(2)
        print(f'A multiplicação de {n1} e {n2} é: {mult}')
    elif opção == 3:
        print('Calculando...')
        sleep(2)
        if n1 > n2:
            print(f'O maior número é: {n1}')
        elif n2 > n1:
            print(f'O maior número é: {n2}')
        elif n2 == n1:
            print(f'Os dois valores são iguais!')
    elif opção == 4:
        n1 = int(input('Digite um novo valor: '))
        n2 = int(input('Digite o segundo novo valor: '))
    else:
        print('Essa opção está errada. Digite de 1 a 5.')
print('Obrigado por usar esse programa!')


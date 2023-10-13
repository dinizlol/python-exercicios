print('_-|'*20)
print('Sequencia de Fibonnaci')
print('_-|'*20)
sequencia = int(input('Quantos termos você quer saber? '))
cont = 0
t1 = 0
t2 = 1
while cont != sequencia:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    cont += 1
    print(f'{t3} ->', end=' ')
print('FIM!')



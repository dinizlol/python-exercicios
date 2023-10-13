r1 = float(input('Digite o comprimento de uma reta: '))
r2 = float(input('Digite o comprimento de outra reta: '))
r3 = float(input('Digite o comprimento da ultima reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas podem formar um triângulo ', end='')
    if r1 == r2 == r3:
        print('Equilatero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('ISOSCELES')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')

else:
    print('As retas não podem formar um triângulo')




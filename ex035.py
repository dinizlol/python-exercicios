#r1 = float(input('Digite o comprimento de uma reta: '))
#r2 = float(input('Digite o comprimento de outra reta: '))
#r3 = float(input('Digite o comprimento da última reta: '))

#if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
#    print('Os segmentos podem gerar um triangulo!')
#else:
    #print('Os segmentos não podem gerar um triangulo!')

r1 = float(input('Digite o comprimento de uma reta: '))
r2 = float(input('Digite o comprimento de outra reta: '))
r3 = float(input('Digite o comprimento da última reta: '))

if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print('As retas podem formar um triângulo!')
else:
    print('As retas não podem formar um triangulo!')
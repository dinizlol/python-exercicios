#from math import sin, cos, tan, radians
#ângulo = int(input('Digite um ângulo que você deseje: '))
#seno = sin(radians(ângulo))
#print(f'O angulo de {ângulo} tem o SENO de {seno:.2f}')
#cosseno = cos(radians(ângulo))
#print(f'O angulo de {ângulo} tem o COSSENO de {cosseno:.2f}')
#tangente = tan(radians(ângulo))
#print(f'O ângulo de {ângulo} tem a TANGENTE de {tangente:.2f}')

import math
angulo = int(input('Digite um angulo que você deseje: '))
seno = math.sin(math.radians(angulo))
print(f'O angulo de {angulo} possui o seno de: {seno:.2f}')
cosseno = math.cos(math.radians(angulo))
print(f'O angulo de {angulo} possui o cosseno de: {cosseno:.2f}')
tangente = math.tan(math.radians(angulo))
print(f'O angulo de {angulo} possui a tangente de: {tangente:.2f}')



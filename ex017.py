import math
from math import hypot

catop = float(input('Comprimento do cateto oposto:'))
catad = float(input('Comprimento do cateto adjacente: '))

hip = math.hypot(catop, catad)


print(f'A hipotenusa vai medir: {hip:.2f} ')

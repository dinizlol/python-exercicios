from time import sleep
n = int(input('Até qual número deseja saber os pares? '))
for c in range(0, n+2, 2):
    print(c, end=' ')
    sleep(0.5)

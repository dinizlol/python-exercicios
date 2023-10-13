termo = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
contador = 1
#resultado = termo
print(f'{termo} ->', end='')
while contador != 10:
    termo = termo + razao
    contador += 1
    print(f' {termo} ->' if contador < 10 else ' FIM', end='')


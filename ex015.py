dias = int(input('Por quantos dias o carro foi alugado? '))
km = int(input(f'Quantos KMs foram rodados em {dias} dias? '))

calculo = (dias*60) + (km*0.15)

print(f'O valor total a ser pago é de: R${calculo:.2f}')
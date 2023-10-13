#viagem = int(input('Digite a distância da sua viagem: '))
#preço = viagem * 0.50 if viagem <=200 else viagem * 0.45

#print(f'O preço da sua viagem será de: R${preço:.2f}')

viagem = int(input('Digita a distancia que deseja viajar: '))
if viagem <= 200:
    preço = viagem * 0.50
else:
    preço = viagem * 0.45
print(f'Sua viagem custará: R${preço:.2f}!')


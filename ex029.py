#vel = int(input('Qual a velocidade do carro? '))
#if vel > 80:
#    multa = (vel - 80) * 7
#    print(f'MULTADO! Você excedeu o limite permitido que é de 80km/h você deve pagar uma multa de R${multa:.2f} ')
#else:
#    print('Você está dentro da velocidade permitida!')

#print('Tenha um bom dia! Diriga com segurança! :)')


velocidade = int(input('Digite a velocidade do carro em km: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Multado! você estava {velocidade-80}km acima do limite, terá de pagar R${multa:.2f}')
else:
    print('Você está dentro do limite da velocidade, tenha um bom dia!')


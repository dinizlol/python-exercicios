peso = float(input('Digite seu peso em KG: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'Seu IMC é {imc:.1f} e você está abaixo do peso ideal.')
elif 18.5 <= imc < 25:
    print(f'Seu IMC é {imc:.1f} e você está no peso ideal.')
elif 25 <= imc < 30:
    print(f'Seu IMC é {imc:.1f} e você está sobrepeso.')
elif 30 <= imc < 40:
    print(f'Seu IMC é {imc:.1f} e você está obeso.')
elif 40 <= imc:
    print(f'Seu IMC é {imc:.1f} e você está com obesidade mórbida.')

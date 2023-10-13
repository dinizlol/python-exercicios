largura = float(input('Qual a largura da sua parede? '))
altura = float(input('Qual a altura da sua parede? '))
lar_alt = largura*altura
print(f'Sua parede tem a dimensão de {largura}x{altura} e sua área é de {lar_alt}m².')
print(f'Para pintar essa parede, você precisará de {lar_alt/2}L de tinta.')
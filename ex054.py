from datetime import date

maior = 0
menor = 0

for c in range(1, 8):
    ano = int(input(f'Qual ano a {c}º pessoa nasceu? '))
    idade = date.today().year - ano
    if idade > 18:
        maior = maior + 1
    else:
        menor = menor + 1

print(f'Temos {maior} maiores de idade e {menor} menores de idade.')
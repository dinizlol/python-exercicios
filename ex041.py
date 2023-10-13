from datetime import date
ano = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = ano - nascimento
if idade <= 9:
    print(f'O atléta tem {idade} anos. Classificação: MIRIM')
elif idade <= 14:
    print(f'O atléta tem {idade} anos. Classificação: INFANTIL')
elif idade <= 19:
    print(f'O atleta tem {idade} anos. Classificação: JUNIOR')
elif idade <= 25:
    print(f'O atleta tem {idade} anos. Classificação: SÊNIOR')
else:
    print(f'O atleta tem {idade} anos. Classificação: MASTER')
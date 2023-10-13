n1 = float(input('Qual a primeira nota do aluno? '))
n2 = float(input('Qual a segunda nota do aluno? '))

media = (n1+n2) / 2

if media >= 7.0:
    print(f'A sua média é de {media} e você foi aprovado!')
elif media < 5.0:
    print(f'A sua média é de {media} e você foi reprovado!')
elif 7 > media >= 5:
    print(f'Sua média foi de {media} e você está de recuperação')
dicionario = {}

dicionario['aluno'] = str(input('Qual o nome do aluno? '))
dicionario['media'] = float(input('Qual a média do aluno? '))
if dicionario["media"] >= 7:
    dicionario["situação"] = 'Aprovado'
elif dicionario["media"] < 5:
    dicionario["situação"] = 'Reprovado'
elif 5 <= dicionario["media"] < 7:
    dicionario["situação"] = 'Recuperação'

for k, v in dicionario.items():
    print(f'{k} é igual a {v}')

from datetime import datetime
def linha():
    print('-=' * 30)
dados = dict()
dados["nome"] = str(input('Digite seu nome: '))
nasc = int(input('Digite a data de nascimento: '))
dados["idade"] = datetime.now().year - nasc
dados["CTPS"] = int(input('Carteira de trabalho[0 se não tiver]: '))
if dados["CTPS"] != 0:
    dados["ano"] = int(input('Digite o ano que foi contratado: '))
    dados["salario"] = float(input('Salário: '))
    dados["aposentadoria"] = dados['idade'] + ((dados['ano'] + 35) - datetime.now().year)
    linha()
for k, v in dados.items():
    print(f'{k} tem o valor de {v}')



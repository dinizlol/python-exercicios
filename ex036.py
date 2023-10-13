casa = float(input('Qual o valor da casa que deseja financiar? R$'))
salario = float(input('Qual o salário do comprador? R$'))
anos = int(input('Em quantos anos gostaria de pagar? '))
parcela = casa / (anos * 12)
salarioc = salario * 30 /100
print(f'O valor da parcela é de: R${parcela:.2f}')

if salarioc >= parcela:
    print('O emprestimo foi concebido!')
else:
    print('O emprestimo foi negado!')
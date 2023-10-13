#atual = date.today().year
#genero = str(input('Você é homem ou mulher? ')).upper()
#if genero in 'MULHER FEMININO':
#elif genero == 'HOMEM':
#    nascimento = int(input('Digite seu ano de nascimento: '))
#    print(f'Quem nasceu em {nascimento} tem {idade} em {atual}.')
#    if idade == 18:
#        print(f'Esse é o ano que você tem de se alistar!')
#    elif idade > 18:
#        saldo = idade - 18
#        diferença = atual - saldo
#        print(f'Você deveria ter se alistado há {saldo} anos.')
#        print(f'Seu ano de alistamento foi: {diferença}')
#    elif idade < 18:
#        saldo = 18 - idade
#        diferença = saldo + atual
#        print(f'Ainda faltam {saldo} anos para o alistamento.')
#        print(f'Seu alistamento será no ano{diferença}')
#else:
#    print('Essa opção não existe')
from datetime import date
ano = date.today().year
genero = str(input('Você é homem ou mulher? ')).upper()
if genero in 'MULHER FEMININO':
    print('Você não precisa se alistar.')
elif genero in 'HOMEM MASCULINO':
    nascimento = int(input('Qual o seu ano de nascimento? '))
    idade = ano - nascimento
    if idade > 18:
        saldo = idade - 18
        diferença = ano - saldo
        print(f'Você já passou da idade de se alistar, seu ano de alistamento foi {diferença}. ')
    elif idade < 18:
       saldo = 18 - idade
       diferença = ano + saldo
       print(f'Você ainda não pode se alistar, seu ano de alistamento será em {diferença}.')
    elif idade == 18:
       print('Você deve se alistar esse ano!')
else:
  print('Opção errada. Digite seu gênero.')

'''from datetime import date
atual = date.today().year
genero = str(input('Você é homem ou mulher? ')).upper()
if genero == 'MULHER':
    print('Você não precisa se alistar.')
    exit()
nascimento = int(input('Digite seu ano de nascimento: '))
idade = atual - nascimento
print(f'Quem nasceu em {nascimento} tem {idade} em {atual}.')
if idade == 18:
    print(f'Esse é o ano que você tem de se alistar!')
elif idade > 18:
     saldo = idade - 18
     diferença = atual - saldo
     print(f'Você deveria ter se alistado há {saldo} anos.')
     print(f'Seu ano de alistamento foi: {diferença}')
elif idade < 18:
     saldo = 18 - idade
     diferença = saldo + atual
     print(f'Ainda faltam {saldo} anos para o alistamento.')
     print(f'Seu alistamento será no ano {diferença}')'''






























def voto(ano):
    from datetime import datetime
    atual = datetime.today().year
    idade = atual - ano
    if idade < 16:
        return print('Não precisa votar')
    elif 16 <= idade < 18 or idade > 65:
        return print('O voto é opcional')
    else:
        return print('O voto é obrigatório!')





nasc = int(input('Digite o ano de nascimento: '))
voto(nasc)

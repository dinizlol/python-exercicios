from ex115.lib.funções import *
from ex115.arquivo import *
from time import sleep

arquivo = 'cadastros.txt'

if not arquivoExiste(arquivo):
    print('O arquivo existe!')
else:
    print('O arquivo não existe')
    criarArquivo(arquivo)



cabeçalho('SISTEMA')

while True:
    resp = menu(['VER PESSOAS CADASTRADAS', 'CADASTRAR NOVAS PESSOAS', 'SAIR DO SISTEMA'])
    if resp == 1:
        cabeçalho('Opção 1:')
    elif resp == 2:
        cabeçalho('Opção 2:')
    elif resp == 3:
        cabeçalho('Opção 3:')
        break
    else:
        print('Opção inválida. Digite de 1 a 3')
    sleep(2)


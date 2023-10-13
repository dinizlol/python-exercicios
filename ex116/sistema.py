from ex116.lib.funções import *
from ex116.arquivo import *
from time import sleep

arquivo = 'cadastros.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)


cabeçalho('SISTEMA')

while True:
    resp = menu(['VER PESSOAS CADASTRADAS', 'CADASTRAR NOVAS PESSOAS', 'SAIR DO SISTEMA'])
    if resp == 1:
        lerArquivo(arquivo)
    elif resp == 2:
        cabeçalho('CADASTRAR UMA NOVA PESSOA')
        nome = str(input('Nome: '))
        idade = leiaint('Idade:')
        cadastrar(arquivo, nome, idade)
    elif resp == 3:
        cabeçalho('SAINDO DO SISTEMA')
        break
    else:
        print('Opção inválida. Digite de 1 a 3')
    sleep(2)


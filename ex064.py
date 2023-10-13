num = conta = soma = 0
num = int(input('Digite um número para saber sua soma[999 para parar]: '))
while num != 999:
    conta += 1
    soma += num
    num = int(input('Digite um número para saber sua soma[999 para parar]: '))

print(f'A soma dos valores digitados(exceto o 999) é de: {soma}')
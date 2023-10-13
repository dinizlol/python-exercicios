#nome = str(input('Digite seu nome completo : '))
#print('Analisando o seu nome...')

#print(f'Seu nome em letras maiúsculas é: {nome.upper()}')
#print(f'Seu nome em letras minúsculas é: {nome.lower()}')
#print(f'Seu nome possui {len(nome)} letras.')
#separa = nome.split()
#print(f'Seu primeiro nome tem {separa[0]} e possui {len(separa[0])} letras.')


from time import sleep
nome = str(input('Digite seu nome completo: '))
print('Analisando seu nome...')
sleep(1)

print(f'Seu nome em letras maiúsculas é: {nome.upper()}')
print(f'Seu nome em letras minúsculas é: {nome.lower()}')
lista = nome.split()
print(f'Seu primeiro nome é {lista[1]} e possui {len(lista[0])} letras.')

print(lista)
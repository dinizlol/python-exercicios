#nome = str(input('Digite seu nome completo: ')).lower().strip()
#s = 'silva' in nome
#print(f'Seu nome tem silva? {s}')


nome = str(input('Qual é o seu nome? ')).lower().strip()
split = nome.split()
s = "silva" in split

print(f'Seu nome tem silva? {s} ')



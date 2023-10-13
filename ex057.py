p = str(input('Qual seu sexo? [M/F] ')).strip().upper()[0]
while p not in 'FM':
     p = str(input('Resposta errada, digite M ou F: ')).strip().upper()[0]
print(f'Sexo {p} registrado com sucesso.')
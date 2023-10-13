campeonato = 'Botafogo', 'Grêmio', 'Flamengo', 'Palmeiras', 'Fluminense', 'Internacional', 'Bragantino', 'Fortaleza', \
    'Athletico-PR', 'Atlético-MG', 'São Paulo', 'Cruzeiro', 'Santos', 'Bahia', 'Corinthians', 'Cuiabá', 'Goiás',\
    'Vasco', 'Ameriga-MG', 'Coritiba'
print(f'Lista de times do brasileirão: {campeonato}')
print(f'Os 5 primeiros são: {campeonato[0:5]}')
print(f'Os 4 últimos são: {campeonato[-4:]}')
print(f'O São Paulo está na {campeonato.index("São Paulo")+1}ª posição.')
print(f'Os times em ordem alfabética: {sorted(campeonato)}')v

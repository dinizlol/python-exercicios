expr = str(input('Digite uma expressão: '))
lista = list()

for c in expr:
    if c == '(':
        lista.append(c)
    elif c == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão está certa!')
else:
    print('Sua expressão está errada!')
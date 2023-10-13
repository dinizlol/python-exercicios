#nome = str(input('Digite uma frase qualquer ')).lower().strip()
#ount = nome.count('a')
#print(f'A letra A aparece {count} vezes')
#fa = nome.find('a')+1
#print(f'A primeira letra A aparece na posição {nome.find("a")+1}.')
#fr = nome.rfind('a')+1
#print(f'A última letra A aparece na posição {nome.rfind("a")+1}.')

frase = str(input('Digite uma frase: '))

#quantia = frase.count('a')
#primeiro = frase.find('a')
#ultimo = frase.rfind('a')

print(f'A frase digitada possui {frase.count("a")} As, o primeiro A está na posição {frase.find("a")+1}'
      f' e o último está na posição {frase.rfind("a")+1}.')




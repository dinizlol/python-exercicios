#a = int(input('Digite um valor: '))
#b = int(input('Digite outro valor: '))
#c = int(input('digite o último valor: '))

#menor = a
#if b < a and b < c:
#    menor = b
#if c < a and c < b:
#    menor = c

#maior = a
#if b > a and b > c:
#    maior = b
#if c > a and c > b:
#    maior = c

#print(f'O menor valor é: {menor}')
#print(f'O maior valor é: {maior}')

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
n3 = int(input('Digite o último valor: '))

maior = n1

if n2 > n3 and n2 > n1:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

menor = n1
if n2 < n3 and n2 < n1:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

print(f'O número maior é {maior} e o número menor é {menor} ')
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
finally:
    print('Acessado com sucesso')
while True:
    try:
        a = int(input('Numerador: '))
        b = int(input('Denominador: '))
        res = a / b
    except (ValueError, TypeError):
        print('Tivemos um problema com os tipos de dados que vc inseriu.')
    except ZeroDivisionError:
        print('Impossível dividir por zero!')
    except KeyboardInterrupt:
        print('O usuario preferiu não inserir os dados.')
    else:
        print(f'O resultado é {res}')
        break
print('Obrigado por usar nosso programa')



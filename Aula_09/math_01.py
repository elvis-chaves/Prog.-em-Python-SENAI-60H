numero = int(input('Numero : '))


match numero:
    case numero if numero % 2 == 0:
        print('par')
    case _:
        print('nao é par')
import time

def atividade_4 (lista):
    
    for numero in lista:
        numero = numero - 1
        if numero != 0:
            time.sleep(1)
            print(numero)
        else:
            time.sleep(1)
            print('FOGO !!!')
              
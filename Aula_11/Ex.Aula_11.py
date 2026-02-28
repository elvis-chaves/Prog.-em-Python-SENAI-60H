# Peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não seja um número inteiro.

def teste_1 ():

    try:
        n1 = int(input('Insira um número:  '))
    except ValueError :
        print('Não é um numero inteiro !!!')
    finally:
        print('Carregamento concluido')

teste_1()       


# Peça ao usuário para inserir dois números e realize uma operação de divisão. Manipule a exceção caso ocorra um erro na operação  -  ZeroDivisionError.


def teste_2 ():

    try:
        numero1 = int(input('Insira um número:  '))
        numero2 = int(input('Insira um número:  '))
        resul = numero1 / numero2
    except ZeroDivisionError :
        print('Não pode ser divisivel por zero !!!')
    finally:
        print('Carregamento concluido')

teste_2()       

# Crie uma lista e um índice como entrada e retorne o índice. Manipule a exceção caso o índice seja inválido(caso imprima um indice que não exista na lista).

def teste_2 ():

    try:
        lista = [0,1,2]
        print(lista[6])
    except IndexError :
        print('Não existe este indice na lista !!!')
    finally:
        print('Carregamento concluido')

teste_2()       
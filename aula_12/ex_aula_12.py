# Exercícios com funções:
# variáveis locais, globais e parâmetros
# 1
# CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS.
n1 = int(input('Insira um numero: '))
n2 = int(input('Insira um numero: '))

def numeros():
    
    if n1%2 == 0:
        print ('Numero 1 é par')
    else:
        print('Numero 1 é impar')  
    print('E')
    if n2%2 == 0:
        print ('Numero 2 é par')
    else:
        print('Numero 2 é impar')   
    return n1,n2
numeros()


# 2
# CRIE UMA FUNÇÃO PARA MULTIPLICAR 3 NUMEROS.
n_1 = int(input('Insira um numero: '))
n_2 = int(input('Insira um numero: '))
n_3 = int(input('Insira um numero: '))
def mult_3 ():
    print('Resultado da multicação é', n_1 * n_2 * n_3 )
mult_3()

# 3
# CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO.

base = int(input('Numero da base: '))
expoente = int(input('Numero do expoente: '))
def potencia ():
    print (f'resultado da {base} sobre o {expoente} é igaul', base ** expoente)
potencia()
# 4
# CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO DIGITAR, 18 ANOS.

idade = int(input('Coloque sua idade: '))

def mostrar_idade():
    if idade >= 18:
        print('ja pode ser preso')
    else:
        print('Voce ainda é um BB')
mostrar_idade()            
# 5
# DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA.
data_atual = 2026
ano_nasc = int(input('Coloque o seu ano de nascimento: '))

def idade_pessoa():
    idade_da_pessoa = data_atual - ano_nasc
    print (" a idade da pessoa é", idade_da_pessoa)
idade_pessoa()    

# 6
# DESENVOLVA UMA FUNÇÃO PARA VER SE O BRASIL GANHOU A COPA DE 1999.

brasil_campeao = [1958, 1962, 1970, 1994, 2002]
ano_pesquisado = int(input('Insira o ano em que talvez o brasil foi campeao: '))
def campeao ():
    if ano_pesquisado == len(brasil_campeao):
        print ('O Brasil foi campeao da copa')
    else:
        print('O Brasil nao foi campeao')
campeao()

# 7
# DESENVOLVA UM SISTEMA DE RESTAURANTE, ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE SALADA, MACARRONADA, SANDUICHE, SORVETE.
cardapio = ['SALADA', 'MACARRONADA', 'SANDUICHE', 'SORVETE']
# 1 - Função - cumprimentar o cliente
print('Seja bem vindo ao restaurante X')
print('****'* 10)
print('Cardapio')
print()
print(cardapio)
# 2 - Função - restaurante
# 3 - Sugestão utilize listas e loops 
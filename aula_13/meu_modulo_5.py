# Peça ao usuário que insira um número inteiro



def atividade_5(numero):
    soma = 0
    for i in range(2, numero + 1):
        if i % 2 == 0:
            soma += i
            
    return soma            

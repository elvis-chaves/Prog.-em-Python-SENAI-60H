# Casdatro no ecormece

dados = {

    'login':[],
    'senha':[],
        'produtos':{
                    '1': ['Computador Del',5000.0],
                    '2': ['Fone Apple',2000.0],
                    '3': ['Mouse lenovo',250.0],
                    '4': ['Monitor Lenovo', 3000.0]
                    }
}

print('Cadastre-se:')
Cad_login = input('Cadastre seu login:')
Cad_senha = input('Cadastre sua senha: ')
dados['login'].append(Cad_login)
dados['senha'].append(Cad_senha)

# acessar o e-commerce
print('Acessar a aplicação: ')
acesso_login = input('Digite seu login para acessar: ')
acesso_senha = input('Digite seu senha para acessar: ')

if acesso_login == dados['login'][0] and acesso_senha == dados['senha'][0]:
    print('Seja bem vindo(a) ao e-commerce z')
    # verificar a lista de produtos
    print(''' Produtos''')
    produto = input(f'''
        
        {dados['produtos']} - escolha 1 - 2 - 3 - 4 ->>>
    
                    ''')

# comprar um produto
    
    carrinho = []
    valores = []

    carrinho.append(dados['produtos'][produto][0])
    valores.append(dados['produtos'][produto][1])
    print(carrinho[0],valores[0])

# pagamento do produto
    soma = sum(valores)
    print('valor a pagar R$:', soma)
    pag = input('digite a forma de pagamento')
    print('forma de pagmento', pag)
    print('Obrigada volte sempre! ')
else:
    print('Digitação de senha e login incorreta')
    print('tente novamente')

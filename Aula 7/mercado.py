#e-comnerce
#lista de produtos 
#lista de valores
#poder comprar um produto

print('E-COMMERCE')

lista_prod= ['','hd','pen-driver','fone','carregador']
lista_valores = [0,450.0,100.0,350.0,90.0]
carrinho = []
meu_valor = []
print('***'*15)
print(f'''

Produtos:
ID          Produtos            Valor      
{lista_prod.index ('hd')} -             {lista_prod[1]}                 {lista_valores[1]}
{lista_prod.index ('pen-driver')} -     {lista_prod[2]}                 {lista_valores[2]}
{lista_prod.index ('fone')} -           {lista_prod[3]}                 {lista_valores[3]}
{lista_prod.index ('carregador')} -     {lista_prod[4]}                 {lista_valores[4]}
''')
print('***'*15)

produto1 = int(input('Digite o id do produto: '))
produto2 = int(input('Digite o id do produto: '))
produto3 = int(input('Digite o id do produto: '))



carrinho.append(lista_prod[produto1])


carrinho.append(lista_prod[produto2])
carrinho.append(lista_prod[produto3])



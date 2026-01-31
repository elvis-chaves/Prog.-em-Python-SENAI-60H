print('Claculadora')
print()
print('...'*10)
print()
print('NUMEROS SELECIONADOS:')
print()
n1 = float(input('Colocar numero 1: '))
n2 = float(input('Colocar numero 2: '))

result_soma = n1+n2
result_divisao = n1/n2
result_subtracao = n1-n2
result_mult = n1*n2
print()
print('RESULTADOS')

print(f'''
Resultado soma: {result_soma}
Resultado divisao: {result_divisao}
Resultado subtração: {result_subtracao}
Resultado multiplicação: {result_mult}''')
print()
print('RESULTADOS SOMADOS')
print()
soma_total = result_soma + result_divisao + result_subtracao + result_mult
print ('Soma de todos os resultados:', soma_total)

#EXERCÍCIOS 1: 
#Utilize condicionais

#Acessar a Aula - 8

# 1* 
# Peça para o usuário digitar um número, verifique se um número é positivo, 
# negativo ou zero.

numero = int(input('Digite um numero: '))
if numero >= 0:
    print('Numero positivo')
else:
    print('Numero negativo')


# 2*

# Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com 
# base na idade.
idade = int(input('Digite sua idade: '))
if idade >= 16:
    print('pode votar')
else:
    print('nao pode votar')

# 3*

# Declara uma variável com um número qualquer, 
# determine se um número é par ou ímpar.

num = 3
if num % 2 == 0:
    print('numero par')
else:
    print('numero impar')


# 4*

# Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo 
# é equilátero, isósceles ou escaleno

# Um triângulo é chamado de equilátero se todos os lados possuem a mesma medida. 
# Um triângulo é chamado de isósceles se dois lados possuem a mesma medida. 
# Um triângulo é chamado de escaleno se todos os lados possuem medidas diferentes.

numero_1 = float(input('digite seu numero: '))
numero_2 = float(input('digite seu numero: '))
numero_3 = float(input('digite seu numero: '))

if numero_1 == numero_2 and numero_2 == numero_3 and numero_3 == numero_1:
    print ('Equilatero',numero_1,numero_2,numero_3)
elif numero_1 == numero_2 or numero_2 == numero_3 or numero_3 == numero_1:
    print ('isoceles',numero_1,numero_2,numero_3)
elif numero_1 != numero_2 and numero_2 != numero_3 and numero_3 != numero_1:
    print ('escaleno',numero_1,numero_2,numero_3)



# 5*

	# Determine se um número é múltiplo de 5 e 7.

n = int(input('coloque o numero: '))

if n % 5 == 0 and n % 7 == 0:
    print('Numero multiplo')
else:
    print('Não é multiplo')
# 6*

# Verifique se um número é positivo e maior que 10

numero_escolhido = int(input('Coloque seu numero: '))
if numero_escolhido >= 10 and numero_escolhido >=0:
    print('Numero correto')
else:
    print('Numero incorreto')

# 7*

# Verifique se um número é divisível por 3 ou 5.

numero_test = int(input('Coloque seu numero: '))
if numero_test % 3 == 0 or numero_test % 5 == 0:
    print('Numero Divisivel')
else:
    print('Nao Divisivel')
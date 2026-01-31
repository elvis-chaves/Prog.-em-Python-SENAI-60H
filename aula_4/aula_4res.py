## ATIVIDADES:


### 1 - Crie um programa para efetuar a leitura de um número inteiro e apresentar o resultado do quadrado deste número.


numero =  10
print(numero ** 2)


### 2 - Crie duas variáveis para armazenar seu primeiro nome e sobrenome. Em seguida, concatene-as para formar seu nome completo e exiba o resultado.


nome, sobrenome =  'Lucas', 'Almeida'


nome = 'Kaue'
sobrenome = 'Santos'


print(nome, sobrenome)


# Concatenações: 
print(nome + ' ' +sobrenome)
print('{} {}'.format(nome, sobrenome))
print('%s %s'%(nome, sobrenome))
print(f'{nome} {sobrenome}')





### 3 - Peça ao usuário para digitar dois números inteiros e armazene-os em variáveis. Realize a concatenação desses números como strings e exiba o resultado.


n1  =  int(input('numero: '))
n2  =  int(input('numero: '))


print('{} {}'.format(n1, n2))


### 4 - Crie uma variável para armazenar a palavra "Python". Em seguida, adicione um número inteiro ao final da palavra usando a concatenação e exiba o resultado.
palavra  =  'Python'
n  =  5
print(palavra, n)


### 5 - Declare uma variável contendo uma frase. Em seguida, peça ao usuário para digitar uma palavra e concatene essa palavra no final da frase. Exiba o resultado.


frase  =  'seja bem vindo(a)'
nome  = input('Digite sue nome:  ')


print(frase, nome)
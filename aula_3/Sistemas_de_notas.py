print('Sistemas de notas')
print('...' * 10)

nome_aluno = input('Nome do Aluno: ')

n1_port = float(input('Nota Portugues: '))
n2_mat = float(input('Nota Matemática: '))
n3_ing = float(input('Nota Ingles: '))

media = (n1_port + n2_mat + n3_ing)/3
print()
print('...' * 10)
print('SITUAÇÃO DO ALUNO: ')
print()

aprovado = media >= 7
reprovado = media < 5
recuperacao = media >=5 and media <7

print(nome_aluno,'Aprovado', aprovado)
print(nome_aluno,'Reprovado', reprovado)
print(nome_aluno,'Recuperação', recuperacao)

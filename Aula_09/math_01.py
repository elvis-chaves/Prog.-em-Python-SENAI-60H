numero = int(input("insira o numero: "))

match numero:
    case numero if numero == 0:
        print('Numero é igual zero')
    case numero if numero < 0:
        print('Numero é negativo')
    case numero if numero > 0:
        print('Numero positivo')

text = ''
text = input('Digite seu texte: ')

match text:
    case '':
        print('Astring é vazia')
    case _:
        print('A string nao é vazia')

numero_ = int(input("insira o numero: "))

match numero:
    case numero_ if numero_ == 10:
        print('Numero é igual 10')
    case numero_ if numero_ < 10:
        print('Numero é menor que 10')
    case numero_ if numero_ > 10:
        print('Numero é maior que 10')

idade = int(input('Coloque sua idade: '))

match idade :
    case x if x <= 12 :
        print("Criança")
    case x if x > 12 and x <= 17:
        print("Adolescente")
    case x if x > 17 and x <= 35 :
        print("Jovem")
    case x if x > 35 and x <= 64:
        print("Adulto")
    case x if x > 64:
        print("idoso")
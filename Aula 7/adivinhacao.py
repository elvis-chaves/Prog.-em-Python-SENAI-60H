import random

aleatorio = random.randint(1,10)
chute = int(input('Chute um numero: '))

if aleatorio == chute:
    print('👌 acertei')
    print('O numero é: ',aleatorio)
else:
    print('😒 deu ruim')
    print('O numero é: ',aleatorio)
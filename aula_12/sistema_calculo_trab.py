# verificar a valor_hora

from teste import hora_extra_receber


def verificar_valor_hora (carga, salario):
    return salario / carga

# verificar quantidade de horas extras
def quantidade_extra(valor_extra, valor_hora):
    return valor_extra * valor_hora

# calculo do valor da hora extra
def quantidade_extra(quantidade, hora_extra):
    return quantidade * hora_extra

# somar com o salario
def salario_bruto (salario, hora_extra_receber):
    return salario + hora_extra_receber

# verificar os descontos  vt, vr
def desconto (salario_bruto, vt, vr):
    salario_bruto - (vt+vr)
    return

# liquido e o bruto
def salario_liquido(salario_receber):
    return salario_receber


def sistema_rh():
    while True:
        salario = float(input('Salario R$: '))
        carga = 220
        print('Verifique o salario a receber: ')
        valor_hora = verificar_valor_hora(carga, salario)
        print('Valor hora R$ ', round(valor_hora,2))
        print("***"*10)
        extra_50 = quantidade_extra(1.5, valor_hora)
        extra_100 = quantidade_extra(2,0, valor_hora)
        print('Extra 50%', round(extra_50,2))
        print('Extra 100%', round(extra_100,2))
        print("***"*10)
        quantidade_50 = float(input('quantidade de extra 50%: '))
        quantidade_100 = float(input('quantidade de extra 100%: '))
        hora_receber_50 = hora_extra_receber(quantidade_50,extra_50)
        hora_receber_100 = hora_extra_receber(quantidade_100,extra_50)

        print(f'''
            hora extra 50% - R${hora_receber_50}
            hora extra 100% - R${hora_receber_100}

        ''')
        print("***"*10)
        hora_extra_total = hora_receber_50 + hora_receber_100
        salario_b = salario_bruto(salario, hora_extra_total)
        print('Salario Bruto: R$ ', salario_b)

        print('Descontos: ')

        salario_liquidoo = desconto(salario_b,1000.0,750.0)
        print ('Salario a receber', salario_liquidoo)

sistema_rh()
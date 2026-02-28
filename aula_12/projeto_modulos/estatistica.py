import statistics


lista = [1,2,3,4,5,6,7,8,9]


def cal_da_media ():
    media = statistics.mean(lista) 
    return media
cal_da_media() 



def cal_da_mediana():
    mediana = statistics.median(lista)
    return mediana
cal_da_mediana

def cal_desv_padra():
    des_padra = statistics.stdev(lista)
    return des_padra
cal_desv_padra()
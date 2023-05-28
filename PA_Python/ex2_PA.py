from functools import reduce

def passar_de_numero(lista):
    return reduce(lambda x,y:x*10+y,lista)

print(passar_de_numero([1,2,3,4]))

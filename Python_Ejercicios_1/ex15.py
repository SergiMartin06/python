def sumar_llista (a):
    sumatori=0
    for i in a:
        sumatori+=i
    return sumatori


def multiplicar_llista(lista):
    multiplicado=1
    for x in lista:
        multiplicado*=x
    return multiplicado

#Programa principal

x= [1,3,4,5,7]
print("El sumatori és: " ,sumar_llista(x))

x= [1,3,4,5,7]
print("El multiplicador és: " ,multiplicar_llista(x))


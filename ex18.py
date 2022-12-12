def superposicion(a,b):
    n=0
    for e in a:
        n+=b.count(e)
    if n>0:
        return [n, True]
    else:
        return [0, False]

a=input("Introduzca la primera lista de elementos como un string, sin espacios: ")
b=input("Introduzca la segunda lista de elementos como un string, sin espaciios: ")
c,d= superposicion(a,b)
if (c==0):
    print("Las listas no tienen ningun elemento en comun")
else:
    print("Las listas tienen en comun" ,c, "elementos")
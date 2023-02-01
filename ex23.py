def paraula_mes_llarga (a):
    b=list()
    i=0
    for e in a:
        b[i] = len (e)
        i+=1
    
    b.sort()
    return b [::-1]

x= ["Hola","adeu","si","matematiques"]
e= paraula_mes_llarga (x)
print ("LA paraula mes llarag es: ", e[0])

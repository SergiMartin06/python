def invertir(a):
    b=list(a)
    c=b[::-1]
    r= " ".join(c)
    return r

b=input("Introduzca una palabra: ")
c=invertir(b)
print("La palabra" ,b, " si la giras es" ,c)
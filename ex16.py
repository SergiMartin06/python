def invertir(s):
    
    llista=list(s)
    a = llista[::-1]
    return a

s = ("Soc del Ramis")
b = invertir (s)
for i in b:
    print (i)

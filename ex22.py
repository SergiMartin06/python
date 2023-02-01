def gran_llista (a):
    
    a.sort (reversed)
    return a[:-1]

#Programa

a= [1,4,6,10,30]
c= gran_llista (a)

print(c(0))

def index_paraula(llista, paraula):
    low = 0
    high = len(llista) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if llista[mid] < paraula:
            low = mid + 1
        elif llista[mid] > paraula:
            high = mid - 1
        else:
            return mid
    
    return -1

l=["mono", "moto", "aula" ]
indice=index_paraula(l,"aula" )
print (indice)
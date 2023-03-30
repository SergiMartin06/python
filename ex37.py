def llegir_nombre():
    return(int(input("Introdueix un valor: ")))

def escriure_serie(a):
    suma=0
    for i in range (a,1,-4):
        suma+=i*2
    print("La suma dels quadrats separats entre si a {} es {}" .format(a,suma))

a=llegir_nombre()
escriure_serie(a)
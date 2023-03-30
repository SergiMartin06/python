def leer_palabra():
    return(input("Introdueix una paraula: "))

def comparar_paraula():
    if a==b:
        print("Son iguals, per tant rimen.")
    elif a[-3:]==b[-3:]: 
        print("Rimen, pq les 3 darreres lletres son iguals")
    elif a[-2:]==b[-2:]:
        print("Rimen un poc, pq les dues darreres lletres son iguals")
    elif a[-1:]==b[-1:]
        print("Rimen molt poc prque la darrere lletre es igauñ")
    else:
        print("No rimen")
a=leer_palabra()
b=leer_palabra()
comparar_paraula(a,b)
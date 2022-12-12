def crear_repetido(a,b):
        c = int(a)*b
        return c

def crear_puntos(a):
    for e in a:
        c=crear_repetido(int(e),'.')
        print(c)

a=input("Escribe una lista numerica de elementos: ")
crear_puntos(a)
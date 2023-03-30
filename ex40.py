def llegir_numero():
    return(int(input("Introdueix un nombre: ")))


def taula_multiplicar(a):
    for i in range(21):
        print("{} x {} = {}".format(i,a,i*a))


a=llegir_numero()
taula_multiplicar(a)


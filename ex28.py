def llegir():
    llista=[]
    a='a'
    while(a!='.'):
        a=input("Introdueix un numero: ")
        if a!='.':
            llista.append(int(a))
    return tuple(llista)

def mostrar_majors_que(a,num):
    for e in a:
        if e>num:
            print(e)

#PP
x=llegir()
i=input("Introdueix un numero que vols comparar: ")
mostrar_majors_que(x,int(i))
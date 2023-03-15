def llegir():
    llista=[]
    a='a'
    while(a!='.'):
        a=input("Introdueix un numero: ")
        if a!='.':
            llista.append(a)
    return llista

def nums_que_comencen_per(l, c):
    p=[]
    x=0
    for e in l:
        if e[0]==c:
            x+=1
            p.append(e)
    print ("El numero de paraules que comencen {} son {} i son {} ".format (c,x,p))

#PP
a=llegir()
c=input("Introduce el caracter que desea buscar: ")
nums_que_comencen_per(a,c)

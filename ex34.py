import random

def Calcular_random(j):
    b=[]
    for i in range (4):
        b.append(random.randint(0.9))
    return

def leer():
    a=[]
    for i in range (4):
        b.append(int(input("Intro num: ")))
    return b

def comparar(a,b):
    a,b=0
    for i in range (4):
        if a[i]==b[i]:
            a+=1
        elif b[i] in a:
            b+=1
        else:
            c+=1
    if a ==4:
        print("")
        return 1
    elif a>0 and y>0:
        print("")
        return 0
    elif a==0 and y>0:
        print("")
        return 0
    elif a>0 and y==0:
        print("")
        return 0
    else:
        print("")
        return 0



a=Calcular_random()
sortir=0
while sortir!=1:
    b=leer()
    if comparar(a,b) ==1:
        sortir=1
    else:
        sortir=0

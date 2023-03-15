def lista(a):
    l=[]
    x="a"
    while x!=".":
        x=input()
        if x!='.':
            l.append(int(x))
    return l

e=lista()
print (e)
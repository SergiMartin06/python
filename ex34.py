def random(j):
    import random
    for i in range(1):
        random.uniform(1000, 9999)

x=[1,9,2,3]

a=int(input("Introduce una cifra: "))
if a==x[0]:
    print("Has adivinado la primera cifra. ")
else:
    print("No es esa cifra.")

b= input("Introduce otra cifra: ")
if a==x[1]:
    print("Has adivinado la primera cifra. ")
else:
    print("No es esa cifra.")
c= input("Introduce otra cifra: ")
if a==x[2]:
    print("Has adivinado la primera cifra. ")
else:
    print("No es esa cifra.")
d= input("Introduce una ultima cifra: ")
if a==x[3]:
    print("Has adivinado la primera cifra. ")
else:
    print("No es esa cifra.")
def gran (z, e):
    a=e

    if (z>e):
        print(z,"es mayor que " ,e)

        a=z
    elif(e>z):
        print(e, "es mayor que " ,z)

    else:
        print(e, "y" ,z," son lo mismo")
    return a

a=int(input("Numero1: "))

b=int(input("Numero2: "))

c=gran(a,b)

print("El mas grande cuesta:" ,c)


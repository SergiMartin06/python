def caracter (x):
    vocales= ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
    if x in vocales:
        return True
    else:
        return False 


x=input("Introduce un caracter: ")
caracter (x)


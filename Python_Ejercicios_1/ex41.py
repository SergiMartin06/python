def sumar_digitos(a):
    suma=0
    for i in str(a):
        i+=str(a)
    return suma

numero=int(input("Pon un numero: "))
suma=sumar_digitos(numero)

if suma%2==0:
    print ("Es par")
else:
    print("Es impar")
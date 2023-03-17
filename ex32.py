def any (any):
    if any%4==0 and any%100>0 and any%400==0:
        print ("Es un any de traspas")
    else: 
        print("{} no es un any de traspas".format(any))

#PP

a=input("Indica un any: ")
any (int(a))
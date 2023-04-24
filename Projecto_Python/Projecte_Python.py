import random


def menu ():
    print("""
    
    1. Funcio amb llistes i nombres aleatoris
    2. 2a opcio
    3. 3a opcio
    4. 4a opcio
    0. Salir

    """)
    
    a=int(input("Selecciona una opcio: "))
    return a


def Llistes_NombresAleatoris():
    l=("Mapa" , "Catalejo", "Chancla", "Guante", "Cuchillo")
    objeto= l(random.randint(1,6))
    print("Te ataca una manada de lobos, para sobrevivir tendras que sacar un objeto de tu mochila para poder hacer algo.")
    if objeto == "Mapa":
        print("Gracias al mapa, escapas por una ruta.")
    elif objeto == "Catalejo":
        print("Debido al catalejo,")
    elif objeto == "Chancla":
        print("Al golpear a un lobo con la chancla, te muerde y acabas muerto")
    elif objeto == "Guante":
        print("Te pones el guante y los lobos se van porque si")
    elif objeto == "Cuchillo":
        print("Sobrevives")




a=1
while a!=0:
    if a!=0:
        a=menu()
        match a:
            case "1":
                Llistes_NombresAleatoris

            
      

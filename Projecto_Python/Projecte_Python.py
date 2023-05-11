import random
import os


def menu():
    print("""
    
    1. Funcio amb llistes i nombres aleatoris
    2. 2a opcio
    3. 3a opcio
    4. 4a opcio
    0. Salir

    """)
    
    a = int(input("Selecciona una opcion: "))
    return a

def Llistes_NombresAleatoris():
    l = ["Mapa", "Catalejo", "Chancla", "Guante", "Cuchillo"]
    objeto = l[random.randint(0, 4)]
    print("Te ataca una manada de lobos, para sobrevivir tendrás que sacar un objeto de tu mochila para poder hacer algo.")
    if objeto == "Mapa":
        print("Gracias al mapa, escapas por una ruta.")
    elif objeto == "Catalejo":
        print("Debido al catalejo, ...")
    elif objeto == "Chancla":
        print("Al golpear a un lobo con la chancla, te muerde y acabas muerto")
    elif objeto == "Guante":
        print("Te pones el guante y los lobos se van porque sí")
    elif objeto == "Cuchillo":
        print("Sobrevives")

def agenda():
    with open("/home/cicles/archivo.txt", "w") as f:
        f.read
        f.write("")
        f.close





a = 1
while a != 0:
    a = menu()
    match a:
        case 1:
            print("Has escogido la opcion 1")
            primera_funcion=Llistes_NombresAleatoris()
        
        case 2:
            print ("Has escogido la 2 opcion")
            segunda_funcion=agenda()
        
        case other:
            print("Opcion no valida")

        

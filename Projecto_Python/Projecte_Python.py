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
    if a == 1:
        Llistes_NombresAleatoris()
    elif a == 2:
        agenda()
    elif a == 3:
        juego()
    elif a == 4:
        print("Opción 4 seleccionada")
    elif a == 0:
        print("Saliendo del programa...")
    else:
        print("Opción inválida, intenta de nuevo")

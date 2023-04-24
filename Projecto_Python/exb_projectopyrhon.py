import random

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
        print("Te pones el guante ylos lobos se van porque si")
    elif objeto == "Cuchillo":
        print("Sobrevives")



Llistes_NombresAleatoris
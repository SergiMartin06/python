import random


def menu ():
    print("""
    
    1. 1a opcio
    2. 2a opcio
    3. 3a opcio
    4. 4a opcio
    
    """)

    a=int(input("Selecciona una opcio: "))
    return a

def Llistes_NombresAleatoris():



def Fitxers():


def Joc():


def Treball_Objectes():


def Llibreria():


def Aplicacio_de_serveis():  



a="1"
while a!="0":
    a=menu
    match a:
        case "1":
            a=Llistes_NombresAleatoris
        case "2":
            a=Fitxers 
        case "3":
            a=Joc
        case "4":
            a=Treball_Objectes
        case "5":
            a=Llibreria
        case "6":
            a=Aplicacio_de_serveis
        case other:
            print("No es una opcio.")

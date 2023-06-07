import random
import os
import tkinter

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


def menu_agenda():
    print("""
    
    1. Añadir elementos en la lista
    
    2. Ver la lista
    
    
    """)

    a=input("Escoge una opcion: ")
    return a



def agenda1():
    segunda_funcion="Agenda"
    a=0
    while a!=".":
        if a!=".":
            with open("/home/Cicles/archivo.txt", "a") as f:
                a=input("Añade tus planes: ")
                f.write(a+"\n")
                f.read()
          




AHORCADO = ['''
    +---+
    |   |
        |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\  |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\  |
    /    |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\  |
    / \  |
        |
    =========''']

palabras = 'valoracion aprenderpython comida juego python web imposible variable curso volador cabeza reproductor mirada escritor billete lapicero celular valor revista gratuito disco voleibol anillo estrella'.split()
 
def buscarPalabraAleat(listaPalabras):
    # Esta funcion retorna una palabra aleatoria.
    palabraAleatoria = random.randint(0, len(listaPalabras) - 1)
    return listaPalabras[palabraAleatoria]
 
def displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta):
    print(AHORCADO[len(letraIncorrecta)])
    print ("")
    fin = " "
    print ('Letras incorrectas:', fin)
    for letra in letraIncorrecta:
        print (letra, fin)
    print ("")
    espacio = '_' * len(palabraSecreta)
    for i in range(len(palabraSecreta)): # Remplaza los espacios en blanco por la letra bien escrita
        if palabraSecreta[i] in letraCorrecta:
            espacio = espacio[:i] + palabraSecreta[i] + espacio[i+1:]
    for letra in espacio: # Mostrará la palabra secreta con espacios entre letras
        print (letra, fin)
    print ("")
 
def elijeLetra(algunaLetra):
    # Devuelve la letra que el jugador ingreso. Esta función hace que el jugador ingrese una letra y no cualquier otra cosa
    while True:
        print ('Adivina una letra:')
        letra = input()
        letra = letra.lower()
        if len(letra) != 1:
            print ('Introduce una sola letra.') 
        elif letra in algunaLetra:
            print ('Ya has elegido esa letra ¿Qué tal si pruebas con otra?')
        elif letra not in 'abcdefghijklmnopqrstuvwxyz':
            print ('Elije una letra.')
        else:
            return letra
 
def empezar():
    # Esta funcion devuelve True si el jugador quiere volver a jugar, de lo contrario devuelve False
    print ('Quieres jugar de nuevo? (Si o No)')
    return input().lower().startswith('s')


def juego_a():
    print ('A H O R C A D O')
    letraIncorrecta = ""
    letraCorrecta = ""
    palabraSecreta = buscarPalabraAleat(palabras)
    finJuego = False
    while True:
        displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta)
        # El usuairo elije una letra.
        letra = elijeLetra(letraIncorrecta + letraCorrecta)
        if letra in palabraSecreta:
            letraCorrecta = letraCorrecta + letra
            # Se fija si el jugador ganó
            letrasEncontradas = True
            for i in range(len(palabraSecreta)):
                if palabraSecreta[i] not in letraCorrecta:
                    letrasEncontradas = False
                    break
            if letrasEncontradas:
                print ('¡Muy bien! La palabra secreta es "' + palabraSecreta + '"! ¡Has ganado!')
                finJuego = True
        else:
            letraIncorrecta = letraIncorrecta + letra
            # Comprueba la cantidad de letras que ha ingresado el jugador y si perdió
            if len(letraIncorrecta) == len(AHORCADO) - 1:
                displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta)
                print ('¡Se ha quedado sin letras!\nDespues de ' + str(len(letraIncorrecta)) + ' letras erroneas y ' + str(len(letraCorrecta)) + ' letras correctas, la palabra era "' + palabraSecreta + '"')
                finJuego = True
        # Pregunta al jugador si quiere jugar de nuevo
        if finJuego:
            if empezar():
                letraIncorrecta = ""
                letraCorrecta = ""
                finJuego = False
                palabraSecreta = buscarPalabraAleat(palabras)
            else:
                break






a = 1
while a != 0:
    a = menu()
    match a:
        case 1:
            print("Has escogido la opcion 1")
            primera_funcion=Llistes_NombresAleatoris()
        
        case 2:
            print ("Has escogido la 2 opcion")
            segunda_funcion=agenda1()
        
        case 3:
            print("Has escogido la opcion 3")
            caca=juego_a()

        case 4:
            print("Has escogido la opcion 4")

        case other:
            print("Opcion no valida")

        

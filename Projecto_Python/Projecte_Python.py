import random
import os
import tkinter as tk
import webbrowser
import requests


#Menu Principal

def menu():
    print("""
    
        Menu Projecte Python

    1. Funcio amb llistes i nombres aleatoris
    2. Agenda
    3. Juego - Ahorcado
    4. Ventana - Boton a Google
    5. Chistes API
    0. Salir

    """)
    
    a = int(input("Selecciona una opcion: "))
    return a


#Funcion lista aleatorias

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


#Funciones sobre agenda

def mostrar_menu_agenda():
    print("""
    
            Agenda - Menú:


    1. Agregar contacto
    2. Buscar contacto
    3. Editar contacto
    4. Eliminar contacto
    0. Salir
    
    """)

def agregar_contacto():
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")

    with open("agenda.txt", "a") as archivo:
        archivo.write(f"{nombre},{telefono},{email}\n")

    print("Contacto agregado correctamente.")

def buscar_contacto():
    nombre_buscar = input("Ingrese el nombre del contacto a buscar: ")

    with open("agenda.txt", "r") as archivo:
        contactos = archivo.readlines()

    encontrado = False
    for contacto in contactos:
        nombre, telefono, email = contacto.strip().split(",")
        if nombre.lower() == nombre_buscar.lower():
            print("Contacto encontrado:")
            print(f"Nombre: {nombre}")
            print(f"Teléfono: {telefono}")
            print(f"Email: {email}")
            encontrado = True
            break

    if not encontrado:
        print("Contacto no encontrado.")

def editar_contacto():
    nombre_editar = input("Ingrese el nombre del contacto a editar: ")

    with open("agenda.txt", "r") as archivo:
        contactos = archivo.readlines()

    encontrado = False
    nuevos_contactos = []
    for contacto in contactos:
        nombre, telefono, email = contacto.strip().split(",")
        if nombre.lower() == nombre_editar.lower():
            nuevo_nombre = input(f"Nuevo nombre ({nombre}): ")
            nuevo_telefono = input(f"Nuevo teléfono ({telefono}): ")
            nuevo_email = input(f"Nuevo email ({email}): ")
            nuevos_contactos.append(f"{nuevo_nombre},{nuevo_telefono},{nuevo_email}\n")
            print("Contacto editado correctamente.")
            encontrado = True
        else:
            nuevos_contactos.append(contacto)

    if not encontrado:
        print("Contacto no encontrado.")

    with open("agenda.txt", "w") as archivo:
        archivo.writelines(nuevos_contactos)

def eliminar_contacto():
    nombre_eliminar = input("Ingrese el nombre del contacto a eliminar: ")

    with open("agenda.txt", "r") as archivo:
        contactos = archivo.readlines()

    encontrado = False
    nuevos_contactos = []
    for contacto in contactos:
        nombre, telefono, email = contacto.strip().split(",")
        if nombre.lower() == nombre_eliminar.lower():
            print("Contacto eliminado correctamente.")
            encontrado = True
        else:
            nuevos_contactos.append(contacto)

    if not encontrado:
        print("Contacto no encontrado.")

    with open("agenda.txt", "w") as archivo:
        archivo.writelines(nuevos_contactos)


#Funciones sobre la ventana

def abrir_google():
    webbrowser.open("https://www.google.com")

def ventana():
    try: 
        ventana = tk.Tk()
        ventana.title("Programa con Menú (Google)")
        menu = tk.Menu(ventana)
        
        
        boton_enviar = tk.Button(ventana, text="Entrar en google", command=abrir_google)
        boton_enviar.grid(row=5, column=0)

        ventana.config(menu=menu)

        ventana.mainloop()

    except:
        ModuleNotFoundError


#Funciones Ahorcado

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

palabras = "serfi", "sergio", "python", "epi".split()
 
def buscarPalabraAleat(listaPalabras):
    palabraAleatoria = random.randint(0, len(listaPalabras))
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
    for i in range(len(palabraSecreta)):
        if palabraSecreta[i] in letraCorrecta:
            espacio = espacio[:i] + palabraSecreta[i] + espacio[i+1:]
    for letra in espacio: 
        print (letra, fin)
    print ("")
 
def elijeLetra(algunaLetra):
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
        letra = elijeLetra(letraIncorrecta + letraCorrecta)
        if letra in palabraSecreta:
            letraCorrecta = letraCorrecta + letra
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
            if len(letraIncorrecta) == len(AHORCADO) - 1:
                displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta)
                print ('¡Se ha quedado sin letras!\nDespues de ' + str(len(letraIncorrecta)) + ' letras erroneas y ' + str(len(letraCorrecta)) + ' letras correctas, la palabra era "' + palabraSecreta + '"')
                finJuego = True

        if finJuego:
            if empezar():
                letraIncorrecta = ""
                letraCorrecta = ""
                finJuego = False
                palabraSecreta = buscarPalabraAleat(palabras)
            else:
                break



#Funciones de API

def chistes():
    url = "https://api.chucknorris.io/jokes/random"
    respuesta = requests.get(url)
    datos = respuesta.json()
    
    chiste = datos["value"]
    print(chiste)



#PP

a = 1
while a != 0:
    a = menu()
    match a:
        case 1:
            print("Has escogido la opcion 1")
            primera_funcion=Llistes_NombresAleatoris()
        
        case 2:
            print ("Has escogido la 2 opcion")
            segunda_funcion=mostrar_menu_agenda()
            a=0
            while a!="1":
                opcion=int(input("Selecciona una opcion: "))
                
                match opcion:

                    case 1:
                        agregar_contacto()

                    case 2:
                        buscar_contacto()

                    case 3:
                        editar_contacto()

                    case 4:
                        eliminar_contacto()

                    case 0:
                        print("Adios!")
                        a="1"
                    
                    case other:
                        print("Pon una opcion correcta")
        
        case 3:
            print("Has escogido la opcion 3")
            caca=juego_a()

        case 4:
            print("Has escogido la opcion 4")
            aa=ventana()

        case 5:
            print("Has escogido la primera opcion")
            bb=chistes()

        case 0:
            print("Nos vemos")
            a=0

        case other:
            print("Opcion no valida")
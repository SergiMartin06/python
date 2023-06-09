import os


def mostrar_menu():
    print("""
    
            Agenda - Menú:


    1. Agregar contacto
    2. Buscar contacto
    3. Editar contacto
    4. Eliminar contacto
    5. Salir
    
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


#PP

a=0
while a!="1":
    mostrar_menu()
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

        case 5:
            print("Adios!")
            a="1"
        
        case other:
            print("Pon una opcion correcta")
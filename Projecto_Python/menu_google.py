import tkinter as tk
import webbrowser

def abrir_google():
    webbrowser.open("https://www.google.com")

ventana = tk.Tk()
ventana.title("Programa con Menú")

menu = tk.Menu(ventana)

archivo_menu = tk.Menu(menu, tearoff=0)
archivo_menu.add_command(label="Abrir", command=abrir_google)
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir", command=ventana.quit)

menu.add_cascade(label="Archivo", menu=archivo_menu)

ventana.config(menu=menu)

ventana.mainloop()

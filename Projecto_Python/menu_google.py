import tkinter as tk
import webbrowser

def abrir_google():
    webbrowser.open("https://www.google.com")

ventana = tk.Tk()
ventana.title("Programa con Menú (Google)")
menu = tk.Menu(ventana)


boton_enviar = tk.Button(ventana, text="Enviar", command=abrir_google)
boton_enviar.grid(row=5, column=0)


ventana.config(menu=menu)

ventana.mainloop()

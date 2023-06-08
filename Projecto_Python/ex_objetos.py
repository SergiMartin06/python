import tkinter as tk
import webbrowser


def google():
	webbrowser.open("https://www.google.com")


ventana = tk.Tk()
ventana.title("Programa con menu")


def enviar_datos():
	print("Opcio:", opcio.get())


tk.Label(ventana, text="1. Calculadora").grid(row=0, columnspan=2)
tk.Label(ventana, text="2. Llistes").grid(row=2, columnspan=2)
tk.Label(ventana, text="Elegeix l'opció adient").grid(row=4, column=0)
opcio=tk.Entry(ventana).grid(row=4,column=1)


boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_datos)
boton_enviar.grid(row=5, column=0)
boto_tancar =tk.Button(ventana, text="Tancar", command=ventana.destroy)
boto_tancar.grid(row=5, column=1)

if tk.Entry==1:
	google
ventana.mainloop()










import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()

# Definir la función que se ejecutará cuando se haga clic en el botón
def enviar_datos():
	print("Opcio:", opcio.get())

# Crear los widgets del formulario
tk.Label(ventana, text="1. Calculadora").grid(row=0, columnspan=2)
tk.Label(ventana, text="2. Llistes").grid(row=1, column=0)
tk.Label(ventana, text="3. POO").grid(row=2, column=0)
tk.Label(ventana, text="4. Fitxers").grid(row=3, column=0)
tk.Label(ventana, text="Elegeix l'opció adient").grid(row=4, column=0)
opcio=tk.Entry(ventana)
opcio.grid(row=4,column=1)

# O opcio=tk.Entry(ventana).grid(row=4,column=1)

boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_datos)
boton_enviar.grid(row=5, column=0)
boto_tancar =tk.Button(ventana, text="Tancar", command=ventana.destroy)
boto_tancar.grid(row=5, column=1)
# Mostrar la ventana
ventana.mainloop()

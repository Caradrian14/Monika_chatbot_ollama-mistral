import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi Aplicación")

# Añadir una etiqueta
etiqueta = tk.Label(ventana, text="¡Hola, Tkinter!")
etiqueta.pack()

# Añadir un botón
def saludar():
    print("¡Hola! Has hecho clic en el botón.")

boton = tk.Button(ventana, text="Haz clic aquí", command=saludar)
boton.pack()

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
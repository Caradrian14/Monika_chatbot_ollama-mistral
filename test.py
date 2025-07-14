import tkinter as tk
from tkinter import ttk

def enviar_mensaje():
    mensaje = entrada.get()
    if mensaje:
        chat.config(state=tk.NORMAL)
        chat.insert(tk.END, "Tú: " + mensaje + "\n")
        chat.config(state=tk.DISABLED)
        entrada.delete(0, tk.END)
        # Aquí podrías añadir la lógica para obtener una respuesta y mostrarla en el chat
        # Por ejemplo, una respuesta automática:
        respuesta = "Bot: " + mensaje + "\n"
        chat.config(state=tk.NORMAL)
        chat.insert(tk.END, respuesta)
        chat.config(state=tk.DISABLED)
        # Actualizar la barra lateral
        barra_lateral.insert(tk.END, mensaje + "\n")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Ventana de Chat")

# Widget para mostrar el chat
chat = tk.Text(ventana, state=tk.DISABLED)
chat.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

# Widget para la entrada de mensajes
entrada = tk.Entry(ventana)
entrada.grid(row=1, column=1, sticky="ew", padx=10, pady=10)
entrada.bind("<Return>", lambda event: enviar_mensaje())

# Botón para enviar mensajes
boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_mensaje)
boton_enviar.grid(row=1, column=2, sticky="ew", padx=10, pady=10)

# Barra lateral para el historial de la conversación
barra_lateral = tk.Text(ventana, width=20)
barra_lateral.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

# Configuración de las filas y columnas para que se expandan
ventana.grid_rowconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)

ventana.mainloop()

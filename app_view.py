import tkinter as tk

ventana = tk.Tk()
ventana.title("Monika Assistant")

# Tamaño de la ventana
ventana.geometry("500x600")

# Área de texto para el historial del chat
historial_chat = tk.Text(ventana, state='normal', width=60, height=30)
historial_chat.pack(padx=10, pady=10)


def enviar_mensaje():
    mensaje = entrada_texto.get()
    if mensaje:
        historial_chat.insert(tk.END, "Tú: " + mensaje + "\n")
        entrada_texto.delete(0, tk.END)
        # Aquí podrías añadir la lógica para obtener una respuesta de la IA y mostrarla en el historial
        # Por ejemplo: respuesta_ia = obtener_respuesta_ia(mensaje)
        # historial_chat.insert(tk.END, "IA: " + respuesta_ia + "\n")
        historial_chat.see(tk.END)

# Campo de entrada para nuevos mensajes
entrada_texto = tk.Entry(ventana, width=50)
entrada_texto.pack(padx=10, pady=5)

# Botón para enviar mensajes
boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_mensaje)
boton_enviar.pack(pady=5)

# Permitir enviar mensajes con la tecla Enter
ventana.bind('<Return>', lambda event: enviar_mensaje())

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
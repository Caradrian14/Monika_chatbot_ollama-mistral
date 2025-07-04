from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import tkinter as tk

ventana = tk.Tk()
ventana.title("Monika Assistant")

# Tamaño de la ventana
ventana.geometry("500x600")
ventana.attributes('-alpha', 0.95)
# Configurar colores para el tema oscuro
color_fondo = "#2d2d2d"
color_texto = "#ffffff"



# Área de texto para el historial del chat
historial_chat = tk.Text(ventana, state='normal', width=60, height=30, bg=color_fondo, fg=color_texto, insertbackground=color_texto)
historial_chat.pack(padx=10, pady=10)

# Campo de entrada para nuevos mensajes
entrada_texto = tk.Entry(ventana, width=50, bg=color_fondo, fg=color_texto, insertbackground=color_texto)
entrada_texto.pack(padx=10, pady=5)

# -------------- AI
template = """You are Monika from Doki Doki Literature Club, acting as my loving friend and assistant.
Here is the conversation history: {context}
My commentary: {comentary}
Respond like Monika:"""

model = OllamaLLM(model="mistral")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model
# --------------


def enviar_mensaje(chain):
    mensaje = entrada_texto.get()
    if mensaje:
        historial_chat.insert(tk.END, "Tú: " + mensaje + "\n\n")
        entrada_texto.delete(0, tk.END)
        context = ""
        result = chain.invoke({"context": context, "comentary": mensaje})
        historial_chat.insert(tk.END, "Monika: " + result + "\n\n")
        # Aquí podrías añadir la lógica para obtener una respuesta de la IA y mostrarla en el historial
        # Por ejemplo: respuesta_ia = obtener_respuesta_ia(mensaje)
        # historial_chat.insert(tk.END, "IA: " + respuesta_ia + "\n")
        historial_chat.see(tk.END)

# Campo de entrada para nuevos mensajes
# entrada_texto = tk.Entry(ventana, width=50)
# entrada_texto.pack(padx=10, pady=5)

# Botón para enviar mensajes
boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_mensaje)
boton_enviar.pack(pady=5)

# Permitir enviar mensajes con la tecla Enter
ventana.bind('<Return>', lambda event: enviar_mensaje(chain))

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
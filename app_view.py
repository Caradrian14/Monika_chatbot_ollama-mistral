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

# Cargar imágenes para los iconos
# Asegúrate de tener las imágenes en el mismo directorio o proporciona la ruta completa
try:
    icono_usuario = tk.PhotoImage(file="media/user.png")
    icono_ia = tk.PhotoImage(file="media/monika.png")
except:
    print("No se pudieron cargar las imágenes. Usando texto en su lugar.")
    icono_usuario = None
    icono_ia = None

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


def enviar_mensaje_depracted(chain):
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

def enviar_mensaje(chain):
    mensaje = entrada_texto.get()
    if mensaje:
        # Mostrar mensaje del usuario con icono
        mostrar_mensaje("User", mensaje, icono_usuario)
        entrada_texto.delete(0, tk.END)

        # Simular respuesta de la IA
        context = ""
        respuesta_ia = chain.invoke({"context": context, "comentary": mensaje})
        mostrar_mensaje("Monika", respuesta_ia, icono_ia)

# Función para mostrar mensajes con iconos
def mostrar_mensaje(autor, mensaje, icono):
    frame = tk.Frame(historial_chat, bg=color_fondo)
    frame.pack(anchor='w', pady=5, padx=10)

    if icono:
        etiqueta_icono = tk.Label(frame, image=icono, bg=color_fondo)
        etiqueta_icono.pack(side='left')

    etiqueta_mensaje = tk.Label(frame, text=f"{autor}: {mensaje}", bg=color_fondo, fg=color_texto, wraplength=400)
    etiqueta_mensaje.pack(side='left')

    historial_chat.window_create(tk.END, window=frame)
    historial_chat.insert(tk.END, "\n")

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
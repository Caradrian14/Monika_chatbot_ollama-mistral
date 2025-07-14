
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import logging


import os
import tkinter as tk
from tkinter import ttk
load_dotenv()

#icon
try:
    user_icon = tk.PhotoImage(file=os.getenv('CHAT_USER_ICON'))
    ia_icon = tk.PhotoImage(file=os.getenv('CHAT_IA_ICON'))
except:
    print("No se pudieron cargar las imágenes. Usando texto en su lugar.")
    user_icon = None
    ia_icon = None


#ollama
template = os.getenv('TEMPLATE_FOR_MODEL')
model_name = os.getenv('MODEL_OLLAMA')
model = OllamaLLM(model=model_name)
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model
context = ""
#funciones
def enviar_mensaje():
    message = input.get()
    if message:
        chat.config(state=tk.NORMAL)
        chat.insert(tk.END, "Tú: " + message + "\n")
        chat.config(state=tk.DISABLED)
        input.delete(0, tk.END)
        # Aquí podrías añadir la lógica para obtener una respuesta y mostrarla en el chat
        respuesta = chain.invoke({"context": context, "comentary": message})

        # Por ejemplo, una respuesta automática:
        #respuesta = "Monika: " + message + "\n"
        chat.config(state=tk.NORMAL)
        chat.insert(tk.END, respuesta)
        chat.config(state=tk.DISABLED)




# Configuración de la ventana principal
window = tk.Tk()
title_window = os.getenv('WINDOW_TITLE')
window.title(title_window)

# Widget para mostrar el chat
chat = tk.Text(window, state=tk.DISABLED)
chat.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

# Widget para la entrada de mensajes
input = tk.Entry(window)
input.grid(row=1, column=1, sticky="ew", padx=10, pady=10)
input.bind("<Return>", lambda event: enviar_mensaje())

# Botón para enviar mensajes
send_button = tk.Button(window, text="Enviar", command=enviar_mensaje)
send_button.grid(row=1, column=2, sticky="ew", padx=10, pady=10)

# Configuración de las filas y columnas para que se expandan
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

window.mainloop()

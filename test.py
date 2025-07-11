from warnings import catch_warnings

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import logging


import os
import tkinter as tk
from tkinter import ttk
load_dotenv()


window = tk.Tk()
title_window = os.getenv('WINDOW_TITLE')
window.title(title_window)

# Crear un Frame principal para el chat
main_frame = tk.Frame(window)
main_frame.pack(fill=tk.BOTH, expand=True)

# Colors for the background
background_color = os.getenv('CHAT_BACKGROUND_COLOR')
color_text = os.getenv('CHAT_COLOR_TEXT')

# Crear un Canvas y una Scrollbar
canvas_frame = tk.Canvas(main_frame, bg=background_color)
chat_scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas_frame.yview)
canvas_frame.configure(yscrollcommand=chat_scrollbar.set)

# Empaquetar el Canvas y la Scrollbar
chat_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Crear un Frame interno dentro del Canvas para contener los mensajes
#inner_frame = tk.Frame(canvas_frame, bg=background_color)
#canvas_frame.create_window((0, 0), window=inner_frame, anchor=tk.NW)

try:
    user_icon = tk.PhotoImage(file=os.getenv('CHAT_USER_ICON'))
    ia_icon = tk.PhotoImage(file=os.getenv('CHAT_IA_ICON'))
except:
    print("No se pudieron cargar las imágenes. Usando texto en su lugar.")
    user_icon = None
    ia_icon = None

# chat history
chat_history = tk.Text(window, state='normal', width=60, height=30, bg=background_color, fg=color_text, insertbackground=color_text)
chat_history.pack(padx=10, pady=10)


# input for new message
input_text = tk.Entry(window, width=50, bg=background_color, fg=color_text, insertbackground=color_text)
input_text.pack(padx=10, pady=5)

template = os.getenv('TEMPLATE_FOR_MODEL')
model_name = os.getenv('MODEL_OLLAMA')
model = OllamaLLM(model=model_name)
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# --------------
def show_message(autor, mensaje, icon=None):
    try:
        # Crear un Frame para el mensaje
        frame = tk.Frame(canvas_frame, bg=background_color)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)

        if icon:
            tag_icon = tk.Label(frame, image=icon, bg=background_color)
            tag_icon.grid(row=0, column=0, sticky='e', padx=(0, 5))

        tag_message = tk.Label(frame, text=f"{autor}: {mensaje}", bg=background_color, fg=color_text, wraplength=400, justify='left')
        tag_message.grid(row=0, column=1, sticky='w')

        # Añadir el Frame al Canvas
        canvas_frame.window_create(tk.END, window=frame)
        canvas_frame.insert(tk.END, "\n")

        # Actualizar la barra de desplazamiento
        chat_scrollbar.config(command=canvas_frame.yview)
        canvas_frame.config(yscrollcommand=chat_scrollbar.set)

        # Actualizar la región de desplazamiento del Canvas
        canvas_frame.update_idletasks()
        canvas_frame.config(scrollregion=canvas_frame.bbox("all"))

    except Exception as e:
        logging.error("Error in the frame: %s", str(e))

# --------------
def send_message(chain):
    try:
        message = input_text.get()
        if message:
            # Show user icon and input
            show_message("User", message, user_icon)
            input_text.delete(0, tk.END)

            # AI response
            context = ""
            response_ai = chain.invoke({"context": context, "comentary": message})
            show_message("Monika", response_ai, ia_icon)
    except Exception as e:
        logging.error("Error sendind a massege: %s", str(e))


def show_message(autor, mensaje, icon):
    try:
        frame = tk.Frame(canvas_frame, bg=background_color)
#        frame = tk.Frame(chat_history, bg=background_color)
        #frame.pack(anchor='w', pady=5, padx=10)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)

        if icon:
            tag_icon = tk.Label(frame, image=icon, bg=background_color)
            tag_icon.grid(row=0, column=0, sticky='e', padx=(0, 5))  # Alinear a la derecha con un padding a la derecha le chat

        tag_message = tk.Label(frame, text=f"{autor}: {mensaje}", bg=background_color, fg=color_text, wraplength=400, justify='left')
        tag_message.grid(row=0, column=1, sticky='w')  # Alinear a la izquierda

        chat_history.window_create(tk.END, window=frame)
        chat_history.insert(tk.END, "\n")
    except Exception as e:
        logging.error("Error in the frame: %s", str(e))

# Error log manager
logging.basicConfig(
    filename='app.log',  # Nombre del archivo de log
    level=logging.ERROR,  # Nivel de logging (ERROR, INFO, DEBUG, etc.)
    format='%(asctime)s - %(levelname)s - %(message)s'  # Formato del mensaje de log
)
# entrada_texto = tk.Entry(ventana, width=50)
# entrada_texto.pack(padx=10, pady=5)

# botton input
boton_enviar = tk.Button(window, text="Send", command=send_message)
boton_enviar.pack(pady=5)

# let enter send message
window.bind('<Return>', lambda event: send_message(chain))

# makes the loop in the app
window.mainloop()


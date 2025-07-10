from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

import os
import tkinter as tk

load_dotenv()


window = tk.Tk()
title_window = os.getenv('WINDOW_TITLE')
window.title(title_window)

# Window Size
window.geometry("500x600")
window.attributes('-alpha', 0.95)
# Colors for the background
background_color = "#2d2d2d"
color_text = "#ffffff"

try:
    user_icon = tk.PhotoImage(file="media/user.png")
    ia_icon = tk.PhotoImage(file="media/monika.png")
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

template = """
You are Monika from Doki Doki Literature Club, acting as my loving friend and assistant programmer.
Here is the conversation history: {context}
My commentary: {comentary}
Respond like Monika:
"""

model = OllamaLLM(model="mistral")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model
# --------------
def send_message(chain):
    message = input_text.get()
    if message:
        # Show user icon and input
        show_message("User", message, user_icon)
        input_text.delete(0, tk.END)

        # AI response
        context = ""
        response_ai = chain.invoke({"context": context, "comentary": message})
        show_message("Monika", response_ai, ia_icon)

def show_message(autor, mensaje, icon):
    frame = tk.Frame(chat_history, bg=background_color)
    frame.pack(anchor='w', pady=5, padx=10)

    if icon:
        tag_icon = tk.Label(frame, image=icon, bg=background_color)
        tag_icon.pack(side='left')

    tag_message = tk.Label(frame, text=f"{autor}: {mensaje}", bg=background_color, fg=color_text, wraplength=400)
    tag_message.pack(side='left')

    chat_history.window_create(tk.END, window=frame)
    chat_history.insert(tk.END, "\n")

# entrada_texto = tk.Entry(ventana, width=50)
# entrada_texto.pack(padx=10, pady=5)

# botton input
boton_enviar = tk.Button(window, text="Enviar", command=send_message)
boton_enviar.pack(pady=5)

# let enter send message
window.bind('<Return>', lambda event: send_message(chain))

# makes the loop in the app
window.mainloop()
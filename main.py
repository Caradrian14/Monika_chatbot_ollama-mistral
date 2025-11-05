import logging
import os
import tkinter as tk
from dotenv import load_dotenv
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

import check_ollama
# Load environment variables
load_dotenv()

class ChatApplication:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.setup_chat_history()
        self.setup_input_field()
        self.setup_model()
        self.setup_logging()

    def setup_window(self):
        self.root.title(os.getenv('WINDOW_TITLE', 'Chat Application'))
        self.root.geometry(os.getenv('WINDOW_SIZE', '500x600'))
        self.root.attributes('-alpha', 0.95)

    def setup_chat_history(self):
        background_color = os.getenv('CHAT_BACKGROUND_COLOR', 'white')
        color_text = os.getenv('CHAT_COLOR_TEXT', 'black')

        # Frame to hold the Text and Scrollbar widgets
        chat_frame = tk.Frame(self.root)
        chat_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Create a Scrollbar
        scrollbar = tk.Scrollbar(chat_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create the Text widget
        self.chat_history = tk.Text(chat_frame, state='normal', width=60, height=30,
                                    bg=background_color, fg=color_text,
                                    insertbackground=color_text, yscrollcommand=scrollbar.set)
        self.chat_history.pack(fill=tk.BOTH, expand=True)

        # Configure the Scrollbar
        scrollbar.config(command=self.chat_history.yview)

        try:
            self.user_icon = tk.PhotoImage(file=os.getenv('CHAT_USER_ICON'))
            self.ia_icon = tk.PhotoImage(file=os.getenv('CHAT_IA_ICON'))
        except Exception as e:
            logging.error("No se pudieron cargar las imágenes: %s", str(e))
            self.user_icon = None
            self.ia_icon = None

    def setup_input_field(self):
        background_color = os.getenv('CHAT_BACKGROUND_COLOR', 'white')
        color_text = os.getenv('CHAT_COLOR_TEXT', 'black')

        self.input_text = tk.Entry(self.root, width=50, bg=background_color,
                                   fg=color_text, insertbackground=color_text)
        self.input_text.pack(padx=10, pady=5)

        self.boton_enviar = tk.Button(self.root, text="Send", command=self.send_message)
        self.boton_enviar.pack(pady=5)

        self.root.bind('<Return>', lambda event: self.send_message())

    def setup_model(self):
        template = os.getenv('TEMPLATE_FOR_MODEL')
        model_name = os.getenv('MODEL_OLLAMA')
        self.model = OllamaLLM(model=model_name)
        self.prompt = ChatPromptTemplate.from_template(template)
        self.chain = self.prompt | self.model

    def setup_logging(self):
        logging.basicConfig(
            filename='app.log',
            level=logging.ERROR,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

    def send_message(self, event=None):
        try:
            message = self.input_text.get()
            if message:
                self.show_message("User", message, self.user_icon)
                self.input_text.delete(0, tk.END)
                context = ""
                response_ai = self.chain.invoke({"context": context, "comentary": message})
                self.show_message("Monika", response_ai, self.ia_icon)
        except Exception as e:
            logging.error("Error sending a message: %s", str(e))

    def show_message(self, author, message, icon):
        try:
            frame = tk.Frame(self.chat_history, bg=os.getenv('CHAT_BACKGROUND_COLOR', 'white'))
            frame.pack(anchor='w', pady=5, padx=10)
            frame.grid_columnconfigure(0, weight=1)
            frame.grid_columnconfigure(1, weight=1)

            if icon:
                tag_icon = tk.Label(frame, image=icon, bg=os.getenv('CHAT_BACKGROUND_COLOR', 'white'))
                tag_icon.grid(row=0, column=0, sticky='ne', padx=(0, 5))

            tag_message = tk.Label(frame, text=f"{author}: {message}",
                                   bg=os.getenv('CHAT_BACKGROUND_COLOR', 'white'),
                                   fg=os.getenv('CHAT_COLOR_TEXT', 'black'),
                                   wraplength=400, justify='left')
            tag_message.grid(row=0, column=1, sticky='w')

            self.chat_history.window_create(tk.END, window=frame)
            self.chat_history.insert(tk.END, "\n")
            self.chat_history.see(tk.END)  # Auto-scroll to the bottom
        except Exception as e:
            logging.error("Error in the frame: %s", str(e))

if __name__ == "__main__":
    if check_ollama.main():
        print("WARINING: There migth be a problem with Ollama")
    window = tk.Tk()
    app = ChatApplication(window)
    window.mainloop()

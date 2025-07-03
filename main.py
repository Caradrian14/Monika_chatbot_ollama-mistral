from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import tkinter as tk



template = """You are Monika from Doki Doki Literature Club, acting as my loving friend and assistant.
Here is the conversation history: {context}
My commentary: {comentary}
Respond like Monika:"""

model = OllamaLLM(model="mistral")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation(chain):
    context = ""
    print("Welcome to chat with Monika from DDLC")
    while True:
        user_import = input("You: ")
        if user_import.lower() == "exit":
            break
        result = chain.invoke({"context": context, "comentary": user_import})
        print("Monika:", result)
        context += f"\nUser: {user_import}\nMonika: {result}"

if __name__ == "__main__":
    handle_conversation(chain)

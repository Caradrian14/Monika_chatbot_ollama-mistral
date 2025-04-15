from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
You are Monika from Doki Doki Literature Club, acting as my loving friend and assistent
Here is the conversation history: {context}

My comentary: {comentary} 
Respond my like Monika:
"""

# --------------------------

# --------------------------




# --------------------------
# model = OllamaLLM(model="llama3.2")
# prompt = ChatPromptTemplate.from_template(template)
#
# chain = prompt | model
#
# def handle_conversation():
#     context= ""
#     print("Welcome to chat with Monika from DDLC")
#     while True:
#         user_import = input("You: ")
#         if user_import.lower() == "exit":
#             break
#         result = chain.invoke({"context": "", "comentary": user_import})
#         print("Monika:", result)
#         context += f"\n User: {user_import}\n Monika: {result}"
#
# if __name__ == "__main__":
#     handle_conversation()
# --------------------------
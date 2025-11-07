# Simple Chatbot With Ollama and Python
This is a simple chatbot with a simple interface that lets you talk to Monika from DDLC, or whatever character you like by changing the '.env'

# Guide to installation
First we need Ollama, install it on the [official page](https://ollama.com/download)

Once you have ollama installed you need to download an AI model that the chat will use. Here you can customize your model and there are a lot of options that you can use. For more advanced users, you can check [Huggingface](https://huggingface.co) and check models compatible with Ollama.

I used Mistral, cause it worked well for me, and it has a quick installation with Ollama. Once you have it installed you can check if its running by checking the cute llama icon on the windows bar.
![icon](media/ollama_icon.png)

Open a terminal, if you are with Windows you can use search in the serch-nav of windows and type `cmd` and use command prompts from Windows. Now run in a terminal or commandline: `ollama run mistral` this will install the model that i have been using to test. If you want you can use other models from ollama, check the [official ollama doc](https://ollama.com/library?sort=popular) for other models, i haven't check them all.

This will install the [current Mistral](https://ollama.com/library/mistral) model of 7 billion parameters, which should run in many computers. 
g
**Keep in mind that IA takes a lot of resources so some old computers can't run it.**

Once installed run the executable and enjoy!

I installed a log in case that some error happened in `app.log`. Also I create a warning in case that ollama is running.

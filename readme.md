# Simple Chatbot
This is a simple chatbot with a simple interface that lets you talk to Monika from DDLC, or whatever character you like by changing the '.env'

# Guide to installation
First we need Ollama, install it on the [official page](https://ollama.com/download)

Once you have ollama installed you need to download an AI model that the chat will use. Here you can customize your model and there are a lot of options that you can use. For more advanced users, you can check [Huggingface](https://huggingface.co) and check models compatible with Ollama.

I used Mistral, cause it worked well for me, and it has a quick installation.

Run in a terminal or commandline: `ollama run mistral`

This will install the current Mistral model of 7 billion parameters, which should run in many computers. 

**Keep in mind that IA takes a lot of resources so some old computers can't run it.**

Once installed run the executable and enjoy!

I installed a log in case that some error happened in `app.log`.
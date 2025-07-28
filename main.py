from tkinter import *
import tkinter as tk
from model import Ollama

# Função principal que cria a interface
def iniciar_tela():
    window = tk.Tk()
    window.title("Chat Simples")

    # Área de exibição de mensagens
    chat_display = tk.Text(
        window,
        height=20,
        width=50,
        background="#E0DDE0"
    )
    chat_display.pack()

    # Campo de entrada de texto
    input_text = tk.StringVar(window)
    campo_de_texto = tk.Entry(window, textvariable=input_text, width=40)
    campo_de_texto.pack()

    # Botão de envio
    send_button = tk.Button(
        window,
        text='Enviar',
        command=lambda: enviar(input_text, campo_de_texto, chat_display)
    )
    send_button.pack()

    window.mainloop()  # Inicia o loop da interface

# Função que captura e exibe o texto

def enviar(user_input, limpar_tela, chat_display):
    historico_msg =user_input.get()
    chat_display.insert(tk.END,"Você: " + historico_msg + '\n')
    limpar_tela.delete(0, tk.END)
    resposta_bot(historico_msg, chat_display)

def resposta_bot(historico_msg, chat_display):
    resposta_bot = Ollama(historico_msg)
    chat_display.insert(tk.END,"Bot: " + resposta_bot.chatbot() + '\n')


if __name__ == "__main__":
    iniciar_tela()









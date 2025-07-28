
# 🗨️ Chat Simples com Interface Tkinter + API Ollama

Este é um projeto de chatbot simples que está em **desenvolvimento** e com intenção de tornar um assistente de reuniões. Possui uma interface gráfica feita em **Tkinter** que utiliza um modelo de linguagem da API **Ollama** para gerar respostas curtas e em português. Ele é ideal como base para projetos de assistentes pessoais, chatbots de atendimento ou estudos com LLMs locais.

---

## 🧠 Funcionalidades

- Interface gráfica com Tkinter
- Campo de entrada de mensagem e botão de envio
- Integração com modelo local via Ollama API (`http://localhost:11434/api/generate`)
- Geração de respostas com no máximo **uma linha** em **português do Brasil**

---

## 🖼️ Prévia da Interface

> Uma janela simples com histórico de mensagens e campo de texto com botão "Enviar".

---

## 🧰 Tecnologias Usadas

- Python 3.12
- Tkinter (nativo do Python)
- [Ollama](https://ollama.com) - para rodar LLMs localmente (ex: Gemma 3B, LLaMA, etc.)
- Modelo `gemma3:1b` (você pode trocar por qualquer outro instalado)

---

## 🚀 Como Executar

### 1. Instale o Ollama e baixe um modelo
Se ainda não tem o Ollama:

```bash
# Instale o Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Baixe o modelo usado no projeto (ou outro que preferir)
ollama run gemma3:1b
```

> **Importante:** Certifique-se de que o Ollama esteja rodando localmente em `http://localhost:11434`.

---

### 2. Instale as dependências Python

```bash
pip install requests
```

---

### 3. Execute o Chatbot

```bash
python chat_interface.py
```

---

## 🗃️ Estrutura do Projeto

```
chat-simples/
│
├── chat_interface.py   # Interface Tkinter e lógica do chat
├── model.py            # Classe Ollama que faz requisição à API
├── README.md           # Este arquivo
```

---

## ✏️ Exemplo de Uso

- Você digita: `Qual é a capital da França?`
- A resposta será algo como: `Paris.`

Sempre de forma curta e objetiva!

---

## 🛠️ Possíveis Melhorias Futuras

- Agendamento de reunião através do chat (Meet, teams e outros)
- Scroll automático na janela de mensagens
- Suporte a múltiplos modelos e seleção dinâmica

---

## 📜 Licença

Este projeto é livre para fins educacionais. Personalize como quiser!

---

## 🤝 Contribuições

Sinta-se à vontade para abrir issues, sugerir melhorias ou fazer pull requests!

import requests # type: ignore

class Ollama:
    def __init__(self, mensagem):
        self.prompt = mensagem

    def chatbot(self):
        url = "http://localhost:11434/api/generate"
        payload = {
            "model": "gemma3:1b",  
            "prompt": self.prompt,
            "stream": False,
            "system": "Quero que retorne sempre resposta de no máximo uma linha e em português Brasil."
        }

        response = requests.post(url, json=payload)
        
        if response.status_code == 200:
            return response.json()["response"]
        else:
            return f"Erro: {response.status_code} - {response.text}"

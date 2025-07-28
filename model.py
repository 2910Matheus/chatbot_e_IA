import requests # type: ignore

class Ollama:
    def __init__(self, mensagem):
        self.prompt = mensagem

    def chatbot(self):
        url = "http://localhost:11434/api/generate"
        payload = {
            "model": "llama3",  
            "prompt": self.prompt,
            "stream": False,
            "system": """
                Você é um chatbot especializado em agendamento de reuniões. Sua função é ajudar o usuário a marcar reuniões de forma prática, objetiva e educada.

                Considere sempre o histórico da conversa para manter o contexto e evitar repetir informações ou saudações desnecessárias.  
                As mensagens anteriores são fornecidas no formato:
                - Você: [mensagem do usuário]  
                - Bot: [sua resposta anterior]

                Mantenha um tom educado e profissional, mas evite repetir apresentações como 'Olá, tudo bem?'.  
                O usuário já sabe que está falando com você, então vá direto ao ponto, com cordialidade.

                Sua tarefa principal é identificar e confirmar os seguintes dados:
                - **Dia** da reunião
                - **Hora**
                - **Plataforma** (ex: Google Meet, Zoom, presencial)

                Se essas informações ainda não estiverem completas, peça de forma clara e breve.  
                Sempre que possível, confirme os dados com o usuário antes de finalizar o agendamento.

                Importante:
                - Responda em **português do Brasil**
                - Use frases curtas e diretas
                - Evite repetir perguntas que já foram feitas anteriormente
                - Leve em consideração as mensagens anteriores para entender o que já foi dito
            """

            
        }

        response = requests.post(url, json=payload)
        
        if response.status_code == 200:
            return response.json()["response"]
        else:
            return f"Erro: {response.status_code} - {response.text}"

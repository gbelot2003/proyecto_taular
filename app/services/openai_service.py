# app/services/openai_service.py
import os
from openai import OpenAI
from dotenv import load_dotenv
from app.services.action_handle_service import ActionHandleService

load_dotenv(override=True)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class OpenAIService:

    def __init__(self):
        self.action_handle_service = ActionHandleService()

    def handle_request(self, prompt):
        try:
            # Manejar la solicitud con ActionHandleService
            action_response = self.action_handle_service.handle_request(prompt)

            if action_response.get("status") == "error":
                return action_response

            gpt_prompt = action_response.get("prompt")

            # Enviar el prompt a OpenAI
            gpt_response = self._enviar_a_gpt(gpt_prompt)
            return {"status": "success", "response": gpt_response}
        
        except Exception as e:
            return {"status": "error", "response": str(e)}

    def _enviar_a_gpt(self, prompt):
        # Enviar el mensaje a GPT y devolver la respuesta
        messages = [{"role": "user", "content": prompt}]
        
        # Enviar los mensajes a la API de OpenAI
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", messages=messages, max_tokens=550, temperature=0.1  # type: ignore
        )
        
        # Obtener la respuesta generada por el modelo
        respuesta_modelo = response.choices[0].message.content.strip()  # type: ignore
        return respuesta_modelo
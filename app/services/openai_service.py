# app/services/openai_service.py

import os
from app import db
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(override=True)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class OpenAIService:

    def __init__(self):
        pass

    def handle_request(self, prompt, from_number):
        # Definir el prompt del usuario
        try:
            # Imprimir el prompt del usuario
            print(f"Usuario: {prompt}")
            
            # Enviar los mensajes a la API de OpenAI
            response = client.chat.completions.create(
                model="gpt-3.5-turbo", messages=messages, max_tokens=550, temperature=0.1  # type: ignore
            )
            
            # Obtener la respuesta generada por el modelo
            respuesta_modelo = response.choices[0].message.content.strip()  # type: ignore

            # Imprimir la respuesta generada por el modelo
            print(f"GPT: {respuesta_modelo}")

            # Guardar la conversión del modelo en la base de datos

            return {"status": "success", "response": respuesta_modelo}
        except Exception as e:
            return {"status": "error", "response": str(e)}
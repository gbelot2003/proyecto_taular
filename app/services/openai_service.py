# app/services/openai_service.py
import os
from app.actions.student_result_action import obtener_resultado_estudiante, crear_prompt_alumno
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(override=True)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class OpenAIService:

    def __init__(self):
        pass

    def handle_request(self, prompt):
        try:
            # Imprimir el prompt del usuario
            print(f"Usuario: {prompt}")

            # Si el prompt solicita el estado de un alumno
            if "estado de" in prompt.lower():
                # Extraer el nombre o email del prompt
                name_or_email = prompt.split('estado de')[-1].strip()

                # Obtener la información del estudiante desde la acción
                alumno_info = obtener_resultado_estudiante(name_or_email)

                # Verificar si se encontró al estudiante
                if alumno_info:
                    # Crear el mensaje para GPT basándose en la información del alumno
                    gpt_prompt = crear_prompt_alumno(alumno_info)

                    # Enviar el mensaje a GPT para análisis
                    gpt_response = self._enviar_a_gpt(gpt_prompt)
                    return {"status": "success", "response": gpt_response}
                else:
                    return {"status": "error", "response": f"No se encontró información del alumno '{name_or_email}'."}
            else:
                # Prompt general, enviar directamente a GPT
                gpt_response = self._enviar_a_gpt(prompt)
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

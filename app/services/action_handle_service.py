# app/services/action_handle_service.py

from app.actions.student_result_action import obtener_resultado_estudiante, crear_prompt_alumno

class ActionHandleService:

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
                print(alumno_info)

                # Verificar si se encontró al estudiante
                if alumno_info:
                    # Crear el mensaje para GPT basándose en la información del alumno
                    gpt_prompt = crear_prompt_alumno(alumno_info)
                    return {"status": "success", "prompt": gpt_prompt}
                else:
                    return {"status": "error", "response": f"No se encontró información del alumno '{name_or_email}'."}
            else:
                # Prompt general, devolver directamente
                return {"status": "success", "prompt": prompt}
        
        except Exception as e:
            return {"status": "error", "response": str(e)}
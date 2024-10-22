# app/actions/student_result_action.py
import os
import requests
from flask import current_app

# Acción para obtener el resultado de un estudiante
def obtener_resultado_estudiante(nombre_o_email):
    try:
        # Definir la URL y el token de la API
        api_url = 'http://127.0.0.1:5000/api/alumno'
        token = os.getenv("SECRET_API_TOKEN")

        # Realizar la solicitud al API de alumnos
        params = {
            'email': nombre_o_email,
            'token': token
        }

        response = requests.get(api_url, params=params)

        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            alumno_info = response.json()
            return alumno_info
        else:
            current_app.logger.error(f"Error al consultar el API de alumnos: {response.status_code} - {response.text}")
            return None
    except requests.RequestException as e:
        current_app.logger.error(f"Error al consultar el API de alumnos: {str(e)}")
        return None
    except Exception as e:
        current_app.logger.error(f"Error inesperado: {str(e)}")
        return None


# Crear el prompt para enviar a GPT basado en los datos del estudiante
def crear_prompt_alumno(alumno_info):
    if not alumno_info:
        return "No se encontró información del alumno."
    
    # Validar que los campos necesarios estén presentes
    if 'nombre' not in alumno_info or 'apellido' not in alumno_info or 'parciales' not in alumno_info:
        return "Información del alumno incompleta."
    
    # Crear un mensaje detallado para enviar a GPT con los datos del alumno
    prompt = f"Estado del alumno {alumno_info['nombre']} {alumno_info['apellido']}:\n"
    for parcial in alumno_info['parciales']:
        if 'total_obtenido' not in parcial or 'clase' not in parcial or 'parcial' not in parcial:
            continue  # Saltar parciales con información incompleta
        
        total_obtenido = parcial['total_obtenido']
        prompt += f"\nParcial {parcial['parcial']} de {parcial['clase']}:\n"
        prompt += f"Total obtenido: {total_obtenido}\n"
    
    prompt += "\nDar el resultado por parcial del alumno y genera 2 consejos para mejorar el rendimiento de este alumno basado en las notas obtenidas."
    return prompt
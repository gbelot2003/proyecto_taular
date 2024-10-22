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
            return None
    except requests.RequestException as e:
        current_app.logger.error(f"Error al consultar el API de alumnos: {str(e)}")
        return None


# Crear el prompt para enviar a GPT basado en los datos del estudiante
def crear_prompt_alumno(alumno_info):
    if not alumno_info:
        return "No se encontró información del alumno."
    
    # Crear un mensaje detallado para enviar a GPT con los datos del alumno
    prompt = f"Estado del alumno {alumno_info['nombre']} {alumno_info['apellido']}:\n"
    for parcial in alumno_info['parciales']:
        total_obtenido = parcial['total_obtenido']
        total_maximo = parcial['total_maximo']
        rendimiento = (total_obtenido / total_maximo) * 100 if total_maximo > 0 else 0
        prompt += f"\nParcial {parcial['parcial']} de {parcial['clase']}:\n"
        prompt += f"Total obtenido: {total_obtenido}/{total_maximo} ({rendimiento:.2f}%)\n"
    
    prompt += "\nDar el resultado por parcial del alumno y genera algunos consejos para mejorar el rendimiento de este alumno basado en las notas obtenidas."
    return prompt
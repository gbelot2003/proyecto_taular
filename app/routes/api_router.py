# Archivo: app/routes/api_router.py
from flask import Flask, current_app, jsonify, request
from app.models.alumno_model import Alumno
from app.models.tarea_model import Tarea
from app.models.prueba_model import Prueba
from app.models.examen_model import Examen
from app.models.parcial_model import Parcial
from config import Config  # Asegúrate de importar tu configuración

from app import db

def configurar_api(app):
    app.config.from_object(Config)  # Cargar la configuración desde Config

    # Función para convertir el objeto Alumno a un diccionario
    def alumno_to_dict(alumno):
        parciales = Parcial.query.all()  # Obtener todos los parciales
        parciales_data = []
        
        for parcial in parciales:
            # Obtener tareas, pruebas y exámenes del alumno para este parcial
            tareas = Tarea.query.filter_by(alumno_id=alumno.id, parcial_id=parcial.id).all()
            pruebas = Prueba.query.filter_by(alumno_id=alumno.id, parcial_id=parcial.id).all()
            examenes = Examen.query.filter_by(alumno_id=alumno.id, parcial_id=parcial.id).all()

            # Sumar puntajes obtenidos y máximos para el parcial
            total_obtenido = sum(tarea.puntaje_obtenido for tarea in tareas) + \
                            sum(prueba.puntaje_obtenido for prueba in pruebas) + \
                            sum(examen.puntaje_obtenido for examen in examenes)

            total_maximo = sum(tarea.puntaje_maximo for tarea in tareas) + \
                        sum(prueba.puntaje_maximo for prueba in pruebas) + \
                        sum(examen.puntaje_maximo for examen in examenes)

            parciales_data.append({
                "parcial": parcial.numero,
                "clase": parcial.clase.nombre,
                "tareas": [{"descripcion": tarea.descripcion, "puntaje_maximo": tarea.puntaje_maximo, "puntaje_obtenido": tarea.puntaje_obtenido} for tarea in tareas],
                "pruebas": [{"descripcion": prueba.descripcion, "puntaje_maximo": prueba.puntaje_maximo, "puntaje_obtenido": prueba.puntaje_obtenido} for prueba in pruebas],
                "examenes": [{"descripcion": examen.descripcion, "puntaje_maximo": examen.puntaje_maximo, "puntaje_obtenido": examen.puntaje_obtenido} for examen in examenes],
                "total_obtenido": total_obtenido,
                "total_maximo": total_maximo
            })

        return {
            "id": alumno.id,
            "nombre": alumno.nombre,
            "apellido": alumno.apellido,
            "email": alumno.email,
            "grado": alumno.grado.nombre if alumno.grado else None,
            "parciales": parciales_data  # Añadir parciales con resultados
        }

    @app.route('/api/alumno', methods=['GET'])
    def buscar_alumno():
        # Obtener el token enviado en la solicitud (puede ser en el encabezado o en los parámetros)
        token = request.args.get('token')  # O también se puede usar: request.headers.get('Authorization')
        nombre = request.args.get('nombre')
        email = request.args.get('email')

        # Verificar si el token es válido
        # if token != current_app.config['SECRET_API_TOKEN']:
        #     return jsonify({"error": "Token de seguridad no válido."}), 403

        # Verificar si se envió un nombre o un email
        if not nombre and not email:
            return jsonify({"error": "Debes proporcionar un nombre o un email"}), 400
        
        # Buscar por nombre si se proporciona
        if nombre:
            alumnos = Alumno.query.filter(Alumno.nombre.ilike(f"%{nombre}%")).all()
            if not alumnos:
                return jsonify({"error": f"No se encontraron alumnos con el nombre {nombre}"}), 404
            return jsonify([alumno_to_dict(alumno) for alumno in alumnos])
        
        # Buscar por email si se proporciona
        if email:
            alumno = Alumno.query.filter_by(email=email).first()
            if not alumno:
                return jsonify({"error": f"No se encontró un alumno con el email {email}"}), 404
            return jsonify(alumno_to_dict(alumno))
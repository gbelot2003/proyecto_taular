# Archivo: app/routes/api_router.py
from flask import Flask, jsonify, request
from app.models.alumno_model import Alumno
from app import db

def configurar_api(app):

    # Función para convertir el objeto Alumno a un diccionario
    def alumno_to_dict(alumno):
        return {
            "id": alumno.id,
            "nombre": alumno.nombre,
            "apellido": alumno.apellido,
            "email": alumno.email,
            "grado": alumno.grado.nombre if alumno.grado else None,
            # Añadir más campos según tu modelo
        }

    @app.route('/api/alumno', methods=['GET'])
    def buscar_alumno():
        nombre = request.args.get('nombre')
        email = request.args.get('email')

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
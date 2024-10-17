# Archivo: app/seeds/parcial_seed.py
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from app import create_app, db
from app.models.parcial_model import Parcial
from app.models.tarea_model import Tarea
from app.models.prueba_model import Prueba
from app.models.examen_model import Examen
from app.models.alumno_model import Alumno
from app.models.clase_model import Clase

def seed_parciales():
    app = create_app()  # Crear la aplicación Flask
    with app.app_context():
        # Obtener una clase y un alumno
        clase = Clase.query.filter_by(nombre='Matemáticas').first()
        alumno = Alumno.query.filter_by(nombre='Juan').first()

        # Crear parciales para la clase
        for i in range(1, 5):
            parcial = Parcial(numero=i, clase=clase)
            db.session.add(parcial)
            db.session.commit()

            # Asignar tareas y pruebas al alumno para el parcial
            tarea1 = Tarea(descripcion=f'Tarea {i}-1', puntaje_maximo=10, parcial=parcial, alumno=alumno, puntaje_obtenido=8)
            prueba1 = Prueba(descripcion=f'Prueba {i}-1', puntaje_maximo=20, parcial=parcial, alumno=alumno, puntaje_obtenido=18)
            examen = Examen(descripcion=f'Examen {i}', puntaje_maximo=70, parcial=parcial, alumno=alumno, puntaje_obtenido=65)

            db.session.add_all([tarea1, prueba1, examen])
            db.session.commit()

        print("Seeding completado: Parciales, tareas, pruebas y examenes agregados.")

if __name__ == '__main__':
    seed_parciales()

# Archivo: app/models/tarea_model.py

from . import db
from app.models.parcial_model import Parcial
from app.models.alumno_model import Alumno

class Tarea(db.Model):
    __tablename__ = 'tareas'

    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(255), nullable=False)
    puntaje_maximo = db.Column(db.Float, nullable=False)
    puntaje_obtenido = db.Column(db.Float, nullable=True)

    parcial_id = db.Column(db.Integer, db.ForeignKey('parciales.id'), nullable=False)
    alumno_id = db.Column(db.Integer, db.ForeignKey('alumnos.id'), nullable=False)
    
    parcial = db.relationship('Parcial', backref='tareas')
    alumno = db.relationship('Alumno', back_populates='tareas')

    def __repr__(self):
        return f'<Tarea {self.descripcion} para el Alumno {self.alumno.nombre}>'

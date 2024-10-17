# Archivo: app/models/prueba_model.py

from . import db
from app.models.parcial_model import Parcial
from app.models.alumno_model import Alumno

class Prueba(db.Model):
    __tablename__ = 'pruebas'

    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(255), nullable=False)
    puntaje_maximo = db.Column(db.Float, nullable=False)
    puntaje_obtenido = db.Column(db.Float)

    alumno_id = db.Column(db.Integer, db.ForeignKey('alumnos.id'), nullable=False)
    parcial_id = db.Column(db.Integer, db.ForeignKey('parciales.id'), nullable=False)

    # Definimos el backref aquí, pero no lo duplicamos en Alumno
    alumno = db.relationship('Alumno', backref='pruebas')
    parcial = db.relationship('Parcial', backref='pruebas')

    def __repr__(self):
        return f'<Prueba {self.descripcion} - Alumno {self.alumno.nombre}>'

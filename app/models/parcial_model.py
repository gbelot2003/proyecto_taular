# Archivo: app/models/parcial_model.py

from . import db
from app.models.clase_model import Clase
from app.models.alumno_model import Alumno

class Parcial(db.Model):
    __tablename__ = 'parciales'

    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, nullable=False)  # Número del parcial (1, 2, 3, 4)
    clase_id = db.Column(db.Integer, db.ForeignKey('clases.id'), nullable=False)
    clase = db.relationship('Clase', backref='parciales')

    def __repr__(self):
        return f'<Parcial {self.numero} de la Clase {self.clase.nombre}>'

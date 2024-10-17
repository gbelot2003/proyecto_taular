# Archivo: app/models/clase_model.py

from . import db
from app.models.grado_model import Grado

class Clase(db.Model):
    __tablename__ = 'clases'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)  # Nombre de la clase

    # Relación con Grado (una clase pertenece a un grado)
    grado_id = db.Column(db.Integer, db.ForeignKey('grados.id'), nullable=False)
    grado = db.relationship('Grado', backref='clases')

    def __repr__(self):
        return f'<Clase {self.nombre}>'

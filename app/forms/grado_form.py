from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class GradoForm(FlaskForm):
    nombre = StringField('Nombre del Grado', validators=[DataRequired()])
    submit = SubmitField('Guardar')

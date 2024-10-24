
from flask import render_template, redirect, session, url_for, flash, request
from app import db
from app.forms.alumno_form import AlumnoForm
from app.models.alumno_model import Alumno
from app.models.tarea_model import Tarea
from app.models.prueba_model import Prueba
from app.models.examen_model import Examen
from app.models.parcial_model import Parcial

def configurar_alumnos(app):
    # Ruta para listar alumnos
    @app.route('/alumnos', methods=['GET'])
    def listar_alumnos():
        if 'user' not in session:
            flash('Debes iniciar sesión para acceder al dashboard.', 'warning')
            return redirect(url_for('login'))
        alumnos = Alumno.query.all()
        return render_template('alumnos/listar.html', alumnos=alumnos)

    # Ruta para crear un nuevo alumno
    @app.route('/alumnos/crear', methods=['GET', 'POST'])
    def crear_alumno():
        if 'user' not in session:
            flash('Debes iniciar sesión para acceder al dashboard.', 'warning')
            return redirect(url_for('login'))
        form = AlumnoForm()
        if form.validate_on_submit():
            nuevo_alumno = Alumno(nombre=form.nombre.data, apellido=form.apellido.data, email=form.email.data, grado_id=form.grado.data)
            db.session.add(nuevo_alumno)
            db.session.commit()
            flash('Alumno creado correctamente.', 'success')
            return redirect(url_for('listar_alumnos'))
        return render_template('alumnos/crear.html', form=form)

    # Ruta para editar un alumno existente
    @app.route('/alumnos/editar/<int:id>', methods=['GET', 'POST'])
    def editar_alumno(id):
        if 'user' not in session:
            flash('Debes iniciar sesión para acceder al dashboard.', 'warning')
            return redirect(url_for('login'))
        alumno = Alumno.query.get_or_404(id)
        form = AlumnoForm(obj=alumno)
    
        # Obtener las tareas, pruebas y exámenes del alumno, agrupados por parcial
        tareas = Tarea.query.filter_by(alumno_id=alumno.id).all()
        pruebas = Prueba.query.filter_by(alumno_id=alumno.id).all()
        examenes = Examen.query.filter_by(alumno_id=alumno.id).all()
        # Siempre obtener los parciales, sin importar si el formulario es enviado o no
        parciales = Parcial.query.all()
       
        if form.validate_on_submit():
            alumno.nombre = form.nombre.data
            alumno.apellido = form.apellido.data
            alumno.email = form.email.data
            alumno.grado_id = form.grado.data
            db.session.commit()
            flash('Alumno actualizado correctamente.', 'success')
            return redirect(url_for('listar_alumnos'))
        
        return render_template('alumnos/editar.html', form=form, alumno=alumno, tareas=tareas, pruebas=pruebas, examenes=examenes, parciales=parciales)

    # Ruta para eliminar un alumno
    @app.route('/alumnos/eliminar/<int:id>', methods=['POST'])
    def eliminar_alumno(id):
        if 'user' not in session:
            flash('Debes iniciar sesión para acceder al dashboard.', 'warning')
            return redirect(url_for('login'))
        alumno = Alumno.query.get_or_404(id)
        db.session.delete(alumno)
        db.session.commit()
        flash('Alumno eliminado correctamente.', 'success')
        return redirect(url_for('listar_alumnos'))
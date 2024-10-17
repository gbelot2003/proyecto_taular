from flask import render_template, redirect, session, url_for, flash, request
from app import db
from app.forms.examen_form import ExamenForm
from app.models.prueba_model import Prueba
from app.models.examen_model import Examen


def configurar_examen(app):
    # CRUD para Exámenes
    # Ruta para listar exámenes
    @app.route('/examenes', methods=['GET'])
    def listar_examenes():
        examenes = Examen.query.all()
        return render_template('examenes/listar.html', examenes=examenes)

    # Ruta para crear un nuevo examen
    @app.route('/examenes/crear', methods=['GET', 'POST'])
    def crear_examen():
        form = ExamenForm()
        if form.validate_on_submit():
            nuevo_examen = Examen(
                descripcion=form.descripcion.data, 
                parcial_id=form.parcial.data, 
                alumno_id=form.alumno.data, 
                puntaje_maximo=form.puntaje_maximo.data,
                puntaje_obtenido=form.puntaje_obtenido.data
            )
            db.session.add(nuevo_examen)
            db.session.commit()
            flash('Examen creado correctamente.', 'success')
            return redirect(url_for('listar_examenes'))
        return render_template('examenes/crear.html', form=form)

    # Ruta para editar un examen existente
    @app.route('/examenes/editar/<int:id>', methods=['GET', 'POST'])
    def editar_examen(id):
        examen = Examen.query.get_or_404(id)
        form = ExamenForm(obj=examen)
        
        if form.validate_on_submit():
            examen.descripcion = form.descripcion.data
            examen.parcial_id = form.parcial.data
            examen.alumno_id = form.alumno.data
            examen.puntaje_maximo = form.puntaje_maximo.data
            examen.puntaje_obtenido = form.puntaje_obtenido.data
            db.session.commit()
            flash('Examen actualizado correctamente.', 'success')
            return redirect(url_for('listar_examenes'))
        
        return render_template('examenes/editar.html', form=form, examen=examen)

    # Ruta para eliminar un examen
    @app.route('/examenes/eliminar/<int:id>', methods=['POST'])
    def eliminar_examen(id):
        examen = Examen.query.get_or_404(id)
        db.session.delete(examen)
        db.session.commit()
        flash('Examen eliminado correctamente.', 'success')
        return redirect(url_for('listar_examenes'))
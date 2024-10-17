from flask import render_template, redirect, url_for, flash, request
from app import db
from app.forms.tareas_form import TareaForm
from app.models.tarea_model import Tarea

def configurar_tareas(app):
    # Ruta para listar tareas
    @app.route('/tareas', methods=['GET'])
    def listar_tareas():
        tareas = Tarea.query.all()
        return render_template('tareas/listar.html', tareas=tareas)

    # Ruta para crear una nueva tarea
    @app.route('/tareas/crear', methods=['GET', 'POST'])
    def crear_tarea():
        form = TareaForm()
        if form.validate_on_submit():
            nueva_tarea = Tarea(
                descripcion=form.descripcion.data, 
                parcial_id=form.parcial.data, 
                alumno_id=form.alumno.data, 
                puntaje_maximo=form.puntaje_maximo.data,
                puntaje_obtenido=form.puntaje_obtenido.data
            )
            db.session.add(nueva_tarea)
            db.session.commit()
            flash('Tarea creada correctamente.', 'success')
            return redirect(url_for('listar_tareas'))
        return render_template('tareas/crear.html', form=form)

    # Ruta para editar una tarea existente
    @app.route('/tareas/editar/<int:id>', methods=['GET', 'POST'])
    def editar_tarea(id):
        tarea = Tarea.query.get_or_404(id)
        form = TareaForm(obj=tarea)
        
        if form.validate_on_submit():
            tarea.descripcion = form.descripcion.data
            tarea.parcial_id = form.parcial.data
            tarea.alumno_id = form.alumno.data
            tarea.puntaje_maximo = form.puntaje_maximo.data
            tarea.puntaje_obtenido = form.puntaje_obtenido.data
            db.session.commit()
            flash('Tarea actualizada correctamente.', 'success')
            return redirect(url_for('listar_tareas'))
        
        return render_template('tareas/editar.html', form=form, tarea=tarea)

    # Ruta para eliminar una tarea
    @app.route('/tareas/eliminar/<int:id>', methods=['POST'])
    def eliminar_tarea(id):
        tarea = Tarea.query.get_or_404(id)
        db.session.delete(tarea)
        db.session.commit()
        flash('Tarea eliminada correctamente.', 'success')
        return redirect(url_for('listar_tareas'))
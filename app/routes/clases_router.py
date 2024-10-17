from flask import render_template, redirect, session, url_for, flash, request
from app import db
from app.forms.clases_form import ClaseForm
from app.models.clase_model import Clase

def configurar_clases(app):
    # Ruta para listar clases
    @app.route('/clases', methods=['GET'])
    def listar_clases():
        if 'user' not in session:
            flash('Debes iniciar sesión para acceder al dashboard.', 'warning')
            return redirect(url_for('login'))
        clases = Clase.query.all()
        return render_template('clases/listar.html', clases=clases)

    # Ruta para crear una nueva clase
    @app.route('/clases/crear', methods=['GET', 'POST'])
    def crear_clase():
        if 'user' not in session:
            flash('Debes iniciar sesión para acceder al dashboard.', 'warning')
            return redirect(url_for('login'))
        form = ClaseForm()
        if form.validate_on_submit():
            nueva_clase = Clase(
                nombre=form.nombre.data, 
                grado_id=form.grado.data, 
                maestro_id=form.maestro.data, 
                horario_inicio=form.horario_inicio.data, 
                horario_fin=form.horario_fin.data
            )
            db.session.add(nueva_clase)
            db.session.commit()
            flash('Clase creada correctamente.', 'success')
            return redirect(url_for('listar_clases'))
        return render_template('clases/crear.html', form=form)

    # Ruta para editar una clase existente
    @app.route('/clases/editar/<int:id>', methods=['GET', 'POST'])
    def editar_clase(id):
        if 'user' not in session:
            flash('Debes iniciar sesión para acceder al dashboard.', 'warning')
            return redirect(url_for('login'))
        clase = Clase.query.get_or_404(id)
        form = ClaseForm(obj=clase)
        
        if form.validate_on_submit():
            clase.nombre = form.nombre.data
            clase.grado_id = form.grado.data
            clase.maestro_id = form.maestro.data
            clase.horario_inicio = form.horario_inicio.data
            clase.horario_fin = form.horario_fin.data
            db.session.commit()
            flash('Clase actualizada correctamente.', 'success')
            return redirect(url_for('listar_clases'))
        
        return render_template('clases/editar.html', form=form, clase=clase)

    # Ruta para eliminar una clase
    @app.route('/clases/eliminar/<int:id>', methods=['POST'])
    def eliminar_clase(id):
        if 'user' not in session:
            flash('Debes iniciar sesión para acceder al dashboard.', 'warning')
            return redirect(url_for('login'))
        clase = Clase.query.get_or_404(id)
        db.session.delete(clase)
        db.session.commit()
        flash('Clase eliminada correctamente.', 'success')
        return redirect(url_for('listar_clases'))
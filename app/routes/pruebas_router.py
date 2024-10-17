from flask import render_template, redirect, session, url_for, flash, request
from app import db
from app.forms.prueba_form import PruebaForm
from app.models.prueba_model import Prueba
from app.models.examen_model import Examen

def configurar_prueba(app):
    # CRUD para Pruebas
    # Ruta para listar pruebas
    @app.route('/pruebas', methods=['GET'])
    def listar_pruebas():
        if 'user' not in session:
            flash('Debes iniciar sesión para acceder al dashboard.', 'warning')
            return redirect(url_for('login'))
        pruebas = Prueba.query.all()
        return render_template('pruebas/listar.html', pruebas=pruebas)

    # Ruta para crear una nueva prueba
    @app.route('/pruebas/crear', methods=['GET', 'POST'])
    def crear_prueba():
        if 'user' not in session:
            flash('Debes iniciar sesión para acceder al dashboard.', 'warning')
            return redirect(url_for('login'))
        form = PruebaForm()
        if form.validate_on_submit():
            nueva_prueba = Prueba(
                descripcion=form.descripcion.data, 
                parcial_id=form.parcial.data, 
                alumno_id=form.alumno.data, 
                puntaje_maximo=form.puntaje_maximo.data,
                puntaje_obtenido=form.puntaje_obtenido.data
            )
            db.session.add(nueva_prueba)
            db.session.commit()
            flash('Prueba creada correctamente.', 'success')
            return redirect(url_for('listar_pruebas'))
        return render_template('pruebas/crear.html', form=form)

    # Ruta para editar una prueba existente
    @app.route('/pruebas/editar/<int:id>', methods=['GET', 'POST'])
    def editar_prueba(id):
        if 'user' not in session:
            flash('Debes iniciar sesión para acceder al dashboard.', 'warning')
            return redirect(url_for('login'))
        prueba = Prueba.query.get_or_404(id)
        form = PruebaForm(obj=prueba)
        
        if form.validate_on_submit():
            prueba.descripcion = form.descripcion.data
            prueba.parcial_id = form.parcial.data
            prueba.alumno_id = form.alumno.data
            prueba.puntaje_maximo = form.puntaje_maximo.data
            prueba.puntaje_obtenido = form.puntaje_obtenido.data
            db.session.commit()
            flash('Prueba actualizada correctamente.', 'success')
            return redirect(url_for('listar_pruebas'))
        
        return render_template('pruebas/editar.html', form=form, prueba=prueba)

    # Ruta para eliminar una prueba
    @app.route('/pruebas/eliminar/<int:id>', methods=['POST'])
    def eliminar_prueba(id):
        if 'user' not in session:
            flash('Debes iniciar sesión para acceder al dashboard.', 'warning')
            return redirect(url_for('login'))
        prueba = Prueba.query.get_or_404(id)
        db.session.delete(prueba)
        db.session.commit()
        flash('Prueba eliminada correctamente.', 'success')
        return redirect(url_for('listar_pruebas'))

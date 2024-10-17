from flask import render_template, redirect, url_for, flash, request
from app import db
from app.forms.grado_form import GradoForm
from app.models.grado_model import Grado


def configurar_grados(app):

    # Ruta para listar grados
    @app.route('/grados', methods=['GET'])
    def listar_grados():
        grados = Grado.query.all()
        return render_template('grados/listar.html', grados=grados)

    # Ruta para crear un nuevo grado
    @app.route('/grados/crear', methods=['GET', 'POST'])
    def crear_grado():
        form = GradoForm()
        if form.validate_on_submit():
            nuevo_grado = Grado(nombre=form.nombre.data)
            db.session.add(nuevo_grado)
            db.session.commit()
            flash('Grado creado correctamente.', 'success')
            return redirect(url_for('listar_grados'))
        return render_template('grados/crear.html', form=form)

    # Ruta para editar un grado existente
    @app.route('/grados/editar/<int:id>', methods=['GET', 'POST'])
    def editar_grado(id):
        grado = Grado.query.get_or_404(id)
        form = GradoForm(obj=grado)
        
        if form.validate_on_submit():
            grado.nombre = form.nombre.data
            db.session.commit()
            flash('Grado actualizado correctamente.', 'success')
            return redirect(url_for('listar_grados'))
        
        return render_template('grados/editar.html', form=form, grado=grado)

    # Ruta para eliminar un grado
    @app.route('/grados/eliminar/<int:id>', methods=['POST'])
    def eliminar_grado(id):
        grado = Grado.query.get_or_404(id)
        db.session.delete(grado)
        db.session.commit()
        flash('Grado eliminado correctamente.', 'success')
        return redirect(url_for('listar_grados'))

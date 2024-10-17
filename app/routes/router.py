from flask import render_template, redirect, url_for, flash, request, session
from app.forms.login_forms import LoginForm
from app.forms.user_forms import UserForm
from app import db
from app.models.user_model import User

def configure_routes(app):    # Ruta para el home
    @app.route("/")
    def index():
        return render_template("index.html")

    # Ruta para la página de login
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            
            # Simulación de verificación de credenciales
            if email == 'admin@example.com' and password == 'password':
                session['user'] = email  # Guardar el usuario en la sesión
                flash('Has iniciado sesión correctamente.', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Correo o contraseña incorrectos.', 'danger')
        
        return render_template('login.html', form=form)

    # Ruta para el dashboard
    @app.route('/dashboard')
    def dashboard():
        if 'user' not in session:
            flash('Debes iniciar sesión para acceder al dashboard.', 'warning')
            return redirect(url_for('login'))
        return render_template('dashboard.html')

    # Ruta para listar usuarios
    @app.route('/usuarios', methods=['GET'])
    def listar_usuarios():
        if 'user' not in session:
            flash('Debes iniciar sesión para acceder al dashboard.', 'warning')
            return redirect(url_for('login'))
        usuarios = User.query.all()
        return render_template('usuarios/listar.html', usuarios=usuarios)


    # Ruta para crear un nuevo usuario
    @app.route('/usuarios/crear', methods=['GET', 'POST'])
    def crear_usuario():
        if 'user' not in session:
            flash('Debes iniciar sesión para acceder al dashboard.', 'warning')
            return redirect(url_for('login'))
        form = UserForm()
        if form.validate_on_submit():
            nuevo_usuario = User(username=form.username.data, email=form.email.data, role=form.role.data)
            db.session.add(nuevo_usuario)
            db.session.commit()
            flash('Usuario creado correctamente.', 'success')
            return redirect(url_for('listar_usuarios'))
        return render_template('usuarios/crear.html', form=form)

    # Ruta para editar un usuario existente
    @app.route('/usuarios/editar/<int:id>', methods=['GET', 'POST'])
    def editar_usuario(id):
        if 'user' not in session:
            flash('Debes iniciar sesión para acceder al dashboard.', 'warning')
            return redirect(url_for('login'))
        usuario = User.query.get_or_404(id)
        form = UserForm(obj=usuario)
        
        if form.validate_on_submit():
            usuario.username = form.username.data
            usuario.email = form.email.data
            usuario.role = form.role.data
            db.session.commit()
            flash('Usuario actualizado correctamente.', 'success')
            return redirect(url_for('listar_usuarios'))
        
        return render_template('usuarios/editar.html', form=form, usuario=usuario)

    # Ruta para eliminar un usuario
    @app.route('/usuarios/eliminar/<int:id>', methods=['POST'])
    def eliminar_usuario(id):
        if 'user' not in session:
            flash('Debes iniciar sesión para acceder al dashboard.', 'warning')
            return redirect(url_for('login'))
        usuario = User.query.get_or_404(id)
        db.session.delete(usuario)
        db.session.commit()
        flash('Usuario eliminado correctamente.', 'success')
        return redirect(url_for('listar_usuarios'))
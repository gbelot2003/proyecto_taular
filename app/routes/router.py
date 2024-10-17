from flask import render_template, redirect, url_for, flash, request, session
from app.forms.login_forms import LoginForm
from app.routes.clases_router import configurar_clases
from app.routes.grados_router import configurar_grados
from app.routes.tareas_router import configurar_tareas
from app.routes.usuarios_router import configurar_usuarios 
from app.routes.alumnos_router import configurar_alumnos

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

    configurar_usuarios(app)
    configurar_alumnos(app)
    configurar_clases(app)
    configurar_grados(app)
    configurar_tareas(app)
from flask import render_template, redirect, url_for, flash, request, session
from app.forms import LoginForm

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
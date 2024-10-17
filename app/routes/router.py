from flask import render_template


def configure_routes(app):    # Ruta para el home
    @app.route("/")
    def index():
        return render_template("index.html")
    
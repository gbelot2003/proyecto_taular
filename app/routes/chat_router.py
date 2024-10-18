from flask import render_template
from flask_socketio import emit

# Ruta para la página del chat
def configurar_chat(app, socketio):
    @app.route('/chat')
    def chat():
        return render_template('index.html')

    # Evento para manejar mensajes enviados desde el cliente
    @socketio.on('send_message')
    def handle_send_message(data):
        message = data['message']
        response_message = f"Consejero: {message}"
        emit('receive_message', {'message': response_message}, broadcast=True)

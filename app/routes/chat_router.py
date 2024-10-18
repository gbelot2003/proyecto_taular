from flask import render_template
from flask_socketio import emit

from app.services.openai_service import OpenAIService

# Ruta para la página del chat
def configurar_chat(app, socketio):
    @app.route('/chat')
    def chat():
        return render_template('index.html')

    # Evento para manejar mensajes enviados desde el cliente
    @socketio.on('send_message')
    def handle_send_message(data):
        message = data['message']
        from_number = data['from_number']

        service = OpenAIService().handle_request(message)

        response_message = f"Consejero: {service['response']}"
        emit('receive_message', {'message': response_message}, broadcast=True)

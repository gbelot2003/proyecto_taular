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
    def handle_message(data):
        prompt = data.get('message')

        if not prompt:
            emit('receive_message', {"error": "Debes proporcionar un mensaje"})
            return

        # Manejar la solicitud con OpenAIService
        gpt_response = OpenAIService().handle_request(prompt)

        if gpt_response.get("status") == "error":
            emit('receive_message', gpt_response)
        else:
            emit('receive_message', gpt_response)

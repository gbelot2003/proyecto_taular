from flask import Flask, jsonify, render_template, request
from app.services.openai_service import OpenAIService

def configurar_chat(app: Flask):
    @app.route('/chat')
    def chat():
        return render_template('index.html')

    @app.route('/send_message', methods=['POST'])
    def handle_send_message():
        data = request.json  # Obtener los datos enviados desde el cliente
        message = data.get('message')
        from_number = data.get('from_number')

        if not message:
            return jsonify({"error": "Message is required"}), 400

        service = OpenAIService().handle_request(message)

        response_message = {
            "from_number": from_number,
            "response": f"Consejero: {service['response']}"
        }
        
        response_message.headers.add('Access-Control-Allow-Origin', '*')

        return jsonify(response_message)
from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")  # Permite todas origens

@socketio.on('connect')
def handle_connect():
    print('👉 Cliente conectado!')  # Debug

@socketio.on('torcida_message')
def handle_message(data):
    print('📩 Mensagem recebida:', data)  # Debug
    socketio.emit('new_message', {
        'user': data.get('user', 'Anônimo'),
        'text': data.get('text', ''),
        'time': 'Agora'
    })

if __name__ == '__main__':
    print('🚀 Servidor WebSocket rodando em http://localhost:5000')
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
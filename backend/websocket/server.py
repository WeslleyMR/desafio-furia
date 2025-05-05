from flask import Flask
from flask_socketio import SocketIO
from .models import TorcidaMessages

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('send_message')
def handle_message(data):
    TorcidaMessages.save(data['usuario'], data['mensagem'])
    socketio.emit('new_message', data)

if __name__ == "__main__":
    socketio.run(app, port=5000)
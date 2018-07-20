from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'
socketio = SocketIO(app)


@socketio.on('connect')
def handle_connect():
    print("Client connected")


@socketio.on('disconnect')
def handle_disconnect():
    print("Client disconnected")


@socketio.on('chat')
def handle_chat(json):
    emit('chat', json)


if __name__ == '__main__':
    socketio.run(app, 'localhost', 4000)


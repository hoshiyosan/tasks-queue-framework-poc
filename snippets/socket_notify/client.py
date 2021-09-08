import socketio

sio = socketio.Client()
sio.connect('http://localhost:8000',
            socketio_path='ws/socket.io', namespaces=['/tasks/fca-235'])

sio.emit('task:done', namespace='/tasks/fca-235')

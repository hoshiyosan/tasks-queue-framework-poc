import socketio

sio = socketio.Client()
sio.connect('http://localhost:8000',
            socketio_path='ws/socket.io', namespaces=['/tasks/fca-235'])


@sio.on('task:done', namespace='/tasks/fca-235')
def on_task_235_done():
    print('task 235 is done')


print('waiting for task to end')

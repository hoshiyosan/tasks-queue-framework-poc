from fastapi import FastAPI
from fastapi_socketio import SocketManager

app = FastAPI()
socket_manager = SocketManager(app=app)


@socket_manager.on('task:done', namespace='/tasks/fca-235')
async def on_task_done(sid, *args, **kwargs):
    print('task fca-235 done')
    await socket_manager.emit('task:done', namespace='/tasks/fca-235')

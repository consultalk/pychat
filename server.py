import socketio


sio = socketio.Server()


@sio.event
def message(sid, data):
    print(f"Message from {sid}: {data}")

    sio.emit('message', data)


@sio.event
def connect(sid, environ):
    print(f"Client connected: {sid}")


@sio.event
def disconnect(sid):
    print(f"Client disconnected: {sid}")

if __name__ == '__main__':

    app = socketio.WSGIApp(sio)


    import gevent
    from gevent.pywsgi import WSGIServer

    http_server = WSGIServer(('localhost', 5000), app)
    print("Server running on http://localhost:5000")
    http_server.serve_forever()


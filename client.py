import socketio


sio = socketio.Client()


sio.connect('http://localhost:5000')

@sio.on('message')
def on_message(data):
    print(f"Received message: {data}")


while True:
    message = input("Enter your message (or 'exit' to quit): ")
    if message.lower() == 'exit':
        break
    sio.emit('message', message)


sio.disconnect()


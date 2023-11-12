**README**

## PYTHON LAB PROJECT IEM KOLKATA

This is a simple Socket.IO chat app that allows users to send and receive messages in real time.

**Server-side Algorithm**

1. **Initialize Server**

Import the necessary libraries:

```python
import socketio
```

Create a Socket.IO server:

```python
sio = socketio.Server()
```

2. **Define Event Handlers**

Define event handlers for Socket.IO events such as `message`, `connect`, and `disconnect`:

```python
@sio.on('message')
def handle_message(sid, message):
    # Broadcast the received message to all connected clients.
    sio.emit('message', message, broadcast=True)

@sio.on('connect')
def handle_connect(sid):
    # Log the connection.
    print('Client connected: {}'.format(sid))

@sio.on('disconnect')
def handle_disconnect(sid):
    # Log the disconnection.
    print('Client disconnected: {}'.format(sid))
```

3. **Run the Socket.IO Server**

Use an external WSGI server (e.g., `eventlet` or `gevent`) to serve the Socket.IO app. For example, to serve the app on port 5000, you would use the following command:

```
gunicorn -b 0.0.0.0:5000 socketio_chat:app
```

**Terminal-based Client-side Algorithm**

1. **Initialize Client**

Import the necessary library:

```python
import socketio
```

2. **Connect to Server**

Create a Socket.IO connection to the server:

```python
sio = socketio.Client()
sio.connect('http://localhost:5000')
```

3. **Define Event Handlers**

Define event handlers for Socket.IO events such as `message`:

```python
@sio.on('message')
def handle_message(message):
    # Print the received message to the terminal.
    print(message)
```

4. **User Interaction**

Use the terminal to get user input and send messages to the server:

```python
while True:
    # Get user input.
    message = input('> ')

    # Emit the 'message' event with the entered message.
    sio.emit('message', message)
```

5. **Run the Socket.IO Client**

Connect to the Socket.IO server:

```python
sio.connect('http://localhost:5000')
```

Run the Socket.IO client in the terminal:

```
while True:
    sio.wait()
```

6. **Disconnect from Server**

Optionally, disconnect from the server when the user decides to exit the chat:

```python
# Disconnect from the server.
sio.disconnect()
```

**Usage**

To start the server, run the following command in a terminal:

```
gunicorn -b 0.0.0.0:5000 socketio_chat:app
```

To start the client, open another terminal and run the following command:

```python
import socketio

sio = socketio.Client()
sio.connect('http://localhost:5000')

while True:
    message = input('> ')
    sio.emit('message', message)

while True:
    sio.wait()
```

You can now start chatting by typing messages into the terminal and pressing Enter. The messages will be sent to the server and broadcast to all connected clients.

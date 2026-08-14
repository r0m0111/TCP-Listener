# TCP Socket Echo Server

A simple Python TCP server that listens for incoming connections, receives data from a client, prints the received data, and sends the same data back to the client (echo server).


## RESULT
<img width="1206" height="707" alt="test" src="https://github.com/user-attachments/assets/8f0d9a31-6106-41ee-8fb0-3f6919b5b928" />



## Requirements

* Python 3.x
* A network connection between the client and server
* Port `6996` available on the server

## How It Works

The server:

1. Creates a TCP socket.
2. Binds to the configured IP address and port.
3. Waits for a client to connect.
4. Receives up to `100` bytes of data at a time.
5. Prints the received data.
6. Sends the data back to the client.
7. Closes the connection when the client disconnects.

## Configuration

```python
TCP_IP = "192.168.1.242"
TCP_PORT = 6996
BUFFER_SIZE = 100
```

### `TCP_IP`

Set this to the IP address of the computer running the server.

For local testing, you can use:

```python
TCP_IP = "127.0.0.1"
```

or:

```python
TCP_IP = "localhost"
```

For connections from another device on your network, use the server's local network IP address.

### `TCP_PORT`

The TCP port the server listens on:

```python
TCP_PORT = 6996
```

The client must connect to the same port.

### `BUFFER_SIZE`

The maximum amount of data received per `recv()` call:

```python
BUFFER_SIZE = 100
```

## Running the Server

Save the program as:

```text
server.py
```

Then run:

```bash
python server.py
```

The server will wait for an incoming TCP connection.

When a client connects, you should see something similar to:

```text
Connection address: ('192.168.1.100', 54321)
```

When the client sends data:

```text
Recieved data: b'Hello Server'
```

The server then sends the same data back to the client.

## Testing Locally

For testing on the same computer, change:

```python
TCP_IP = "127.0.0.1"
```

You can then connect to:

```text
127.0.0.1:6996
```

using a TCP client.

## Network Testing

If another computer is connecting to the server, make sure:

* Both devices are on the same network.
* The server IP address is correct.
* Port `6996` is allowed through the firewall.
* The client connects to the server's IP, not its own IP.
* The server is running before the client attempts to connect.

For example:

```text
Server IP: 192.168.1.242
Server Port: 6996
```

The client should connect to:

```text
192.168.1.242:6996
```

## Important Notes

This is a **single-client** example. The server calls:

```python
s.listen(1)
conn, addr = s.accept()
```

and handles one connection at a time. It does not create separate threads or processes for multiple clients.

The server also uses a fixed buffer size of 100 bytes. TCP is a stream protocol, so a single `recv(100)` does not necessarily correspond to one complete message.

For production or more advanced applications, consider adding:

* Multiple-client support
* Threads or `asyncio`
* Error handling
* Connection timeouts
* Graceful server shutdown
* Message framing
* Logging
* Input validation

## License

Use and modify this example freely for learning and personal projects.

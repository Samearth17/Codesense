# Server program

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 8888

# Bind to the port
server_socket.bind((host, port))

server_socket.listen(5)

print("Waiting for a connection...")

# Establish a connection with the client
client_socket, addr = server_socket.accept()

print("Received a connection from %s " % str(addr))

while True:
 data = client_socket.recv(1024).decode('utf-8')
 if not data:
   break
 print("Received from client: %s" %data)
 data = data.upper()
 print("Sending to client: %s" %data)
 client_socket.send(data.encode('utf-8'))

client_socket.close()

# Client program
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 8888

# Connect to server's socket
client_socket.connect((host, port))

message = input("Enter a message -> ")
# Send a message
client_socket.send(message.encode('utf-8'))

# Receive a message
data = client_socket.recv(1024).decode('utf-8')
print("Received from server: %s" %data)

client_socket.close()
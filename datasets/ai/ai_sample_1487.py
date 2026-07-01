import socket

# Create a socket object
s = socket.socket()

# Connect to local host
host = '127.0.0.1'
port = 8888
s.connect((host, port))

# Receive data from server
data = s.recv(1024)
print(data)

# Close the socket connection
s.close()
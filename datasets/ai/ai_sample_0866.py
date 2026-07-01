# Server:

import socket 

s = socket.socket()
host = '127.0.0.1'
port = 12345

s.bind((host, port))
s.listen(5)
while True:
 c, addr = s.accept()
 print('Got connection from', addr)
 c.send(b'Thank you for connecting!')
 message = c.recv(1024)
 print('Received:', message)
 c.close()

# Client: 

import socket 

s = socket.socket()
host = '127.0.0.1'
port = 12345

s.connect((host, port))
print(s.recv(1024))
s.send(b'Hello, this is client!')
s.close()
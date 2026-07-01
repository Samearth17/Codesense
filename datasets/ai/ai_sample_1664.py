import socket
import os

from cryptography.fernet import Fernet

# generate an encryption key
key = Fernet.generate_key()

# create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket
sock.bind(('127.0.0.1', 8080))

# wait for incoming connections
sock.listen()
conn, addr = sock.accept()

with conn:
 print('Connected by', addr)
 while True:
 # get the incoming message
 msg = conn.recv(1024)

 # decrypt the message with the key
 f = Fernet(key)
 decrypted_msg = f.decrypt(msg)

 # do something with the message
 print('Message:', decrypted_msg)

 # send a reply
 reply = 'Thanks for the message'
 encrypted_reply = f.encrypt(reply)
 conn.sendall(encrypted_reply)
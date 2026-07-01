import socket

# Create a TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_1_address = ('localhost', 10000)
server_2_address = ('localhost', 20000)
s.bind(server_1_address)
s.bind(server_2_address)

# Listen for incoming connections
s.listen(1)

while True:
    # Wait for a connection
    connection_1, client_address_1 = s.accept()
    connection_2, client_address_2 = s.accept()

    try:
        print("Connection from:", client_address_1, "and", client_address_2)

        # Receive the data in small chunks and retransmit it
        while True:
            data_1 = connection_1.recv(1024, 0)
            data_2 = connection_2.recv(1024, 0)
            if data_1:
                connection_1.sendall(data_1, 0)
            if data_2:
                connection_2.sendall(data_2, 0)
            else:
                break

    finally:
        # Clean up the connection
        connection_1.close()
        connection_2.close()
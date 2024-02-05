#UDP Server Side

import socket

#Create a server side socket IPv4 (AF_INET) and UDP (SOCK_DGRAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Bind our new socket to a tuple (IP address, port address)
IPv4 = socket.gethostbyname(socket.gethostname())
port = 12345
server_socket.bind((IPv4, port))

#We are not listening or accepting connections since UDP is a connectionless protocol
message, address = server_socket.recvfrom(1024)
print(message.decode("utf-8"))
print(address)

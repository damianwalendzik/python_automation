#TCP client side

import socket

#Create a client side IPv4 (AF_INET) and TCP (SOCK_STREAM) socket 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect the socket to a server located at a given IP and Port
port = 12345
IPv4 = socket.gethostbyname(socket.gethostname())
client_socket.connect((IPv4, port))




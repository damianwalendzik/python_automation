#TCP client side

import socket

#Create a client side IPv4 (AF_INET) and TCP (SOCK_STREAM) socket 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect the socket to a server located at a given IP and Port
IPv4 = socket.gethostbyname(socket.gethostname())
port = 12345
client_socket.connect((IPv4, port))

#Receive a message from the server. You mustspecify the max number of bytes to receive within the message.
message=client_socket.recv(1024)
print(message.decode("utf-8"))


#Close the client socket.
client_socket.close()



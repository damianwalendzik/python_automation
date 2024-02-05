#TCP Server Side

import socket

#Create a server side socket using IPv4 (AF_INET) and TCP (SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Hence it is TCP socket, we need to define a place where socket should listen. using bing method 

#See how to get IP address dynamically
print(socket.gethostname()) #hostname
print(socket.gethostbyname(socket.gethostname())) #ip of a given hostname

#Bind our new socket to a tuple (IP Address, Port Address)
port = 12345
IPv4 = socket.gethostbyname(socket.gethostname())
server_socket.bind((IPv4, port))

#Put the socket into listening mode to listen for any possible connections
server_socket.listen()

#listen forever to accept ANY connection
while True:
    #Accept every single connection and store two pieces of information
    client_socket, client_address = server_socket.accept()
    print(type(client_socket))
    print(client_socket)
    print(type(client_address))
    print(client_address)

    print(f"Connected to {client_address}!\n")

#Send a message to the client that just connected
client_socket.send("You are connected.".encode("utf-8"))
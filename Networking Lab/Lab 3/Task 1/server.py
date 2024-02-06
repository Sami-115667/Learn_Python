import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)
print(socket.gethostname())

while True:
    try:
        clientsocket, address = s.accept()
        print(f"Connection from {address} has been established")
        
        msg = clientsocket.recv(1024)
        msg_decoded = msg.decode()
        msg_lowercase = msg_decoded.lower()
        print("I am receiving the message from client: " + msg_decoded)
        clientsocket.sendall(msg_lowercase.encode())  
    except Exception as e:
        print(f"Error: {e}")

    finally:
        clientsocket.close()  # Close the client socket

import socket
import threading

def handle_client(client_socket):

    # msg = client_socket.recv(1024).decode()

    # response = "pdf1.pdf,pdf.pdf,sami.txt"
    # client_socket.send(response.encode())

    msg1=client_socket.recv(1024).decode()
    print(msg1)
    
   
    # try:
    #     with open(msg, 'rb') as f:
    #         data = f.read(1024)
    #     while data:
    #         client_socket.send(data)
    #         data = f.read(1024)
    # except FileNotFoundError:
    #     print("File not found!")
    # finally:

    client_socket.close()

def server():
    #server_address = (socket.gethostname(), 1234)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('',1234))
    s.listen(6)
    print("Server is listening for incoming connections...")
    while True:
        c, address = s.accept()
        print("connectioned")
        client_thread = threading.Thread(target=handle_client, args=(c,))
        client_thread.start()

if __name__ == "__main__":
    server()

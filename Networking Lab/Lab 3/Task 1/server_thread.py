import socket
import threading
import os

def handle_client(client_socket,address):
    
    msg = client_socket.recv(1024).decode()
    print(msg)
    response = "This file are avaiable : pdf1.pdf,pdf.pdf,sami.txt"
    client_socket.send(response.encode())
    msg1 = client_socket.recv(1024)
    msg1 = msg1.decode()
    print(msg1)
    file_path = os.path.join(r"F:\Python\Python\Networking Lab\Lab 3\Task 1", msg1)
  

    try:
        with open(file_path, 'rb') as f:
            while True:
                data = f.read(1024)
                if not data:
                    break
                client_socket.sendall(data)
        
        f.close()
        response1="File transfer Successfully"
        client_socket.send(response1.encode())
        print(response1)
    # except FileNotFoundError:
    #     print("File not found!")
    except Exception as e:
        print("Error occurred during file transmission:", e)
    finally:
        client_socket.close()

  

    

    # with open(file_path, 'rb') as file:
    # # Your file handling code here


    # # file =open("sami.txt","rb")
    #     dd=file.read()
    #     client_socket.sendall(dd)
    #     file.close()
    # client_socket.close()



def server():
    #server_address = (socket.gethostname(), 1234)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(),1234))
    s.listen()
    print("Server is listening for incoming connections...")

    while True:
        
        client_socket, address = s.accept()
        print("connection Successfull")
        client_thread = threading.Thread(target=handle_client, args=(client_socket,address))
        client_thread.start()

if __name__ == "__main__":
    server()

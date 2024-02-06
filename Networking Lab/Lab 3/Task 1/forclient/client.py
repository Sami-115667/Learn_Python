import socket
import threading

def client():
    # There in socket.gethosname() use the appropriate server ip address.
    server_address = (socket.gethostname(), 1234)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect(server_address)

    message = "GIVE ME FILE NAME?"
    s.send(message.encode())


    msg = s.recv(1024).decode()
    print("After receiving data from server: " + msg)

    print("Write the selected file with extension")
    message1 = input()
    s.send(message1.encode())

   

    with open (message1,'wb')as file:
        dataa=s.recv(1024)
        while dataa:
            file.write(dataa)
            dataa=s.recv(1024)
        file.close()
    # ss=s.recv(1024).decode()
    # print(ss)

    
    s.close()


num_clients = 1

# Create and start threads for each client
threads = []
for _ in range(num_clients):
    t = threading.Thread(target=client)
    threads.append(t)
    t.start()
    


for t in threads:
    t.join()
    
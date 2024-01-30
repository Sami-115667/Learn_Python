import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)
print(socket.gethostname())

while True:
    try:
        clientsocket, address = s.accept()
        print(f"Connection from {address} has been established")
       # clientsocket.send(bytes("Welcome ", "utf-8"))
        msgg= clientsocket.recv(1024)
        sami=msgg.decode("utf-7")
        samiii =sami.lower()
        print("I am receiving the message form client= " +sami)
        clientsocket.send(bytes(samiii, "utf-8"))

        #check_palindrome(samiii)
        #clientsocket.send(bytes(check_palindrome(samiii), "utf-8"))
        #samii=sami
       # print("sami")
        print(sami)
        
    except Exception as e:
        print(f"Error: {e}")


    clientsocket.close()



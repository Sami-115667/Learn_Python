import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)
count=0
strr=""

while True:
    try:
        clientsocket, address = s.accept()
        print(f"Connection from {address} has been established")
      
        msgg= clientsocket.recv(1024)
        x=(msgg.decode())
        
        
       
        strr=strr+x
        print(strr) 
        #if x>=3:
        clientsocket.sendall(strr.encode())
    
        #else:
        #    clientsocket.sendall("Error".encode())
            

        
    except Exception as e:
        print(f"Error: {e}")


    clientsocket.close()



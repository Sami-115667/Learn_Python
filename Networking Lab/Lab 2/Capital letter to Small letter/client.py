import socket

#socket first
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("Sami", 1234))
message = "HELLO SERVER"
s.send(message.encode('utf-7'))

msg= s.recv(1024)
print("Sending  data from client :"+ message)

print("After receiving Data Fron Server : "+msg.decode("utf-8"))
s.close()




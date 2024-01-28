import socket

#socket first
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("Sami", 1234))
message = "hello server"
s.send(message.encode('utf-7'))

msg= s.recv(1024)
print("Sending  data from client :"+ message)

print("After receiving Data Fron Server : "+msg.decode("utf-8"))
s.close()



#second socket 
s1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s1.connect(("Sami", 1234))
message1 = "123321"
print("Sending  palindrome input :"+ message1)
s.send(message1.encode('utf-7'))
msg1= s.recv(1024)
print(msg1.decode("utf-8"))
s1.close()
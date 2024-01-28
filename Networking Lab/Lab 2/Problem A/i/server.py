import socket
samii=""






s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(2)

while True:
    try:
        clientsocket, address = s.accept()
        print(f"Connection from {address} has been established")
       # clientsocket.send(bytes("Welcome ", "utf-8"))
        msgg= clientsocket.recv(1024)
        sami=msgg.decode("utf-7")
        samiii =sami.upper()
        print("I am receiving the message form client= " +sami)
        clientsocket.send(bytes(samiii, "utf-8"))

        #check_palindrome(samiii)
        #clientsocket.send(bytes(check_palindrome(samiii), "utf-8"))
        #samii=sami
       # print("sami")
        print(sami)
        
    except Exception as e:
        print(f"Error: {e}")


#msgg= clientsocket.recv(1024)
#sami=msgg.decode("utf-7")
#clientsocket.send(bytes(msgg, "utf-6"))

#clientsocket.send(bytes(msgg, "utf-5"))

clientsocket.close()


#print(samii)
def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    # Compare the string with its reverse
    return s == s[::-1]




ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind((socket.gethostname(), 1234))
ss.listen(2)

while True:
    try:
        clientsocket1, address1 = ss.accept()
        print(f"Connection from {address1} has been established")
        msgg= clientsocket1.recv(1024)
        sa=msgg.decode("utf-7")
        sam= is_palindrome(sa)
        clientsocket1.send(bytes(sam, "utf-8"))
     
    except Exception as e:
        print(f"Error: {e}")






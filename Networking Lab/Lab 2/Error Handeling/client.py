import socket
import random

# Socket creation and connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))
count = 0

try:
    for x in range(1, 10):
        number = random.randint(0, 10)
        s.sendall(str(number).encode())
          
    #s.sendall("clear".encode())    
    response = s.recv(1024).decode() 
    for digit_char in response:
        digits = int(digit_char)
        if digits > 2:
            count += 1
    print(response)
    print("The Error is ", (100 - (count * 10)), "%")

finally:
    s.close()

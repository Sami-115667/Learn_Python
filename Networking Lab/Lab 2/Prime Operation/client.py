import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("Sami", 1234))

try:
    request = int(input("Enter a number: "))

    s.sendall(str(request).encode())
    response = s.recv(1024).decode()
    print("The number is ",request," "+response)

finally:
    s.close()

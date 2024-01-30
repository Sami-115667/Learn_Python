import socket

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    connection, address = s.accept()
    print(f"Connection from {address} has been established")
    try:
        data = connection.recv(1024)
        data = int(data.decode())
        success = is_prime(data)
        if success:
            connection.sendall("It is a prime number".encode())
        else:
            connection.sendall("It is not a prime number".encode())
    finally:
        connection.close()

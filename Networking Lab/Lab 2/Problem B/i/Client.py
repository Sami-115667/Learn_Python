import socket

# Function to perform withdrawal
def withdraw(client_socket, card_number, password, amount):
    request = f"{card_number},{password},WITHDRAW,{amount}"
    client_socket.sendall(request.encode())
    response = client_socket.recv(1024).decode()
    return response.split(',')

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((socket.gethostname(), 1234))
print(socket.gethostname())

try:
    # Example withdrawal request
    card_number = "123456789"
    password = "1234"
    amount = 500

    # Send withdrawal request to the server
    response_code, message = withdraw(client_socket, card_number, password, amount)

    # Process the response
    if response_code == "SUCCESS":
        print(f"Withdrawal successful. Updated balance: {message}")
    else:
        print(f"Withdrawal failed: {message}")

finally:
    # Clean up the connection
    client_socket.close()

import socket


accounts = {
    "123456789": {"password": "1234", "balance": 1000}
}

def process_withdrawal(card_number, password, amount):
    if card_number in accounts and accounts[card_number]["password"] == password:
        if accounts[card_number]["balance"] >= amount:
            accounts[card_number]["balance"] -= amount
            return True, accounts[card_number]["balance"]
        else:
            return False, "Insufficient funds"
    else:
        return False, "Invalid card number or password"




s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5)


while True:
    connection,address = s.accept()
    print(f"Connection from {address} has been established")

    try:
        
        # Receive the data from the ATM
        data = connection.recv(1024)
        data = data.decode().split(',')

        if len(data) == 4:
            # Process the received data
            card_number, password, operation, amount = data

            if operation == "WITHDRAW":
                success, response = process_withdrawal(card_number, password, int(amount))
                if success:
                    # Send success response to ATM
                    connection.sendall(f"SUCCESS,{response}".encode())
                else:
                    # Send failure response to ATM
                    connection.sendall(f"FAILURE,{response}".encode())
            else:
                connection.sendall("FAILURE,Invalid operation".encode())
        else:
            connection.sendall("FAILURE,Invalid request format".encode())

    finally:
        # Clean up the connection
        connection.close()
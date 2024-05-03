import socket

def main():
    try:
        # Create a server socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('localhost', 1234))
        server_socket.listen(1)
        print("Server started and listening on port 1234...")

        # Accept client connection
        client_socket, addr = server_socket.accept()
        print("Client connected: ", addr)

        # Receive the MSS from client
        mss = 1024

        # Initialize congestion control variables
        cwnd = mss
        ssthresh = 100000
        dup_ack_count = 0

        # Receive file data from client
        file_data = bytearray()
        ack = 0
        while True:
            segment = client_socket.recv(cwnd)
            if not segment:
                break
            # Simulate packet loss by dropping the 3rd packet
            if dup_ack_count == 2:
                print("Simulating packet loss...")
                dup_ack_count = 0
                continue
            # Write data to file and send ACK
            file_data.extend(segment)
            ack += len(segment)
            print("Next ack:", ack)
            client_socket.sendall(ack.to_bytes(4, 'big'))  # Sending ACK
            # Update congestion control variables
            if cwnd < ssthresh:
                cwnd += mss
            else:
                cwnd += (mss * mss) // cwnd

        print("File received successfully.")

        # Write data to a file
        with open("b.txt", "wb") as file:
            file.write(file_data)

        # Close the sockets
        client_socket.close()
        server_socket.close()

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()

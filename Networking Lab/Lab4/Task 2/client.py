import socket
import struct

def main():
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 5000)

    # Sending Domain to Local DNS Server
    domain = "www.cse.du.ac.bd"
    print("Sent Domain:", domain)
    message_bytes = domain.encode('utf-8')
    message_length = len(message_bytes)

    # Packing data into byte array
    send_data = struct.pack("!HBBi", 1, 2, 2, message_length) + message_bytes

    socket_client.sendto(send_data, server_address)

    # Receiving IP from the Local DNS Server
    receive_data, server = socket_client.recvfrom(1024)
    message_length, = struct.unpack("!i", receive_data[:4])
    IP = receive_data[4:message_length + 4].decode('utf-8')
    print("Received IP:", IP)

    socket_client.close()

if __name__ == "__main__":
    main()

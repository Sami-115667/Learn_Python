import socket
import struct

def main():
    # Create a UDP socket
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_server.bind(('10.42.0.74', 7000))

    # Receive message from Local DNS Server
    receive_data, address = socket_server.recvfrom(1024)
    message_length = struct.unpack('!I', receive_data[:4])[0]
    domain = receive_data[4:4+message_length].decode('utf-8')
    print("Received from Local DNS:", domain)

    # Sending message to Local DNS Server
    IP = "0.0.0.1"
    message_bytes = IP.encode('utf-8')
    message_length = len(message_bytes)

    buffer = struct.pack('!HBBI', 1, 2, 2, message_length) + message_bytes

    print("Sending to Local DNS:", IP)
    socket_server.sendto(buffer, ('10.42.0.74', 5000))

    socket_server.close()

if __name__ == "__main__":
    main()

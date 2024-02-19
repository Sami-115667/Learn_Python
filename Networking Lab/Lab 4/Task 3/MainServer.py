import socket
import struct

def main():
    # Receiving message from TLD DNS Server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('10.42.0.74', 9000))

    receive_data, address = server_socket.recvfrom(1024)
    received_buffer = memoryview(receive_data)

    message_length = struct.unpack('!I', received_buffer[:4])[0]
    domain = received_buffer[4:4+message_length].tobytes().decode('utf-8')
    print("Received from TLD DNS:", domain)

    # Sending message to TLD DNS Server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    ip = "1.1.1.1"
    message_bytes2 = ip.encode('utf-8')
    message_length2 = len(message_bytes2)

    print("Sending to TLD DNS:", ip)

    send_data = struct.pack('!HBBI', 1, 2, 2, message_length2) + message_bytes2

    client_socket.sendto(send_data, ('10.42.0.74', 9800))

    server_socket.close()
    client_socket.close()

if __name__ == "__main__":
    main()

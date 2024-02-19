import socket
import struct

def main():
    # Create a UDP socket
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_server.bind(('10.42.0.74', 9000))

    while True:
        # Receive message from Local DNS Server
        receive_data, address = socket_server.recvfrom(1024)
        message_length = struct.unpack('!I', receive_data[:4])[0]
        domain = receive_data[4:4+message_length].decode('utf-8')
        print("Receiving from local DNS:", domain)

        # Send message from Local DNS Server
        IP = "1.0.2.1"
        send_message(socket_server, ('10.42.0.74', 5000), IP)

    socket_server.close()

def send_message(socket_server, address, ip):
    message_bytes = ip.encode('utf-8')
    message_length = len(message_bytes)
    buffer = struct.pack('!HBBI', 1, 2, 2, message_length) + message_bytes
    print("Sending to Local DNS:", ip)
    socket_server.sendto(buffer, address)

if __name__ == "__main__":
    main()

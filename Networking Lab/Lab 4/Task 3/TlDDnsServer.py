import socket
import struct

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('10.42.0.74', 9800))

    # Receive message from Root DNS Server
    receive_data, root_dns_address = server_socket.recvfrom(1024)
    received_buffer = memoryview(receive_data)

    message_length = struct.unpack('!I', received_buffer[:4])[0]
    domain = received_buffer[4:4+message_length].tobytes().decode('utf-8')
    print("Received from Root DNS:", domain)

    # Send message to Auth DNS Server
    auth_dns_address = ('10.42.0.74', 9000)
    auth_ip = "1.1.0.0"

    print("Sending to Auth DNS:", auth_ip)

    message_bytes2 = auth_ip.encode('utf-8')
    message_length2 = len(message_bytes2)

    send_data = struct.pack('!HBBI', 1, 2, 2, message_length2) + message_bytes2

    server_socket.sendto(send_data, auth_dns_address)

    # Receive message from Auth DNS Server
    receive_data2, _ = server_socket.recvfrom(1024)
    received_buffer2 = memoryview(receive_data2)

    message_length3 = struct.unpack('!I', received_buffer2[:4])[0]
    domain2 = received_buffer2[4:4+message_length3].tobytes().decode('utf-8')
    print("Received from Auth DNS:", domain2)

    # Send message to Root DNS Server
    root_dns_ip = "1.1.1.1"

    print("Sending to Root DNS:", root_dns_ip)

    message_bytes5 = root_dns_ip.encode('utf-8')
    message_length5 = len(message_bytes5)

    send_data2 = struct.pack('!HBBI', 1, 2, 2, message_length5) + message_bytes5

    server_socket.sendto(send_data2, root_dns_address)

if __name__ == "__main__":
    main()

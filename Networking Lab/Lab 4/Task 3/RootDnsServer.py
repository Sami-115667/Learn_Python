import socket
import struct

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('10.42.0.74', 7000))

    # Receive message from Local DNS Server
    receive_data, local_dns_address = server_socket.recvfrom(1024)
    received_buffer = memoryview(receive_data)

    message_length = struct.unpack('!I', received_buffer[:4])[0]
    domain = received_buffer[4:4+message_length].tobytes().decode('utf-8')
    print("Received from Local DNS:", domain)

    # Send message to Root TLD DNS Server
    tld_dns_address = ('10.42.0.74', 9800)
    tld_ip = "0.0.1.0"

    print("Sending to TLD DNS:", tld_ip)

    message_bytes2 = tld_ip.encode('utf-8')
    message_length2 = len(message_bytes2)

    send_data = struct.pack('!HBBI', 1, 2, 2, message_length2) + message_bytes2

    server_socket.sendto(send_data, tld_dns_address)

    # Receive message from TLD DNS Server
    receive_data2, _ = server_socket.recvfrom(1024)
    received_buffer2 = memoryview(receive_data2)

    message_length3 = struct.unpack('!I', received_buffer2[:4])[0]
    domain2 = received_buffer2[4:4+message_length3].tobytes().decode('utf-8')
    print("Received from TLD DNS:", domain2)

    # Send message to Local DNS Server
    local_dns_ip = "1.1.1.1"

    print("Sending to Local DNS:", local_dns_ip)

    message_bytes5 = local_dns_ip.encode('utf-8')
    message_length5 = len(message_bytes5)

    send_data2 = struct.pack('!HBBI', 1, 2, 2, message_length5) + message_bytes5

    server_socket.sendto(send_data2, local_dns_address)

if __name__ == "__main__":
    main()

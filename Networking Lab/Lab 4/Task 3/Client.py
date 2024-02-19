import socket
import struct

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('10.42.0.224', 5000)

    # Sending Domain to Local DNS Server
    domain = "www.cse.du.ac.bd"
    print("Sending domain:", domain)
    message_bytes = domain.encode('utf-8')
    message_length = len(message_bytes)

    send_data = struct.pack('!HBBI', 1, 2, 2, message_length) + message_bytes

    client_socket.sendto(send_data, server_address)

    # Receiving IP from the Local DNS Server
    receive_data, _ = client_socket.recvfrom(1024)
    received_buffer = memoryview(receive_data)

    query_id2, query_type2, query_class2, message_length2 = struct.unpack('!HBBI', received_buffer[:8])
    message_bytes2 = received_buffer[8:8+message_length2].tobytes()
    received_ip = message_bytes2.decode('utf-8')

    print("Received IP:", received_ip)

    client_socket.close()

if __name__ == "__main__":
    main()

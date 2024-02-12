
import socket
import struct

def main():
    # Create a UDP socket
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_server.bind(('localhost', 5000))

    while True:
        # Receive message from client
        receive_data, address = socket_server.recvfrom(1024)
        message_length = struct.unpack('!I', receive_data[:4])[0]
        domain = receive_data[4:4+message_length].decode('utf-8')
        print("Received from client:", domain)

        # Send message to Root DNS Server
        root_dns_address = ('localhost', 7000)
        send_message(socket_server, root_dns_address, "0.0.0.0")

        # Receive message from Root DNS Server
        root_dns_response = receive_message(socket_server)

        # Send message to TLD DNS Server
        tld_dns_address = ('localhost', 9876)
        send_message(socket_server, tld_dns_address, "0.0.0.1")

        # Receive message from TLD DNS Server
        tld_dns_response = receive_message(socket_server)

        # Send message to Authoritative DNS Server
        auth_dns_address = ('localhost', 9000)
        send_message(socket_server, auth_dns_address, "0.0.1.0")

        # Receive message from Authoritative DNS Server
        auth_dns_response = receive_message(socket_server)

        # Send message back to client
        client_address = (address[0], 1234)
        send_message(socket_server, client_address, "0.0.1.0")

    socket_server.close()

def send_message(socket_server, address, ip):
    message_bytes = ip.encode('utf-8')
    message_length = len(message_bytes)
    buffer = struct.pack('!HBBI', 1, 2, 2, message_length) + message_bytes
    print("Sending to", address[0] + ":", ip)
    socket_server.sendto(buffer, address)

def receive_message(socket_server):
    receive_data, address = socket_server.recvfrom(1024)
    message_length = struct.unpack('!I', receive_data[:4])[0]
    ip = receive_data[4:4+message_length].decode('utf-8')
    print("Received from", address[0] + ":", ip)
    return ip

if __name__ == "__main__":
    main()

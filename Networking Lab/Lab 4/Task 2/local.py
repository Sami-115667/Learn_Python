
import socket
import struct

def main():
    # Create a UDP socket
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_server.bind(('10.42.0.74', 5000))

    while True:
        # Receive message from client
        receive_data, address = socket_server.recvfrom(1024)
        message_length = struct.unpack('!I', receive_data[:4])[0]
        domain = receive_data[4:4+message_length].decode('utf-8')
        print("Received from client:", domain)

        # Send message to Root DNS Server
        root_dns_address = ('10.42.0.74', 7000)
        send_message(socket_server, root_dns_address, domain)

        # Receive message from Root DNS Server
        root_dns_response = receive_message(socket_server)

        # Send message to TLD DNS Server
        tld_dns_address = ('10.42.0.74', 9876)
        send_message(socket_server, tld_dns_address, "0.0.0.1")

        # Receive message from TLD DNS Server
        tld_dns_response = receive_message(socket_server)

        # Send message to Authoritative DNS Server
        auth_dns_address = ('10.42.0.74', 9000)
        send_message(socket_server, auth_dns_address, "0.0.1.0")

        # Receive message from Authoritative DNS Server
        auth_dns_response = receive_message(socket_server)

        # Send message back to client
        #client_address = (address[0], 5000)
        send_message(socket_server, address, "0.0.1.0")

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

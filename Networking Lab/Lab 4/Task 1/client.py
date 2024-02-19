import socket

def string_to_binary(input_string):
    binary_representation = ' '.join(format(ord(char), '08b') for char in input_string)
    return binary_representation



udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = "mail.cse.du.ac.bd."

buffer = message.encode('utf-8')
server_address = ('10.42.0.74', 1500)


udp_socket.sendto(buffer, server_address)

buffer, server_address = udp_socket.recvfrom(1024)
response = buffer.decode('utf-8')

binary_result = string_to_binary(response)
print(f"Server Response : After Encode : {binary_result}")


print("Server response: After Decode : ", response)

udp_socket.close()
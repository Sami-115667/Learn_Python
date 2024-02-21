import socket
import struct

def to_header(seq_num, ack_num, ack, sf, rwnd):
    return struct.pack('!IIbbh', seq_num, ack_num, ack, sf, rwnd)

def from_header(segment):
    if len(segment) < 12:
        return None, None, None, None, None
    return struct.unpack('!IIbbh', segment)

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5000))
    server_socket.listen(1)
    client_socket, addr = server_socket.accept()
    recv_buffer_size = 12
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, recv_buffer_size)
    expected_seq_num = 0
    ack_num = 0
    received_data = bytearray()

    while True:
        header = client_socket.recv(12)
        seq_num, ack_num, ack, sf, rwnd = from_header(header)

        if seq_num is None:
            print("Header size is less than 12 bytes")
            break
        
        print("\nSeq Num: {}\nWindow Size: {}\nString sent: ".format(seq_num, rwnd))

        data = client_socket.recv(rwnd)
        if not data:
            break

        print(data.decode('utf-8'))

        seq_num = ack_num

        if seq_num == expected_seq_num:
            received_data.extend(data)
            ack_num += len(data)
            expected_seq_num += len(data)

            to_send_ack = to_header(seq_num, ack_num, 1, 0, 12)
            client_socket.send(to_send_ack)
        else:
            to_send_ack = to_header(seq_num, ack_num, 1, 0, 12)
            client_socket.send(to_send_ack)

    received_data_str = received_data.decode('utf-8')
    print(received_data_str)

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()

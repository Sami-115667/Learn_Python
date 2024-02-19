import socket
import struct

def to_header(seq_num, ack_num, ack, sf, rwnd):
    return struct.pack('!IIBBH', seq_num, ack_num, ack, sf, rwnd)

def from_header(segment):
    return struct.unpack('!IIBBH', segment)

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((socket.gethostname(), 5000))
    server_socket.listen(1)

    client_socket, addr = server_socket.accept()
    recv_buffer_size = 1
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, recv_buffer_size)
    expected_seq_num = 0
    received_data = bytearray()
    #print(received_data)

    while True:
        header = client_socket.recv(12)
        if not header:
            break

        seq_num, ack_num, ack, sf, rwnd = from_header(header)

        data = client_socket.recv(rwnd)
        if not data:
            break
        
        message=f"\nSeq Num: {seq_num}\nWindow Size: {rwnd}\nString sent: "
        print(message)
        #client_socket.send(message)

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

    received_data_str = received_data.decode("UTF-8")
    print(received_data_str + "\n")

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()

import socket
import struct
import time

def to_header(seq_num, ack_num, ack, sf, rwnd):
    return struct.pack('!IIbbh', seq_num, ack_num, ack, sf, rwnd)

def from_header(segment):
    return struct.unpack('!IIbbh', segment)

def main():
    # Establish connection with the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5000))
    recv_buffer_size = 2
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, recv_buffer_size)

    # Initialize sequence number and expected acknowledgment number
    seq_num = 0
    expected_ack_num = 0

    # Data to be sent
    data = "This is a sample test message send to the Sever to check the control algorithm."
    print("String to be sent:", data)
    data_len = len(data)

    # Timeout value in seconds
    timeout = 2000
    start_time = time.time()

    # Sending data to the server
    while expected_ack_num < data_len:
        send_size = min(1, data_len - expected_ack_num)
        header = to_header(seq_num, expected_ack_num, 1, 0, send_size)
        message = data[seq_num:seq_num + send_size].encode()
        segment = header + message

        # Sending the segment to the server
        client_socket.sendall(segment)

        # Receiving acknowledgment from the server
        ack_header = client_socket.recv(12)
        ack_num = from_header(ack_header)[1]

        # Updating sequence number and expected acknowledgment number
        seq_num += send_size
        expected_ack_num = ack_num

        # Handling timeout
        if time.time() - start_time > timeout:
            seq_num = expected_ack_num
            start_time = time.time()

    # Closing the socket
    client_socket.close()

if __name__ == "__main__":
    main()

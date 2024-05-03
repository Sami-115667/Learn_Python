import socket
import struct
import random
import time

def to_header(seq_num, ack_num, ack, sf, rwnd):
    return struct.pack('!IIbbh', seq_num, ack_num, ack, sf, rwnd)

def from_header(segment):
    return struct.unpack('!IIbbh', segment)

def duplicate_acks():
    random_number = random.randint(10, 99)
    print(random_number)
    return random_number < 10

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5000))
    recv_buffer_size = 2
    window_size = 4 * recv_buffer_size
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, recv_buffer_size)

    window = []

    cwnd = 1
    ssthrs = 8
    flag = 0

    seq_num = 0
    expected_ack_num = 0

    data = "This is a sample test message sent to the Server to check the control algorithm."
    data_len = len(data)

    timeout = 2  # in seconds
    start_time = time.time()

    while expected_ack_num < data_len:

        if cwnd <= ssthrs and flag == 0:
            window_size = cwnd
            if cwnd * 2 <= ssthrs:
                cwnd *= 2
            else:
                flag = 1
                cwnd = ssthrs
        else:
            if not duplicate_acks():
                cwnd += 1
                window_size = cwnd
            else:
                ssthrs = cwnd // 2 - 1
                cwnd = 1
                flag = 0
                window_size = cwnd
                if cwnd * 2 <= ssthrs:
                    cwnd *= 2
                print("Duplicate Acks received...")

        rtt_start_time = time.time()

        send_size = min(window_size, data_len - expected_ack_num)

        header = to_header(seq_num, expected_ack_num, 1, 0, send_size)
        message = data[seq_num:seq_num + send_size].encode('utf-8')
        segment = header + message

        client_socket.send(segment)

        ack_header = client_socket.recv(12)

        #estimated_rtt = 0.2
        #alpha = 0.125
        #dev_rtt = 0.2
        #beta = 0.125

        rtt_end_time = time.time()

        duration = (rtt_end_time - rtt_start_time) * 1000
        sample_rtt = duration

       # estimated_rtt = (1 - alpha) * estimated_rtt + alpha * sample_rtt

        #dev_rtt = (1 - beta) * dev_rtt + beta * (sample_rtt - estimated_rtt)

        #rto = estimated_rtt + 4 * dev_rtt

        print("RTT: {:.3f} ms\n"
              .format(sample_rtt))

        ack_num = from_header(ack_header)[1]

        print("The cumalitive ack:",ack_num)

        seq_num += send_size
        expected_ack_num = ack_num

        if (time.time() - start_time) > timeout:
            seq_num = expected_ack_num
            start_time = time.time()

    client_socket.close()

if __name__ == "__main__":
    main()

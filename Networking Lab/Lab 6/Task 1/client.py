import socket
import os
import math
import time

mss = 1024

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost",1234))

cwnd = mss
ssthresh = float('inf')
dup_ack_count = 0

file_name = os.path.join(r"F:\Python\Python\Networking Lab\Lab 6\Task 1", "b.txt")
#file_name ="b"

file_size = os.path.getsize(file_name)

num_segments = math.ceil(file_size / mss)
print("Number of segments:", num_segments)

with open(file_name, "rb") as file_in:
    file_data = file_in.read()

print("Total file size:", num_segments * mss, "bytes")

ack = 0
current_segment = 0
ack_count = 0
start_time = time.time()

while ack < file_size:
    offset = ack
    segment_size = min(file_size - ack, cwnd)
    print("ack:", ack, "sz:", segment_size)
    client_socket.sendall(file_data[offset:offset + segment_size])
    
    try:
        ack_data = client_socket.recv(1024)
        ack = int.from_bytes(ack_data, byteorder='big')
        
        print("Received ACK:", ack)
        ack_count += 1
        dup_ack_count = 0
        
        if cwnd < ssthresh:
            cwnd += mss  # increase cwnd in slow start
        else:
            cwnd += (mss * mss) // cwnd  # increase cwnd in congestion avoidance
    except socket.timeout:
        print("Packet loss detected")
        ssthresh = cwnd // 2
        cwnd = ssthresh + 3 * mss
        dup_ack_count = 0
        current_segment -= ack_count
        ack_count = 0

    current_segment += 1

client_socket.close()

end_time = time.time()
total_time = end_time - start_time
throughput = (file_size / total_time) * 1000 / 1024  # Mbps
print("Transmission time:", total_time * 1000, "ms")
print("Throughput:", throughput, "Mbps")

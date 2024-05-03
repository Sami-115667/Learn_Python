import socket
import pickle
import time
from collections import deque
import array as arr
import numpy as np

MAX = float('inf')

def compare_sub_arrays(A, B, i1, j1, i2, j2):
    for k in range(len(A[0][0])):
        if A[i1][j1][k] != B[i2][j2][k]:
            return False
    return True

def print_3D_array(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            for k in range(len(arr[i][j])):
                x = arr[i][j][k]
                if x == MAX:
                    print("∞ ", end="")
                else:
                    print(x, end=" ")
            print()
        print()

def dijkstra(router, graph, source):
    count = 4
    visited_vertex = [False] * count
    distance = [MAX] * count

    distance[source] = 0

    for _ in range(count):
        u = find_min_distance(distance, visited_vertex)
        visited_vertex[u] = True

        for v in range(count):
            if not visited_vertex[v] and graph[u][v] != 0 and graph[u][v] != MAX \
                    and (distance[u] + graph[u][v] < distance[v]):
                distance[v] = distance[u] + graph[u][v]

    for i in range(count):
        if router[i] != distance[i]:
            router[i] = distance[i]

def find_min_distance(distance, visited_vertex):
    min_distance = MAX
    min_distance_vertex = -1
    for i in range(4):
        if not visited_vertex[i] and distance[i] < min_distance:
            min_distance = distance[i]
            min_distance_vertex = i

    return min_distance_vertex

if __name__ == "__main__":
    starttime = time.time()
    duration = 0

    D = [
        [0, 2, 7, MAX],
        [2, 0, 1, 3],
        [7, 1, 0, 2],
        [MAX, 3, 2, 0]
    ]

    Router = [
        [[0, 2, 7, MAX], [MAX, MAX, MAX, MAX], [MAX, MAX, MAX, MAX], [MAX, MAX, MAX, MAX]],
        [[MAX, MAX, MAX, MAX], [2, 0, 1, 3], [MAX, MAX, MAX, MAX], [MAX, MAX, MAX, MAX]],
        [[MAX, MAX, MAX, MAX], [MAX, MAX, MAX, MAX], [7, 1, 0, 2], [MAX, MAX, MAX, MAX]],
        [[MAX, MAX, MAX, MAX], [MAX, MAX, MAX, MAX], [MAX, MAX, MAX, MAX], [MAX, 3, 2, 0]]
    ]

    port = [5000, 6000, 7000, 8000]

    adj = [
        [1, 2],
        [0, 2, 3],
        [0, 1, 3],
        [1, 2]
    ]

    send = [[] for _ in range(4)]
    for i in range(4):
        send[i].append(i)

    queue = deque()
    rqueue = deque()
    flag = 0

    while True:
        change = 0

        for i in range(4):
            send[i].clear()
            send[i].append(i)

        queue.append(0)

        i = 0

        while queue:
            xyz = queue.popleft()
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            for ii in range(4):
                s.sendto(pickle.dumps(Router[ii]), ("localhost", port[ii]))
                s.sendto(str(xyz + 1).encode(), ("localhost", port[ii]))
                time.sleep(1)

            for j in range(len(send[xyz])):
                for k in range(len(adj[xyz])):
                    x = send[xyz][j]
                    y = adj[xyz][k]

                    if not compare_sub_arrays(Router, Router, xyz, x, y, x):
                        Router[y][x] = Router[xyz][x].copy()
                        if y not in queue:
                            queue.append(y)

                    if x not in send[y]:
                        send[y].append(x)

            if time.time() - starttime >= 10 and flag == 0:
                Router[1][1][3] = 2
                D[1][3] = 2
                D[2][0] = 2
                rqueue.append(1)

                while queue:
                    value = queue.popleft()
                    if value != 1:
                        rqueue.append(value)

                queue.extend(rqueue)
                flag = 1
                print("Values changed\n")
                print_3D_array(Router)

            i += 1

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        for ii in range(4):
            s.sendto(pickle.dumps(Router[ii]), ("localhost", port[ii]))
            s.sendto(str(5).encode(), ("localhost", port[ii]))
            time.sleep(1)

        print("Dijkstra started")

        for a in range(4):
            dijkstra(Router[a][a], D, a)
            i += 1

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        value = 1 if change == 1 else 0

        for ii in range(4):
            s.sendto(pickle.dumps(Router[ii]), ("localhost", port[ii]))
            s.sendto(str(change).encode(), ("localhost", port[ii]))

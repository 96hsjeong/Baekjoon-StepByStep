import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())

graph = {node: {} for node in range(1, V + 1)}

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().rstrip().split())

    if v in graph[u] and graph[u][v] < w:
        continue

    graph[u][v] = w

distances = {node: float('inf') for node in range(1, V + 1)}
distances[K] = 0

queue = []
heapq.heappush(queue, (distances[K], K))

while queue:
    current_distance, current_node = heapq.heappop(queue)

    if distances[current_node] < current_distance:
        continue

    for adjacent, weight in graph[current_node].items():
        distance = current_distance + weight

        if distance < distances[adjacent]:
            distances[adjacent] = distance
            heapq.heappush(queue, (distance, adjacent))

for i in range(1, V + 1):
    if distances[i] == float('inf'):
        print('INF')
    else:
        print(distances[i])
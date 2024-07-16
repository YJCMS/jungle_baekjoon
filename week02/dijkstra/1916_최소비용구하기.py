import sys
import heapq

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor_vertex, neighbor_distance in graph[current_vertex].items():
            new_distance = current_distance + neighbor_distance

            if new_distance < distances[neighbor_vertex]:
                distances[neighbor_vertex] = new_distance
                heapq.heappush(pq, (new_distance, neighbor_vertex))
    
    return distances

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = {i: {} for i in range(1, n+1)}

# 같은 노선의 가중치가 한번 더 들어올 때 비교해서 작은 값을 넣는 코드가 필요함
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    # graph[a][b]에 이미 값이 있으면 새로운 c와 기존 값 중 작은 값을 저장
    if b in graph[a]:
        graph[a][b] = min(graph[a][b], c)
    else:
        graph[a][b] = c

start, stop = map(int, sys.stdin.readline().split())

distances = dijkstra(graph, start)

print(distances[stop])

# 반례
# 2
# 2
# 1 2 1
# 1 2 5
# 1 2
# 1


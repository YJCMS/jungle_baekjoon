import sys
import heapq  # 우선순위 큐 구현을 위함

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]  # 우선순위 큐(최소 힙), (거리, 정점) 형태의 튜플을 저장
    
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

n, m, k, x = map(int, sys.stdin.readline().split())

graph = {i: {} for i in range(1, n+1)}

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1  # 문제에서 주어진 간선의 가중치는 모두 1로 가정

distances = dijkstra(graph, x)

result = []

for node, distance in distances.items():
    if distance == k :
        result.append(node)

if result:
    for city in result:
        print(city)
else:
    print(-1)




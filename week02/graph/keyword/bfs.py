import sys
from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return visited

graph = {
    1: [2, 3, 4],
    2: [5, 6],
    3: [],
    4: [7, 8],
    5: [],
    6: [],
    7: [],
    8: []
}

# BFS 실행
start_node = 1
visited_nodes = bfs(graph, start_node)
print(visited_nodes)  # BFS 탐색 순서 출력
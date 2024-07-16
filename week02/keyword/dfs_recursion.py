
visited = []
def dfs_recursive(graph, start):
    # 이미 방문한 노드라면 탐색 종료
    if start in visited:
        return
    
    # 방문 표시
    visited.append(start)
    print(start, end=' ')

    # 인접 정점들에 대해 재귀 호출
    for now in graph[start]:
        dfs_recursive(graph, now)

graph = {
    'A': ['B'],
    'B': ['A', 'H', 'C'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}

print(dfs_recursion(graph, 'A'))
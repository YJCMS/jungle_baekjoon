# 그래프를 인접 리스트로 표현
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [],
    5: [],
    6: [],
    7: []
}

# 각 노드의 방문 여부를 저장하는 리스트
visited = set()

def dfs(node):
    if node not in visited:
        print(node, end=' ')  # 현재 노드 출력
        visited.add(node)  # 현재 노드를 방문 처리
        
        for neighbor in graph[node]:
            dfs(neighbor)  # 인접한 노드에 대해 재귀 호출

# 시작 노드를 1로 설정하여 DFS 수행
dfs(1)
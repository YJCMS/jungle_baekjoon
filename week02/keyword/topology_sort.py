from collections import deque

# 위상정렬 Kahn's Algorithm
def topology_sort():
    result = []
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
 
    for i in result:
        print(i, end=' ')

n, m = map(int, sys.stdin.readline().split())
# 노드에 대한 진입차수를 담을 indegree를 0으로 초기화
indegree = [0] * (n+1)
graph = [[] for i in range(n+1)]

# 방향그래프 간선정보 입력받기
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1

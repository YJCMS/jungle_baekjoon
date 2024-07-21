# 최소신장트리(MST) 
import sys
 
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]
 
# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
 
 # 노드의 개수와 간선(Union 연산)의 개수 입력 받기
input = sys.stdin.readline
v, e = map(int, input().split())
parent = [0] * (v + 1)

# 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
for i in range(1, v + 1):
    parent[i] = i

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
edges = []
result = 0

# 모든 간선에 대한 정보를 입력 받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((a, b, cost))

# 간선을 비용 순으로 정렬
edges.sort(key=lambda x: x[2])
 
# 간선을 하나씩 확인하며, 
for edge in edges:
    a, b, cost = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
 
print(result)
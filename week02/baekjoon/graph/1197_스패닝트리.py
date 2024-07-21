import sys

n, m = map(int, sys.stdin.readline().split())

tree = []
for _ in range(m):
    tree.append(list(map(int, sys.stdin.readline().split())))
    
tree.sort(key=lambda x: x[2])

parent = list(range(n+1))

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a<b:
        parent[b] = a
    else:
        parent[a] = b
        
def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
        
    return parent[a]

ans = 0

for a, b, c in tree:
    if find(a) != find(b):
        union(a, b)
        ans += c
        
print(ans)


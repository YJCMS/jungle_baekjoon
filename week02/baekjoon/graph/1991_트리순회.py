import sys
sys.setrecursionlimit(10**8)

n = int(sys.stdin.readline())
graph = {}

for i in range(n):
    root, left, right = map(str, sys.stdin.readline().split())
    graph[root] = left, right

def preorder(v): # 전위순회
    if v != ".":
        print(v, end='')
        preorder(graph[v][0])
        preorder(graph[v][1])

def inorder(v): # 중위순회
    if v != ".":
        inorder(graph[v][0])
        print(v, end='')
        inorder(graph[v][1])

def postorder(v): # 후위순회
    if v != ".":
        postorder(graph[v][0])
        postorder(graph[v][1])
        print(v, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
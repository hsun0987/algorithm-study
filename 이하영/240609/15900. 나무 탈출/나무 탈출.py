# 리프노드에서 부모노드까지 올라감
# 루트노드까지에서 루트노드들까지 깊이 합이 홀수면 성원이가 승
import sys
sys.setrecursionlimit((10**5) * 5)

input = sys.stdin.readline

def DFS(v):
    visited[v] = True
    
    for i in tree[v]:
        if not visited[i]:
            depth[i] = depth[v] + 1 #자식 노드로 내려갈 때마다 깊이 +1 해줌
            DFS(i)

N = int(input())

tree = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
depth = [0 for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    
DFS(1)
result = 0
for i in range(2, N+1):
    if len(tree[i]) == 1: #연결된 노드가 하나 뿐이라면 부모 노드임
        result += depth[i]

if result % 2 == 0: #짝수라면
    print("No")
else:
    print("Yes")
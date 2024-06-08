import sys

T = int(sys.stdin.readline())

def DFS(v, count):
    visited[v] = True
    
    for i in graph[v]:
        if not visited[i]:
            count = DFS(i, count + 1) 
    return count

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)]
    
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
        
    visited = [False for _ in range(N+1)]
    cnt = 0
    
    print(DFS(1, cnt))
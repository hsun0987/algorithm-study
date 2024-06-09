# 루트노드에서 가장 먼 노드가 경로가 긴 노드에 해당하는 노드 중 하나
# 그 노드를 기준으로 탐색을 하며 가중치의 합들을 구함
# 가장 큰 합이 정답 (max)

import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

def DFS(v, d):
    visited[v] = True
    
    for i, dist in tree[v]:
        if not visited[i]:
            distance[i] = d + dist # 지금까지의 거리 + 다음 노드까지의 거리
            DFS(i, distance[i])

N = int(input())

tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, D = map(int, input().split())
    tree[a].append([b, D])
    tree[b].append([a, D])

visited = [False for _ in range(N+1)] 
distance = [0 for _ in range(N+1)]
distance[1] = 0
DFS(1, distance[1])

long_node = distance.index(max(distance)) #가장 큰 값을 가지고 있는 인덱스가 루트에서 가장 긴 거리의 노드

visited = [False for _ in range(N+1)] 
distance = [0 for _ in range(N+1)]
distance[long_node] = 0
DFS(long_node, distance[long_node])

print(max(distance))


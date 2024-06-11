#DFS로 탐색 =  물 주기 // ->  리프노드의 수만 구하면 되므로 DFS할 필요 없음
# 더 이상 물이 움직이지 않는 상태 = 리프노드
# 기댓값 : 값1 * 값1의 확률 + 값2 * 값2의 확률 + ...
# 물이 고르게 분포되는 것이 평균 -> 물의 양 / 리프노드의 수

import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, W = map(int, input().split()) # N = 노드 수, W = 1번 노드에 고인 물의 양
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)
    
leaf_node = 0
for i in range(2, N+1): #루트노드 tree[1] 제외
    if len(tree[i]) == 1:
        leaf_node += 1
        
print(float(W / leaf_node))
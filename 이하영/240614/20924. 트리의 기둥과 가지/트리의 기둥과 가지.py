# 기둥 : 루트 노드 ~ 기가 노드
# 가지 : 기가 노드 ~ 리프 노드
# 기가 노드 : 루트노드를 제외하고 순회를 했을 때 가지 쪽에서 자식노드가 2개 이상인 첫 노드
# 가지 없이 기둥 뿐이면 리프노드 = 기가 노드
# 기둥 없이 가지 뿐이면 루트 노드 = 기가 노드
# 가지의 길이 = 가장 긴 가지의 길이가 대표

# 나무의 기둥 길이 = 기가노드까지의 간선 길이 -> 기가 노드는 자식노드가 2개인 노드 
import sys
sys.setrecursionlimit(2 * 10 ** 5)
input = sys.stdin.readline

N, R = map(int, input().split())  # 노드의 개수, 루트노드 번호

tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, d = map(int, input().split())  # a, b = 노드 d = 간선의 길이
    tree[a].append((b, d))
    tree[b].append((a, d))

result = [0, 0]
visited = [False for _ in range(N+1)]

def DFS(v, sum, op):  # op = 0은 기둥, op = 1은 가지
    visited[v] = True

    if op == 0:
        result[0] = sum  # 기가 노드까지의 간선 길이의 합
    else:
        result[1] = max(result[1], sum)  # 가장 긴 가지의 길이

    if op == 0:
        if v == R:  # 현재 노드가 루트 노드인 경우, 인접 노드가 2개 이상이면 기가 노드
            if len(tree[v]) > 1:
                op, sum = 1, 0
        else:  # 현재 노드가 루트 노드가 아닌 경우, 인접 노드가 2개보다 많으면 기가 노드
            if len(tree[v]) > 2:
                op, sum = 1, 0

    for next_node, distance in tree[v]:
        if not visited[next_node]:  # 방문하지 않은 노드만 탐색
            DFS(next_node, sum + distance, op)

DFS(R, 0, 0)  # 현재 노드, 현재까지 길이, 노드 위치

print(result[0], result[1])

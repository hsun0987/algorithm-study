# 입력받기
# 정점 1 ; 6, 4
# 정점 4 : 1, 2, 7
# 정점 6 : 1, 3
# 정점 7 : 4
# 정점 2 : 4
# 정점 3 : 6, 5

from collections import deque
import sys
sys.setrecursionlimit(1000000) # 재귀 횟수 셋팅
            
N = int(sys.stdin.readline()) #노드 개수
Visited = [False for _ in range(N+1)] #인덱스 1부터 시작
result = [0 for _ in range(N+1)]  #결과를 담을 리스트
Graph = [[] for _ in range(N+1)] #그래프 그릴 리스트

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    Graph[a].append(b)
    Graph[b].append(a)  #인접해있으므로 인덱스 a, b에 각각 추가
    
def DFS(v, graph, visited):
    visited[v] = True #탐색을 시작하면 방문했다는 표시를 함
    for i in graph[v]:  #인접 노드 탐색 시작 ex v가 1이라면 6, 4 탐색
        if not visited[i]: #방문한 적 없는 정점이라면, 탐색 시작
            result[i] = v  #자신(v)과 인접해있고, 첫 방문이라면 그 i는 v의 자식 노드(위에서 아래로 탐색하니까)
            DFS(i, graph, visited)

DFS(1, Graph, Visited) #1 이 루트이므로 1로 시작

for i in range(2, N+1):
    print(result[i])
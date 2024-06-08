# 자식노드에서 루트노드까지 거쳐가는 노드를 저장
# 구하려는 노드만 정보 빼냄
# 구하려는 두 노드 중 한 노드를 정해 루트까지 방문처리
# 다른 한 노드도 루트 노드까지 방문 -> 중간에 방문 처리한 노드 발견하면 그게 최소 공통 조상

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    
    parents = [0 for _ in range(N+1)]
    
    for _  in range(N-1):
        a, b = map(int, input().split()) #a는 b의 부모
        parents[b] = a
    
    x, y = map(int, input().split())
    
    visited = [False for _ in range(N+1)]
    
    visited[x] = True
    
    while parents[x] != 0: #부모 노드가 있을 때까지(루트노드까지)    
        x = parents[x] #x의 부모 노드로 올라감
        visited[x] = True
    
    while True:
        if visited[y] == True: #y를 방문한 흔적이 있다면, x에서 루트노드까지의 경로에도 포함된 노드이므로
            print(y) # 두 노드의 최소 공통 부모 노드는 y노드
            break
        else:
            y = parents[y]
# 제거할 노드가 부모 노드라면 그의 자식 노드도 제거
# 부모 노드들을 담은 리스트에 언급되지 않는 노드의 개수가 정답
# 자식 노드가 삭제돼서 리프노드가 된 경우 고려

import sys
sys.setrecursionlimit(10 ** 6)

def DFS(v):
    parents.append(nodes[v]) #삭제할 노드의 부모 노드 저장 -> 자식노드가 삭제돼서 리프노드가 된 경우 고려하기 위해
    visited[v] = False  #삭제한 노드는 False로 변경
    for i in range(N):
        if nodes[i] == v: # 제거할 노드를 부모 노드로 갖고 있는 노드가 있다면
            DFS(i) #그 자식 노드도 삭제함

N = int(sys.stdin.readline())
nodes = list(map(int, sys.stdin.readline().split()))
delete_node = int(sys.stdin.readline())
visited = [True for _ in range(N)]
parents = []
            
DFS(delete_node)

cnt = 0 
for i in range(N):
    if visited[i]: #삭제하지 않은 노드 중 
        if i not in nodes: #처음부터 리프노드여서 언급되지 않는 노드
            cnt += 1
        elif i in parents: #부모노드였지만 자식 노드가 삭제되어 리프 노드가 된 노드
            if parents.count(i) >= nodes.count(i): #자식노드가 2개 이상인데 1개만 삭제된 경우 고려(1개만 삭제되면 리프X)
                cnt += 1
print(cnt)


# 단절점 : A정점을 제거했을 때, 그래프가 2개 이상으로 나뉘는 경우
        # -> 연결된 노드가 2개 이상이면 단절점이 될 수 있음. = 1개인 경우 제외하고 전부 다 해당
# 단절선 : B간선을 제거했을 때, 그래프가 2개 이상으로 나뉘는 경우  
        # -> 간선은 노드와 노드를 이어주므로 항상 그래프가 2개로 나뉨
# 애드 혹 알고리즘 : 문제의 특성에 맞게 해결책을 찾아내는 방식 (문제 해석이 중요)
import sys

input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    
q = int(input())

for _ in range(q):
    t, k = map(int, input().split())
    
    if t == 1: # k번 정점이 단절점인지
        if(len(tree[k]) == 1):
            print("no")  # 연결된 노드가 하나 뿐이라면 단절점 X
        else:
            print("yes")
    elif t == 2: # k번 간선이 단절선인지
        print("yes")
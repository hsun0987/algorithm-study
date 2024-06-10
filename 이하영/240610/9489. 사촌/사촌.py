# 첫번째 수 -> 루트

import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

while True:
    n, k = map(int, input().split()) #n = 노드의 수, k = 사촌의 수를 구할 노드
    if n == 0 and k == 0:
        break
    node_set = [-1] + list(map(int, input().split()))
    
    parent = [0 for _ in range(n+1)] #부모 노드 저장
    parent[0] = -1 #인덱스 0에 접근하지 못하도록
    
    parent_idx = -1 # n 번째 부모노드
    k_idx = 0
    for i in range(1, n+1):
        if node_set[i] == k:
            k_idx = i #node_set에서 k가 들어있는 인덱스 
        if node_set[i] != node_set[i-1] + 1: #연속된 숫자가 아니라면
            parent_idx += 1 # 부모가 달라지므로 옆 칸으로 옮김(인덱스 이동)
            
        parent[i] = parent_idx #해당 노드의 부모가 몇 번째 부모인지 저장
        
    count = 0
        
    for i in range(1, n+1):
        if parent[i] != parent[k_idx] and parent[parent[i]] == parent[parent[k_idx]]: 
        # 부모는 같지 않고, 부모의 부모는 같으면
            count += 1
    print(count)